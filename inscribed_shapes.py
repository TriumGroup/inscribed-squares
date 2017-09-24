import sdl2

from math import trunc, tan, pi


class InscribedShapes:
    PADDING = 20
    INSCRIBED_SHAPES_COUNT = 16
    DEFAULT_ANGLE = pi / INSCRIBED_SHAPES_COUNT

    def __init__(self, renderer, shift_angle=DEFAULT_ANGLE):
        self.__renderer = renderer
        self.__shift_angle = shift_angle
        self.__points = self.__prepare_points_for_square(self.__renderer.size)

    def draw(self):
        self.__draw_shape()
        for i in range(self.INSCRIBED_SHAPES_COUNT):
            self.__points = list(map(self.__shift_points, enumerate(self.__points)))
            self.__draw_shape()

    def __shift_points(self, iterable):
        index, point = iterable
        return self.__shift_point(point, self.__next_point(index))

    def __next_point(self, current_point_index):
        return self.__points[(current_point_index + 1) % len(self.__points)]

    def __shift_point(self, base_point, next_point):
        base_x, base_y = base_point
        next_x, next_y = next_point
        return self.__shift_coordinate(base_x, next_x), self.__shift_coordinate(base_y, next_y)

    def __shift_coordinate(self, base_coordinate, next_coordinate):
        return (1 - self.__clipping_factor()) * base_coordinate + self.__clipping_factor() * next_coordinate

    def __clipping_factor(self):
        return tan(self.__shift_angle) / (tan(self.__shift_angle) + 1)

    def __draw_shape(self):
        points_length = len(self.__points)
        for i, point in enumerate(self.__points):
            next_point = self.__points[(i + 1) % points_length]
            self.__connect_points(point, next_point)

    def __connect_points(self, start_point, end_point):
        start_point_x, start_point_y = start_point
        end_point_x, end_point_y = end_point
        sdl2.SDL_RenderDrawLine(
            self.__renderer.sdl_renderer,
            trunc(start_point_x),
            trunc(start_point_y),
            trunc(end_point_x),
            trunc(end_point_y)
        )

    def __draw_point(self, point):
        x, y = point
        sdl2.SDL_RenderDrawPoint(self.__renderer.sdl_renderer, x, y)

    def __prepare_points_for_square(self, renderer_size):
        width, height = renderer_size
        return [
            (self.PADDING, self.PADDING),
            (width - self.PADDING, self.PADDING),
            (width - self.PADDING, height - self.PADDING),
            (self.PADDING, height - self.PADDING)
        ]
