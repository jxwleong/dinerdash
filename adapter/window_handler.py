import pygetwindow as gw

class WindowHandler:
    def __init__(self, window_name):
        self.window_name = window_name

    @property
    def window(self):
        while True:
            try:
                return gw.getWindowsWithTitle(self.window_name)[0]
            except IndexError:
                continue

    @property
    def is_active(self):
        return self.window.isActive

    def activate(self):
        self.window.activate()