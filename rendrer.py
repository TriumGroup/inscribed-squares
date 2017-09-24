import sdl2

from inscribed_shapes import InscribedShapes


class Renderer:
    def __init__(self, window):
        self._window = window
        self.sdl_renderer = sdl2.SDL_CreateRenderer(
            self._window.sdl_window,
            -1,
            sdl2.SDL_RENDERER_ACCELERATED
        )

    @property
    def size(self):
        return self._window.size

    def resize(self):
        self._clear_draw_field()
        InscribedShapes(self).draw()
        sdl2.SDL_RenderPresent(self.sdl_renderer)

    def _clear_draw_field(self):
        sdl2.SDL_SetRenderDrawColor(self.sdl_renderer, 255, 255, 255, 255)
        sdl2.SDL_RenderClear(self.sdl_renderer)
        sdl2.SDL_SetRenderDrawColor(self.sdl_renderer, 0, 0, 0, 0)

