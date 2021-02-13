import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
#import process
print(sys.path)

from process import Process

dinerdash = Process(process_exec=r'D:\Diner Dash\Diner Dash.exe')
print(dinerdash.is_running)
dinerdash.launch