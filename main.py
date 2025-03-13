import os
from ctypes import *
import lib.constants
from lib.structs import retro_system_info

cmd_names = { v: k for k, v in vars(lib.constants).items() if isinstance(v, int) }

@CFUNCTYPE(c_bool, c_uint, c_void_p)
def set_environment(cmd, data):
    cmd_name = cmd_names[cmd] if cmd in cmd_names else f'Unknown: {cmd}'
    print(f'set_environment: {cmd_name}')

    if cmd == lib.constants.RETRO_ENVIRONMENT_GET_LOG_INTERFACE:
        return c_bool(False)
    
    if cmd == lib.constants.RETRO_ENVIRONMENT_GET_CAN_DUPE:
        cast(data, POINTER(c_ubyte))[0] = 1
        return c_bool(True)
    
    if cmd == lib.constants.RETRO_ENVIRONMENT_GET_SYSTEM_DIRECTORY or cmd == lib.constants.RETRO_ENVIRONMENT_GET_SAVE_DIRECTORY:
        buffer = create_string_buffer(b'.')
        pointer = cast(data, POINTER(c_void_p))
        pointer[0] = cast(buffer, c_void_p)

        return c_bool(True)

    return c_bool(True)

@CFUNCTYPE(None, c_void_p, c_uint, c_uint, c_byte)
def set_video_refresh(data, width, height, pitch):
    pass

@CFUNCTYPE(None)
def set_input_poll():
    pass

@CFUNCTYPE(c_short, c_uint, c_uint, c_uint, c_uint)
def set_input_state(port, device, index, id):
    return c_short(0)

@CFUNCTYPE(None, c_short, c_short)
def set_audio_sample(left, right):
    pass

@CFUNCTYPE(c_uint, c_void_p, c_uint)
def set_audio_sample_batch(data, frames):
    return c_uint(0)

dll = cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), 'sameboy_libretro.dll'))
dll.retro_set_environment(set_environment)
dll.retro_set_video_refresh(set_video_refresh)
dll.retro_set_input_poll(set_input_poll)
dll.retro_set_input_state(set_input_state)
dll.retro_set_audio_sample(set_audio_sample)
dll.retro_set_audio_sample_batch(set_audio_sample_batch)
dll.retro_init()

print('Core loaded')

system_info = retro_system_info()

dll.retro_get_system_info(POINTER(retro_system_info)(system_info))

print('retro_get_system_info called!')
