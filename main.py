import os
import lib.constants
import sdl2
import sdl2.ext

from ctypes import *
from lib.enums import retro_pixel_format
from lib.structs import retro_game_info, retro_log_callback, retro_system_info

### Configuration
window_size = (160, 144)
core = 'sameboy_libretro.dll'
rom = 'demo.gb' # Source of demo.gb rom: https://buildbot.libretro.com/assets/cores/Nintendo%20-%20GameBoy
###

cmd_names = { v: k for k, v in vars(lib.constants).items() if isinstance(v, int) }
scancodes = { v: k for k, v in vars(sdl2.scancode).items() if isinstance(v, int) }
base_dir = os.path.dirname(__file__)

sdl2.ext.init()
window = sdl2.ext.Window("nanoarch.py", size=window_size)
window.show()
renderer = sdl2.SDL_CreateRenderer(window.window, -1, sdl2.SDL_RENDERER_ACCELERATED)
texture = sdl2.SDL_CreateTexture(renderer, sdl2.SDL_PIXELFORMAT_ARGB8888, sdl2.SDL_TEXTUREACCESS_STREAMING, window_size[0], window_size[1])

pressed_scancodes: set[sdl2.SDL_Scancode] = set()

sdl2_scancode_to_joypad = {
    sdl2.SDL_SCANCODE_LEFT: lib.constants.RETRO_DEVICE_ID_JOYPAD_LEFT,
    sdl2.SDL_SCANCODE_RIGHT: lib.constants.RETRO_DEVICE_ID_JOYPAD_RIGHT,
    sdl2.SDL_SCANCODE_UP: lib.constants.RETRO_DEVICE_ID_JOYPAD_UP,
    sdl2.SDL_SCANCODE_DOWN: lib.constants.RETRO_DEVICE_ID_JOYPAD_DOWN,
    sdl2.SDL_SCANCODE_Z: lib.constants.RETRO_DEVICE_ID_JOYPAD_A,
    sdl2.SDL_SCANCODE_X: lib.constants.RETRO_DEVICE_ID_JOYPAD_B,
    sdl2.SDL_SCANCODE_RETURN: lib.constants.RETRO_DEVICE_ID_JOYPAD_START,
    sdl2.SDL_SCANCODE_BACKSPACE: lib.constants.RETRO_DEVICE_ID_JOYPAD_SELECT,
}
joypad_to_sdl2_scancode = { v: k for k, v in sdl2_scancode_to_joypad.items() }

# Todo: to use python logs callback variadic arguments needs to be handled somehow
# https://cffi.readthedocs.io/en/stable/using.html#id27
# https://stackoverflow.com/a/13869542
@CFUNCTYPE(None, c_uint, c_char_p)
def log(level, message):
    print(level, message)

@CFUNCTYPE(c_bool, c_uint, c_void_p)
def set_environment(cmd, data):
    if cmd == lib.constants.RETRO_ENVIRONMENT_GET_VARIABLE_UPDATE:
        # to skipping logs since its called many times
        return c_bool(True)

    cmd_name = cmd_names[cmd] if cmd in cmd_names else f'Unknown: {cmd}'
    print(f'set_environment: {cmd_name}')

    if cmd == lib.constants.RETRO_ENVIRONMENT_GET_LOG_INTERFACE:
        return c_bool(False)
        # todo: If variadic arguments will be handled uncomment below lines to enable logging via log python method and comment out upper line
        # pointer = cast(data, POINTER(retro_log_callback))
        # pointer.contents.log = log
        # return c_bool(True)

    if cmd == lib.constants.RETRO_ENVIRONMENT_GET_CAN_DUPE:
        cast(data, POINTER(c_ubyte))[0] = 1
        return c_bool(True)
    
    if cmd == lib.constants.RETRO_ENVIRONMENT_SET_PIXEL_FORMAT:
        format = cast(data, POINTER(c_uint))[0]

        if format == retro_pixel_format.RETRO_PIXEL_FORMAT_0RGB1555:
            print(f'Pixel format not yet implemented: {format}')
            return c_bool(False)
        elif format == retro_pixel_format.RETRO_PIXEL_FORMAT_XRGB8888:
            print(f'Pixel format set to XRGB8888')
            return c_bool(True)
        elif format == retro_pixel_format.RETRO_PIXEL_FORMAT_RGB565:
            print(f'Pixel format not yet implemented: {format}')
            return c_bool(False)
        else:
            print(f'Invalid pixel format: {format}')
            return c_bool(False)

    if cmd == lib.constants.RETRO_ENVIRONMENT_GET_SYSTEM_DIRECTORY or cmd == lib.constants.RETRO_ENVIRONMENT_GET_SAVE_DIRECTORY:
        buffer = create_string_buffer(b'.')
        pointer = cast(data, POINTER(c_void_p))
        pointer[0] = cast(buffer, c_void_p)

        return c_bool(True)

    return c_bool(True)

