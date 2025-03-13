from ctypes import *

class retro_system_info(Structure):
    _fields_ = [
        ('library_name', c_char_p),
        ('library_version', c_char_p),
        ('valid_extensions', c_char_p),
        ('need_fullpath', c_bool),
        ('block_extract', c_bool),
    ]

class retro_log_callback(Structure):
    _fields_ = [
        ('log', CFUNCTYPE(None, c_uint, c_char_p)),
    ]

class retro_game_info(Structure):
    _fields_ = [
        ('path', c_char_p),
        ('data', c_void_p),
        ('size', c_size_t),
        ('meta', c_char_p),
    ]
