# cat libretro.h | grep '^#define' > constants.h
RETRO_API_VERSION =         1
RETRO_DEVICE_TYPE_SHIFT =         8
RETRO_DEVICE_MASK =               ((1 << RETRO_DEVICE_TYPE_SHIFT) - 1)
# RETRO_DEVICE_SUBCLASS =(base, id) (((id + 1) << RETRO_DEVICE_TYPE_SHIFT) | base)
RETRO_DEVICE_NONE =         0
RETRO_DEVICE_JOYPAD =       1
RETRO_DEVICE_MOUSE =        2
RETRO_DEVICE_KEYBOARD =     3
RETRO_DEVICE_LIGHTGUN =     4
RETRO_DEVICE_ANALOG =       5
RETRO_DEVICE_POINTER =      6
RETRO_DEVICE_ID_JOYPAD_B =        0
RETRO_DEVICE_ID_JOYPAD_Y =        1
RETRO_DEVICE_ID_JOYPAD_SELECT =   2
RETRO_DEVICE_ID_JOYPAD_START =    3
RETRO_DEVICE_ID_JOYPAD_UP =       4
RETRO_DEVICE_ID_JOYPAD_DOWN =     5
RETRO_DEVICE_ID_JOYPAD_LEFT =     6
RETRO_DEVICE_ID_JOYPAD_RIGHT =    7
RETRO_DEVICE_ID_JOYPAD_A =        8
RETRO_DEVICE_ID_JOYPAD_X =        9
RETRO_DEVICE_ID_JOYPAD_L =       10
RETRO_DEVICE_ID_JOYPAD_R =       11
RETRO_DEVICE_ID_JOYPAD_L2 =      12
RETRO_DEVICE_ID_JOYPAD_R2 =      13
RETRO_DEVICE_ID_JOYPAD_L3 =      14
RETRO_DEVICE_ID_JOYPAD_R3 =      15
RETRO_DEVICE_ID_JOYPAD_MASK =    256
RETRO_DEVICE_INDEX_ANALOG_LEFT =       0
RETRO_DEVICE_INDEX_ANALOG_RIGHT =      1
RETRO_DEVICE_INDEX_ANALOG_BUTTON =     2
RETRO_DEVICE_ID_ANALOG_X =             0
RETRO_DEVICE_ID_ANALOG_Y =             1
RETRO_DEVICE_ID_MOUSE_X =                0
RETRO_DEVICE_ID_MOUSE_Y =                1
RETRO_DEVICE_ID_MOUSE_LEFT =             2
RETRO_DEVICE_ID_MOUSE_RIGHT =            3
RETRO_DEVICE_ID_MOUSE_WHEELUP =          4
RETRO_DEVICE_ID_MOUSE_WHEELDOWN =        5
RETRO_DEVICE_ID_MOUSE_MIDDLE =           6
RETRO_DEVICE_ID_MOUSE_HORIZ_WHEELUP =    7
RETRO_DEVICE_ID_MOUSE_HORIZ_WHEELDOWN =  8
RETRO_DEVICE_ID_MOUSE_BUTTON_4 =         9
RETRO_DEVICE_ID_MOUSE_BUTTON_5 =         10
RETRO_DEVICE_ID_LIGHTGUN_SCREEN_X =        13 #Absolute Position*/
RETRO_DEVICE_ID_LIGHTGUN_SCREEN_Y =        14 #Absolute Position*/
RETRO_DEVICE_ID_LIGHTGUN_IS_OFFSCREEN =    15 #Status Check*/
RETRO_DEVICE_ID_LIGHTGUN_TRIGGER =          2
RETRO_DEVICE_ID_LIGHTGUN_RELOAD =          16 #Forced off-screen shot*/
RETRO_DEVICE_ID_LIGHTGUN_AUX_A =            3
RETRO_DEVICE_ID_LIGHTGUN_AUX_B =            4
RETRO_DEVICE_ID_LIGHTGUN_START =            6
RETRO_DEVICE_ID_LIGHTGUN_SELECT =           7
RETRO_DEVICE_ID_LIGHTGUN_AUX_C =            8
RETRO_DEVICE_ID_LIGHTGUN_DPAD_UP =          9
RETRO_DEVICE_ID_LIGHTGUN_DPAD_DOWN =       10
RETRO_DEVICE_ID_LIGHTGUN_DPAD_LEFT =       11
RETRO_DEVICE_ID_LIGHTGUN_DPAD_RIGHT =      12
RETRO_DEVICE_ID_LIGHTGUN_X =                0 #Relative Position*/
RETRO_DEVICE_ID_LIGHTGUN_Y =                1 #Relative Position*/
RETRO_DEVICE_ID_LIGHTGUN_CURSOR =           3 #Use Aux:A instead*/
RETRO_DEVICE_ID_LIGHTGUN_TURBO =            4 #Use Aux:B instead*/
RETRO_DEVICE_ID_LIGHTGUN_PAUSE =            5 #Use Start instead*/
RETRO_DEVICE_ID_POINTER_X =             0
RETRO_DEVICE_ID_POINTER_Y =             1
RETRO_DEVICE_ID_POINTER_PRESSED =       2
RETRO_DEVICE_ID_POINTER_COUNT =         3
RETRO_DEVICE_ID_POINTER_IS_OFFSCREEN = 15
RETRO_REGION_NTSC =  0
RETRO_REGION_PAL =   1
RETRO_MEMORY_MASK =        0xff
RETRO_MEMORY_SAVE_RAM =    0
RETRO_MEMORY_RTC =         1
RETRO_MEMORY_SYSTEM_RAM =  2
RETRO_MEMORY_VIDEO_RAM =   3
RETRO_ENVIRONMENT_EXPERIMENTAL = 0x10000
RETRO_ENVIRONMENT_PRIVATE = 0x20000
RETRO_ENVIRONMENT_SET_ROTATION =  1
RETRO_ENVIRONMENT_GET_OVERSCAN =  2
RETRO_ENVIRONMENT_GET_CAN_DUPE =  3
RETRO_ENVIRONMENT_SET_MESSAGE =   6
RETRO_ENVIRONMENT_SHUTDOWN =      7
RETRO_ENVIRONMENT_SET_PERFORMANCE_LEVEL = 8
RETRO_ENVIRONMENT_GET_SYSTEM_DIRECTORY = 9
RETRO_ENVIRONMENT_SET_PIXEL_FORMAT = 10
RETRO_ENVIRONMENT_SET_INPUT_DESCRIPTORS = 11
RETRO_ENVIRONMENT_SET_KEYBOARD_CALLBACK = 12
RETRO_ENVIRONMENT_SET_DISK_CONTROL_INTERFACE = 13
RETRO_ENVIRONMENT_SET_HW_RENDER = 14
RETRO_ENVIRONMENT_GET_VARIABLE = 15
RETRO_ENVIRONMENT_SET_VARIABLES = 16
RETRO_ENVIRONMENT_GET_VARIABLE_UPDATE = 17
RETRO_ENVIRONMENT_SET_SUPPORT_NO_GAME = 18
RETRO_ENVIRONMENT_GET_LIBRETRO_PATH = 19
RETRO_ENVIRONMENT_SET_FRAME_TIME_CALLBACK = 21
RETRO_ENVIRONMENT_SET_AUDIO_CALLBACK = 22
RETRO_ENVIRONMENT_GET_RUMBLE_INTERFACE = 23
RETRO_ENVIRONMENT_GET_INPUT_DEVICE_CAPABILITIES = 24
RETRO_ENVIRONMENT_GET_SENSOR_INTERFACE = (25 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_CAMERA_INTERFACE = (26 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_LOG_INTERFACE = 27
RETRO_ENVIRONMENT_GET_PERF_INTERFACE = 28
RETRO_ENVIRONMENT_GET_LOCATION_INTERFACE = 29
RETRO_ENVIRONMENT_GET_CONTENT_DIRECTORY = 30
RETRO_ENVIRONMENT_GET_CORE_ASSETS_DIRECTORY = 30
RETRO_ENVIRONMENT_GET_SAVE_DIRECTORY = 31
RETRO_ENVIRONMENT_SET_SYSTEM_AV_INFO = 32
RETRO_ENVIRONMENT_SET_PROC_ADDRESS_CALLBACK = 33
RETRO_ENVIRONMENT_SET_SUBSYSTEM_INFO = 34
RETRO_ENVIRONMENT_SET_CONTROLLER_INFO = 35
RETRO_ENVIRONMENT_SET_MEMORY_MAPS = (36 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_SET_GEOMETRY = 37
RETRO_ENVIRONMENT_GET_USERNAME = 38
RETRO_ENVIRONMENT_GET_LANGUAGE = 39
RETRO_ENVIRONMENT_GET_CURRENT_SOFTWARE_FRAMEBUFFER = (40 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_HW_RENDER_INTERFACE = (41 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_SET_SUPPORT_ACHIEVEMENTS = (42 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_SET_HW_RENDER_CONTEXT_NEGOTIATION_INTERFACE = (43 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_SET_SERIALIZATION_QUIRKS = 44
RETRO_ENVIRONMENT_SET_HW_SHARED_CONTEXT = (44 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_VFS_INTERFACE = (45 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_LED_INTERFACE = (46 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_AUDIO_VIDEO_ENABLE = (47 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_MIDI_INTERFACE = (48 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_FASTFORWARDING = (49 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_TARGET_REFRESH_RATE = (50 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_INPUT_BITMASKS = (51 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_CORE_OPTIONS_VERSION = 52
RETRO_ENVIRONMENT_SET_CORE_OPTIONS = 53
RETRO_ENVIRONMENT_SET_CORE_OPTIONS_INTL = 54
RETRO_ENVIRONMENT_SET_CORE_OPTIONS_DISPLAY = 55
RETRO_ENVIRONMENT_GET_PREFERRED_HW_RENDER = 56
RETRO_ENVIRONMENT_GET_DISK_CONTROL_INTERFACE_VERSION = 57
RETRO_ENVIRONMENT_SET_DISK_CONTROL_EXT_INTERFACE = 58
RETRO_ENVIRONMENT_GET_MESSAGE_INTERFACE_VERSION = 59
RETRO_ENVIRONMENT_SET_MESSAGE_EXT = 60
RETRO_ENVIRONMENT_GET_INPUT_MAX_USERS = 61
RETRO_ENVIRONMENT_SET_AUDIO_BUFFER_STATUS_CALLBACK = 62
RETRO_ENVIRONMENT_SET_MINIMUM_AUDIO_LATENCY = 63
RETRO_ENVIRONMENT_SET_FASTFORWARDING_OVERRIDE = 64
RETRO_ENVIRONMENT_SET_CONTENT_INFO_OVERRIDE = 65
RETRO_ENVIRONMENT_GET_GAME_INFO_EXT = 66
RETRO_ENVIRONMENT_SET_CORE_OPTIONS_V2 = 67
RETRO_ENVIRONMENT_SET_CORE_OPTIONS_V2_INTL = 68
RETRO_ENVIRONMENT_SET_CORE_OPTIONS_UPDATE_DISPLAY_CALLBACK = 69
RETRO_ENVIRONMENT_SET_VARIABLE = 70
RETRO_ENVIRONMENT_GET_THROTTLE_STATE = (71 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_SAVESTATE_CONTEXT = (72 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_HW_RENDER_CONTEXT_NEGOTIATION_INTERFACE_SUPPORT = (73 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_JIT_CAPABLE = 74
RETRO_ENVIRONMENT_GET_MICROPHONE_INTERFACE = (75 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_DEVICE_POWER = (77 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_SET_NETPACKET_INTERFACE = 78
RETRO_ENVIRONMENT_GET_DEVICE_POWER = (77 | RETRO_ENVIRONMENT_EXPERIMENTAL)
RETRO_ENVIRONMENT_GET_PLAYLIST_DIRECTORY = 79
RETRO_ENVIRONMENT_GET_FILE_BROWSER_START_DIRECTORY = 80
RETRO_VFS_FILE_ACCESS_READ =            (1 << 0)
RETRO_VFS_FILE_ACCESS_WRITE =           (1 << 1)
RETRO_VFS_FILE_ACCESS_READ_WRITE =      (RETRO_VFS_FILE_ACCESS_READ | RETRO_VFS_FILE_ACCESS_WRITE)
RETRO_VFS_FILE_ACCESS_UPDATE_EXISTING = (1 << 2) # Prevents discarding content of existing files opened for writing */
RETRO_VFS_FILE_ACCESS_HINT_NONE =              (0)
RETRO_VFS_FILE_ACCESS_HINT_FREQUENT_ACCESS =   (1 << 0)
RETRO_VFS_SEEK_POSITION_START =    0
RETRO_VFS_SEEK_POSITION_CURRENT =  1
RETRO_VFS_SEEK_POSITION_END =      2
RETRO_VFS_STAT_IS_VALID =               (1 << 0)
RETRO_VFS_STAT_IS_DIRECTORY =           (1 << 1)
RETRO_VFS_STAT_IS_CHARACTER_SPECIAL =   (1 << 2)
RETRO_SERIALIZATION_QUIRK_INCOMPLETE = (1 << 0)
RETRO_SERIALIZATION_QUIRK_MUST_INITIALIZE = (1 << 1)
RETRO_SERIALIZATION_QUIRK_CORE_VARIABLE_SIZE = (1 << 2)
RETRO_SERIALIZATION_QUIRK_FRONT_VARIABLE_SIZE = (1 << 3)
RETRO_SERIALIZATION_QUIRK_SINGLE_SESSION = (1 << 4)
RETRO_SERIALIZATION_QUIRK_ENDIAN_DEPENDENT = (1 << 5)
RETRO_SERIALIZATION_QUIRK_PLATFORM_DEPENDENT = (1 << 6)
RETRO_MEMDESC_CONST =      (1 << 0)
RETRO_MEMDESC_BIGENDIAN =  (1 << 1)
RETRO_MEMDESC_SYSTEM_RAM = (1 << 2)
RETRO_MEMDESC_SAVE_RAM =   (1 << 3)
RETRO_MEMDESC_VIDEO_RAM =  (1 << 4)
RETRO_MEMDESC_ALIGN_2 =    (1 << 16)
RETRO_MEMDESC_ALIGN_4 =    (2 << 16)
RETRO_MEMDESC_ALIGN_8 =    (3 << 16)
RETRO_MEMDESC_MINSIZE_2 =  (1 << 24)
RETRO_MEMDESC_MINSIZE_4 =  (2 << 24)
RETRO_MEMDESC_MINSIZE_8 =  (3 << 24)
RETRO_SIMD_SSE =      (1 << 0)
RETRO_SIMD_SSE2 =     (1 << 1)
RETRO_SIMD_VMX =      (1 << 2)
RETRO_SIMD_VMX128 =   (1 << 3)
RETRO_SIMD_AVX =      (1 << 4)
RETRO_SIMD_NEON =     (1 << 5)
RETRO_SIMD_SSE3 =     (1 << 6)
RETRO_SIMD_SSSE3 =    (1 << 7)
RETRO_SIMD_MMX =      (1 << 8)
RETRO_SIMD_MMXEXT =   (1 << 9)
RETRO_SIMD_SSE4 =     (1 << 10)
RETRO_SIMD_SSE42 =    (1 << 11)
RETRO_SIMD_AVX2 =     (1 << 12)
RETRO_SIMD_VFPU =     (1 << 13)
RETRO_SIMD_PS =       (1 << 14)
RETRO_SIMD_AES =      (1 << 15)
RETRO_SIMD_VFPV3 =    (1 << 16)
RETRO_SIMD_VFPV4 =    (1 << 17)
RETRO_SIMD_POPCNT =   (1 << 18)
RETRO_SIMD_MOVBE =    (1 << 19)
RETRO_SIMD_CMOV =     (1 << 20)
RETRO_SIMD_ASIMD =    (1 << 21)
RETRO_SENSOR_ACCELEROMETER_X = 0
RETRO_SENSOR_ACCELEROMETER_Y = 1
RETRO_SENSOR_ACCELEROMETER_Z = 2
RETRO_SENSOR_GYROSCOPE_X = 3
RETRO_SENSOR_GYROSCOPE_Y = 4
RETRO_SENSOR_GYROSCOPE_Z = 5
RETRO_SENSOR_ILLUMINANCE = 6
# RETRO_HW_FRAME_BUFFER_VALID = ((void*)-1)
RETRO_NETPACKET_UNRELIABLE =  0        # Packet to be sent unreliable, depending on network quality it might not arrive. */
RETRO_NETPACKET_RELIABLE =    (1 << 0) # Reliable packets are guaranteed to arrive at the target in the order they were sent. */
RETRO_NETPACKET_UNSEQUENCED = (1 << 1) # Packet will not be sequenced with other packets and may arrive out of order. Cannot be set on reliable packets. */
RETRO_NETPACKET_FLUSH_HINT =  (1 << 2) # Request the packet and any previously buffered ones to be sent immediately */
RETRO_NETPACKET_BROADCAST = 0xFFFF
RETRO_NUM_CORE_OPTION_VALUES_MAX = 128
RETRO_MEMORY_ACCESS_WRITE = (1 << 0)
RETRO_MEMORY_ACCESS_READ = (1 << 1)
RETRO_MEMORY_TYPE_CACHED = (1 << 0)
RETRO_THROTTLE_NONE =              0
RETRO_THROTTLE_FRAME_STEPPING =    1
RETRO_THROTTLE_FAST_FORWARD =      2
RETRO_THROTTLE_SLOW_MOTION =       3
RETRO_THROTTLE_REWINDING =         4
RETRO_THROTTLE_VSYNC =             5
RETRO_THROTTLE_UNBLOCKED =         6
RETRO_MICROPHONE_INTERFACE_VERSION = 1
RETRO_POWERSTATE_NO_ESTIMATE = (-1)
