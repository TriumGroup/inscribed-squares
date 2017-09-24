import sdl2

from math import trunc, tan, pi


class InscribedShapes:
    PADDING = 20
    INSCRIBED_SQUARES_COUNT = 32
    DEFAULT_ANGLE = (pi / 2) / (INSCRIBED_SQUARES_COUNT - 1)

    def __init__(self, renderer, shift_angle=DEFAULT_ANGLE):
        self.__renderer = renderer
        self.__shift_angle = shift_angle

    def draw_squares(self):
        width, height = self.__renderer.size
        points = [
            (self.PADDING, self.PADDING),
            (width - self.PADDING, self.PADDING),
            (width - self.PADDING, height - self.PADDING),
            (self.PADDING, height - self.PADDING)
        ]
        self.__draw_shape(points)
        for i in range(self.INSCRIBED_SQUARES_COUNT):
            self.__shift_points(points)
            self.__draw_shape(points)

    def __shift_points(self, points):
        points_length = len(points)
        for i in range(points_length):
            next_point = points[(i + 1) % points_length]
            points[i] = self.__shift_point(points[i], next_point)

    def __shift_point(self, base_point, next_point):
        base_x, base_y = base_point
        next_x, next_y = next_point
        return self.__shift_coordinate(base_x, next_x), self.__shift_coordinate(base_y, next_y)

    def __shift_coordinate(self, base_coordinate, next_coordinate):
        return (1 - self.__clipping_factor()) * base_coordinate + self.__clipping_factor() * next_coordinate

    def __clipping_factor(self):
        return tan(self.__shift_angle) / (tan(self.__shift_angle) + 1)

    def __draw_shape(self, points):
        points_length = len(points)
        for i, point in enumerate(points):
            next_point = points[(i + 1) % points_length]
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