@CFUNCTYPE(None, c_void_p, c_uint, c_uint, c_size_t)
def set_video_refresh(data, width, height, pitch):
    data_ptr = cast(data, POINTER(c_ubyte))
    sdl2.SDL_UpdateTexture(texture, None, data_ptr, pitch)

@CFUNCTYPE(None)
def set_input_poll():
    pass

@CFUNCTYPE(c_int16, c_uint, c_uint, c_uint, c_uint)
def set_input_state(port, device, index, id):
    if port != 0:
        print('Another player unsupported')
        return 0
    
    if device != lib.constants.RETRO_DEVICE_JOYPAD:
        print('Unsupported device:', cmd_names[device])
        return 0

    if id == lib.constants.RETRO_DEVICE_ID_JOYPAD_MASK:
        mask = 0
        for code in pressed_scancodes:
            if code in sdl2_scancode_to_joypad:
                mask |= 1 << sdl2_scancode_to_joypad[code]
        return mask

    if id in joypad_to_sdl2_scancode:
        return 1 if joypad_to_sdl2_scancode[id] in pressed_scancodes else 0
    return 0

@CFUNCTYPE(None, c_short, c_short)
def set_audio_sample(left, right):
    pass

@CFUNCTYPE(c_size_t, c_void_p, c_size_t)
def set_audio_sample_batch(data, frames):
    return frames

dll = cdll.LoadLibrary(os.path.join(base_dir, core))
dll.retro_set_environment(set_environment)
dll.retro_set_video_refresh(set_video_refresh)
dll.retro_set_input_poll(set_input_poll)
dll.retro_set_input_state(set_input_state)
dll.retro_set_audio_sample(set_audio_sample)
dll.retro_set_audio_sample_batch(set_audio_sample_batch)
dll.retro_init()

print('Core loaded')

system_info_ptr = POINTER(retro_system_info)(retro_system_info())

dll.retro_get_system_info(system_info_ptr)

with open(rom, 'rb') as f:
    data = f.read()

game_info = retro_game_info(
    path = os.path.join(base_dir, rom).encode('utf-8'),
    size = len(data),
    data = cast(c_char_p(data), c_void_p),
)
if dll.retro_load_game(POINTER(retro_game_info)(game_info)) == 0:
    print('Failed to load game!')
    exit(1)

running = True

while running:
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_QUIT:
            running = False
        if event.type == sdl2.SDL_KEYUP:
            if event.key.keysym.scancode in pressed_scancodes:
                pressed_scancodes.remove(event.key.keysym.scancode)
                print('Detected previous pressed key release:', scancodes[event.key.keysym.scancode])
        if event.type == sdl2.SDL_KEYDOWN:
            if event.key.keysym.scancode not in pressed_scancodes:
                pressed_scancodes.add(event.key.keysym.scancode)
                print('Detected new keypress:', scancodes[event.key.keysym.scancode])

    dll.retro_run()

    sdl2.SDL_RenderCopy(renderer, texture, None, None)
    sdl2.SDL_RenderPresent(renderer)
    sdl2.SDL_Delay(20)
