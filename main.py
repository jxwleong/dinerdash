import os
import subprocess
import logging
import time
import logger
import pyautogui
import pygetwindow as gw
# Pillow is needed/ pip install pillow
# Pip install opencv-python
import psutil

from adapter.process import Process
from adapter.window_handler import WindowHandler
import adapter.image_handler as Imageman

logger = logging.getLogger(__name__)
DINERDASH_EXEC_PATH = r'D:\Diner Dash\Diner Dash.exe'
dinerdash = Process(executable_path=DINERDASH_EXEC_PATH)
dinerdash_window = WindowHandler(title='Diner Dash')


def __launch_if_process_not_running(process):
    if process.is_running is False:
        process.launch()
    logger.info(f'{process.name} executed with PID: {process.pid}')
    

def __activate_window_if_not_active(window):
    if window.is_active is False:
        logger.info(f'{window.title} window is not active, activating now...')
        window.activate()
        logger.info(f'{window.title} window activated')
    else:
        logger.info(f'{window.title} window is active')


def start():
    __launch_if_process_not_running(dinerdash)
    __activate_window_if_not_active(dinerdash_window)


endless_shift = {
    'menu_button': r'img/endless_shift.png',
    'restaurant': r'img/restaurant_min.png',
    'easy' : r'img/endless_shift_easy.png',
    'medium': r'img/endless_shift_easy.png',
    'hard': r'img/endless_shift_hard.png',
    'lets_play': r'img/lets_play.png',   
}

def play_endless_shift(level):
    '''Expecting in Main Menu'''
    menu_button = endless_shift.get('menu_button')
    Imageman.locate_image_and_click(menu_button)    
    restaurant = endless_shift.get('restaurant')
    Imageman.locate_image_and_click(restaurant)       
    level_image = endless_shift.get(level.lower())
    Imageman.locate_image_and_click(level_image)
    lets_play = endless_shift.get('lets_play')
    Imageman.locate_image_and_click(lets_play)


start()
Imageman.wait_for_image(r'G:\My Projects\dinerdash\img\menu_chalkboard.png')
play_endless_shift(level='easy')
