import sys

from window import Window
from event_loop import EventLoop


def main():
    window_with_plot = Window(b"Lab 2")
    EventLoop(window_with_plot).run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
