from ctypes import *

class retro_system_info(Structure):
    _fields_ = [
        ('library_name', c_char_p),
        ('library_version', c_char_p),
        ('valid_extensions', c_char_p),
        ('need_fullpath', c_bool),
        ('block_extract', c_bool),
    ]
