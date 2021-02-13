import os
import sys
import time

from process import Process
from window_handler import WindowHandler


dinerdash = Process(process_exec=r'D:\Diner Dash\Diner Dash.exe')
print(dinerdash.is_running)
dinerdash.launch()

dd_window = WindowHandler(window_name='Diner Dash')
print(dd_window.window)
print(dd_window.is_active)

time.sleep(10)
if dd_window.is_active is False:
    dd_window.activate()