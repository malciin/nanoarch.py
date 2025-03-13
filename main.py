import os
from ctypes import *

@CFUNCTYPE(c_bool, c_uint, c_void_p)
def set_environment(cmd, data):
    print('set_environment', cmd, data)
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