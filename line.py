import sdl2

from math import trunc
import numpy as np


# Attention! Optimized code below! Take care of your eyes.
class Line:
    def __init__(self, sdl_renderer, line_coordinates):
        self._sdl_renderer = sdl_renderer
        self._x1, self._y1, x2, y2 = tuple(map(trunc, line_coordinates))
        self._delta_x = abs(x2 - self._x1)
        self._delta_y = abs(y2 - self._y1)
        self._step_x = 1 if x2 >= self._x1 else -1
        self._step_y = 1 if y2 >= self._y1 else -1
        self._d2 = -abs(self._delta_x - self._delta_y) * 2

    def draw(self):
        if self._delta_x >= self._delta_y:
            self._draw_by_continuous_x_increase(self._x1, self._y1)
        else:
            self._draw_by_continuous_y_increase(self._x1, self._y1)

    def _draw_by_continuous_x_increase(self, x, y):
        d1 = self._delta_y * 2
        d = d1 - self._delta_x
        for i in range(self._delta_x):
            self._draw_point(x, y)
            x += self._step_x
            if d > 0:
                d += self._d2
                y += self._step_y
            else:
                d += d1

    def _draw_by_continuous_y_increase(self, x, y):
        d1 = self._delta_x * 2
        d = d1 - self._delta_y
        for i in range(self._delta_y):
            self._draw_point(x, y)
            y += self._step_y
            if d > 0:
                d += self._d2
                x += self._step_x
            else:
                d += d1

    def _draw_point(self, x, y):
        sdl2.SDL_RenderDrawPoint(self._sdl_renderer, x, y)
        vector = np.array([x, y, 1])
        x, y, _ = vector.dot(self._matrix()).dot(self._matrix_scale())
        sdl2.SDL_RenderDrawPoint(self._sdl_renderer, trunc(x), trunc(y))


    def _matrix(self):
        return np.array([
            [1, 0, 0],
            [0, 1, 0],
            [900, 200, 1],
        ])

    def _matrix_scale(self):
        return np.array([
            [0.5, 0, 0],
            [0, 0.5, 0],
            [0, 0, 0],
        ])


