import pygetwindow as gw

class WindowHandler:
    def __init__(self, title):
        self.title = title

    @property
    def window(self):
        while True:
            try:
                return gw.getWindowsWithTitle(self.title)[0]
            except IndexError:
                continue

    @property
    def is_active(self):
        return self.window.isActive

    def activate(self):
        self.window.activate()