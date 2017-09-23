import sdl2
import ctypes

from event_dispatcher import EventDispatcher


class EventLoop:
    def __init__(self, window):
        self.__event_dispatcher = EventDispatcher(self, window)
        self.__running = False

    def run(self):
        self.__running = True
        while self.__running:
            self.__receive_events()

    def stop(self):
        self.__running = False

    def __receive_events(self):
        event = sdl2.SDL_Event()
        event_pointer = ctypes.byref(event)
        while self.__running and sdl2.SDL_PollEvent(event_pointer) != 0:
            self.__event_dispatcher.dispatch(event)

