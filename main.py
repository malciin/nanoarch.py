import os
import lib.constants
import time
import sdl2
import sdl2.ext

from ctypes import *
from lib.enums import retro_pixel_format
from lib.structs import retro_game_info, retro_log_callback, retro_system_info

cmd_names = { v: k for k, v in vars(lib.constants).items() if isinstance(v, int) }
base_dir = os.path.dirname(__file__)

sdl2.ext.init()
window = sdl2.ext.Window("RGB Buffer", size=(160, 144))
window.show()
renderer = sdl2.SDL_CreateRenderer(window.window, -1, sdl2.SDL_RENDERER_ACCELERATED)
texture = sdl2.SDL_CreateTexture(renderer, sdl2.SDL_PIXELFORMAT_ARGB8888, sdl2.SDL_TEXTUREACCESS_STREAMING, 160, 144)

# Todo: to use python logs callback variadic arguments needs to be handled somehow
# https://cffi.readthedocs.io/en/stable/using.html#id27
# https://stackoverflow.com/a/13869542
@CFUNCTYPE(None, c_uint, c_char_p)
def log(level, message):
    print(level, message)

@CFUNCTYPE(c_bool, c_uint, c_void_p)
def set_environment(cmd, data):
    cmd_name = cmd_names[cmd] if cmd in cmd_names else f'Unknown: {cmd}'
    print(f'set_environment: {cmd_name}')

    if cmd == lib.constants.RETRO_ENVIRONMENT_GET_LOG_INTERFACE:
        return c_bool(False)
        # todo: If variadic arguments will be handled uncomment below lines to enable logging via log python method and comment out upper
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
    # ffmpeg -y -f rawvideo -pixel_format bgr0 -video_size 160x144 -i imgbuffer.raw -frames:v 1 output.png
    # with open('imgbuffer.raw', "wb") as f:
    #     data_ptr = cast(data, POINTER(c_ubyte))  # Cast void* to byte pointer
    #     for y in range(height):
    #         row_offset = y * pitch  # Move to the correct row
    #         f.write(bytearray(data_ptr[row_offset: row_offset + (width * 4)]))  # Write only valid pixel data
    data_ptr = cast(data, POINTER(c_ubyte))  # Cast void* to byte pointer
    sdl2.SDL_UpdateTexture(texture, None, data_ptr, width * 4)

@CFUNCTYPE(None)
def set_input_poll():
    # print('set_input_poll')
    pass

@CFUNCTYPE(c_int16, c_uint, c_uint, c_uint, c_uint)
def set_input_state(port, device, index, id):
    # print('set_input_state')
    return 0

@CFUNCTYPE(None, c_short, c_short)
def set_audio_sample(left, right):
    # print('set_audio_sample')
    pass

@CFUNCTYPE(c_size_t, c_void_p, c_size_t)
def set_audio_sample_batch(data, frames):
    # print('set_audio_sample_batch')
    return frames

dll = cdll.LoadLibrary(os.path.join(base_dir, 'sameboy_libretro.dll'))
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

print('Need fullpath', system_info_ptr.contents.need_fullpath)

rom = 'Tetris.gb'

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

print('retro_get_system_info called!')

start_time = time.time()
interval = 1 # displays the frame rate every 1 second
counter = 0

for i in range(1000):
    dll.retro_run()

    sdl2.SDL_RenderClear(renderer)
    sdl2.SDL_RenderCopy(renderer, texture, None, None)
    sdl2.SDL_RenderPresent(renderer)

    counter+=1
    if (time.time() - start_time) > interval:
        print("FPS: ", counter / (time.time() - start_time))
        counter = 0
        start_time = time.time()
print('Done!')
