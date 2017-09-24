import sdl2


class Renderer:
    def __init__(self, sdl_window):
        self.__renderer = sdl2.SDL_CreateRenderer(sdl_window, -1, sdl2.SDL_RENDERER_ACCELERATED)
        self.__clear_draw_field()

    def resize(self, window_size):
        self.__clear_draw_field()

    def __clear_draw_field(self):
        sdl2.SDL_SetRenderDrawColor(self.__renderer, 255, 255, 255, 255)
        sdl2.SDL_RenderClear(self.__renderer)
        sdl2.SDL_RenderPresent(self.__renderer)

    def __draw_point(self, point):
        x, y = point
        sdl2.SDL_RenderDrawPoint(self.__renderer, x, y)
