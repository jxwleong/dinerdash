import os
import sys
import time

from adapter.process import Process
from adapter.window_handler import WindowHandler


dinerdash = Process(executable_path=r'D:\Diner Dash\Diner Dash.exe')
if dinerdash.is_running is False:
    dinerdash.launch()
print(dinerdash.pid)
dd_window = WindowHandler(title='Diner Dash')
print(dd_window.window)
print(dd_window.is_active)

time.sleep(10)
if dd_window.is_active is False:
    dd_window.activate()