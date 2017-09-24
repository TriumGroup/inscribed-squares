import sdl2

from inscribed_shapes import InscribedShapes


class Renderer:
    def __init__(self, window):
        self.__window = window
        self.__sdl_renderer = sdl2.SDL_CreateRenderer(
            self.__window.sdl_window,
            -1,
            sdl2.SDL_RENDERER_ACCELERATED
        )
        self.__inscribed_shapes = InscribedShapes(self)

    @property
    def sdl_renderer(self):
        return self.__sdl_renderer

    @property
    def size(self):
        return self.__window.size

    def redraw(self):
        self.__clear_draw_field()
        self.__inscribed_shapes.draw_squares()
        sdl2.SDL_RenderPresent(self.__sdl_renderer)

    def __clear_draw_field(self):
        sdl2.SDL_SetRenderDrawColor(self.__sdl_renderer, 255, 255, 255, 255)
        sdl2.SDL_RenderClear(self.__sdl_renderer)
        sdl2.SDL_SetRenderDrawColor(self.__sdl_renderer, 0, 0, 0, 0)

