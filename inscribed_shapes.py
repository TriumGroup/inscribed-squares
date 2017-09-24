import sdl2

from math import tan, pi
from line import Line


class InscribedShapes:
    PADDING = 20
    INSCRIBED_SHAPES_COUNT = 16
    DEFAULT_ANGLE = pi / INSCRIBED_SHAPES_COUNT

    def __init__(self, renderer, shift_angle=DEFAULT_ANGLE):
        self._renderer = renderer
        self._shift_angle = shift_angle
        self._points = self._prepare_points_for_square(self._renderer.size)

    def draw(self):
        for i in range(self.INSCRIBED_SHAPES_COUNT + 1):
            self._draw_shape()
            self._shift_points()

    def _prepare_points_for_square(self, renderer_size):
        width, height = renderer_size
        return [
            (self.PADDING, self.PADDING),
            (width - self.PADDING, self.PADDING),
            (width - self.PADDING, height - self.PADDING),
            (self.PADDING, height - self.PADDING)
        ]

    def _draw_shape(self):
        for point_with_index in enumerate(self._points):
            shape_side = self._neighboring_points(point_with_index)
            self._draw_side(shape_side)

    def _neighboring_points(self, point_with_index):
        point_index, point = point_with_index
        return point + self._next_point(point_index)

    def _next_point(self, current_point_index):
        return self._points[(current_point_index + 1) % len(self._points)]

    def _shift_points(self):
        self._points = list(map(self._shifted_point, enumerate(self._points)))

    def _shifted_point(self, point_with_index):
        x, y, next_x, next_y = self._neighboring_points(point_with_index)
        return self._shifted_coordinate(x, next_x), self._shifted_coordinate(y, next_y)

    def _shifted_coordinate(self, base_coordinate, next_coordinate):
        return (1 - self._clipping_factor()) * base_coordinate + self._clipping_factor() * next_coordinate

    def _clipping_factor(self):
        return tan(self._shift_angle) / (tan(self._shift_angle) + 1)

    def _draw_side(self, side):
        Line(self._renderer.sdl_renderer, side).draw()
