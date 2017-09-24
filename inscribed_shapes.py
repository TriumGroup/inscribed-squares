from math import tan, pi
from line import Line
from square import Square


class InscribedShapes:
    DEFAULT_NESTING_LEVEL = 16
    DEFAULT_ANGLE = pi / DEFAULT_NESTING_LEVEL

    def __init__(self, renderer, nesting_level=DEFAULT_NESTING_LEVEL, shift_angle=DEFAULT_ANGLE):
        self._renderer = renderer
        self._nesting_level = nesting_level
        self._shift_angle = shift_angle
        self._points = Square.prepare_points(*self._renderer.size)

    def draw(self):
        for i in range(self._nesting_level + 1):
            self._draw_shape()
            self._shift_points()

    def _draw_shape(self):
        for point_with_index in enumerate(self._points):
            shape_side = self._neighboring_points(point_with_index)
            self._draw_side(shape_side)

    def _neighboring_points(self, point_with_index):
        point_index, point = point_with_index
        return point + self._next_point(point_index)

    def _next_point(self, current_point_index):
        return self._points[(current_point_index + 1) % len(self._points)]

    def _draw_side(self, side):
        Line(self._renderer.sdl_renderer, side).draw()

    def _shift_points(self):
        self._points = list(map(self._shifted_point, enumerate(self._points)))

    def _shifted_point(self, point_with_index):
        x, y, next_x, next_y = self._neighboring_points(point_with_index)
        return self._shifted_coordinate(x, next_x), self._shifted_coordinate(y, next_y)

    def _shifted_coordinate(self, coordinate, next_coordinate):
        mu = self._clipping_factor()
        return (1 - mu) * coordinate + mu * next_coordinate

    def _clipping_factor(self):
        return tan(self._shift_angle) / (tan(self._shift_angle) + 1)

