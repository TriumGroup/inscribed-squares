import ctypes
import sdl2

from rendrer import Renderer


class Window:
    def __init__(self, title, width=500, height=500):
        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
        self.__sdl_window = sdl2.SDL_CreateWindow(
            title,
            sdl2.SDL_WINDOWPOS_CENTERED,
            sdl2.SDL_WINDOWPOS_CENTERED,
            width,
            height,
            sdl2.SDL_WINDOW_RESIZABLE
        )
        self.renderer = Renderer(self.__sdl_window)

    def resize(self):
        self.renderer.resize(self.__window_size())

    def close(self):
        sdl2.SDL_DestroyWindow(self.__sdl_window)
        sdl2.SDL_Quit()

    def __window_size(self):
        width = ctypes.c_int()
        height = ctypes.c_int()
        sdl2.SDL_GetWindowSize(self.__sdl_window, ctypes.byref(width), ctypes.byref(height))
        return width.value, height.value
