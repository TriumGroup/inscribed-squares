import sdl2


class EventDispatcher:
    def __init__(self, event_loop, window):
        self.__window = window
        self.__event_loop = event_loop
        self.__event_dispatchers = {
            sdl2.SDL_WINDOWEVENT: self.__dispatch_window_event,
            sdl2.SDL_QUIT: self.__dispatch_quit_event
        }

    def dispatch(self, event):
        dispatcher = self.__event_dispatchers.get(event.type)
        if dispatcher is not None:
            dispatcher(event)

    def __dispatch_window_event(self, event):
        if event.window.event == sdl2.SDL_WINDOWEVENT_RESIZED:
            self.__window.resize()

    def __dispatch_quit_event(self, _):
        self.__event_loop.stop()
        self.__window.close()
