import sdl2

from math import trunc, tan, pi


class InscribedShapes:
    PADDING = 20
    INSCRIBED_SHAPES_COUNT = 16
    DEFAULT_ANGLE = pi / INSCRIBED_SHAPES_COUNT

    def __init__(self, renderer, shift_angle=DEFAULT_ANGLE):
        self._renderer = renderer
        self._shift_angle = shift_angle
        self._points = self._prepare_points_for_square(self._renderer.size)

    def draw(self):
        self._draw_shape()
        for i in range(self.INSCRIBED_SHAPES_COUNT):
            self._points = list(map(self._shift_points, enumerate(self._points)))
            self._draw_shape()

    def _shift_points(self, iterable):
        index, point = iterable
        return self._shift_point(point, self._next_point(index))

    def _next_point(self, current_point_index):
        return self._points[(current_point_index + 1) % len(self._points)]

    def _shift_point(self, base_point, next_point):
        base_x, base_y = base_point
        next_x, next_y = next_point
        return self._shift_coordinate(base_x, next_x), self._shift_coordinate(base_y, next_y)

    def _shift_coordinate(self, base_coordinate, next_coordinate):
        return (1 - self._clipping_factor()) * base_coordinate + self._clipping_factor() * next_coordinate

    def _clipping_factor(self):
        return tan(self._shift_angle) / (tan(self._shift_angle) + 1)

    def _draw_shape(self):
        points_length = len(self._points)
        for i, point in enumerate(self._points):
            next_point = self._points[(i + 1) % points_length]
            self._connect_points(point, next_point)

    def _connect_points(self, start_point, end_point):
        start_point_x, start_point_y = start_point
        end_point_x, end_point_y = end_point
        sdl2.SDL_RenderDrawLine(
            self._renderer.sdl_renderer,
            trunc(start_point_x),
            trunc(start_point_y),
            trunc(end_point_x),
            trunc(end_point_y)
        )

    def _draw_point(self, point):
        x, y = point
        sdl2.SDL_RenderDrawPoint(self._renderer.sdl_renderer, x, y)

    def _prepare_points_for_square(self, renderer_size):
        width, height = renderer_size
        return [
            (self.PADDING, self.PADDING),
            (width - self.PADDING, self.PADDING),
            (width - self.PADDING, height - self.PADDING),
            (self.PADDING, height - self.PADDING)
        ]
