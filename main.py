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


# endless_shift_level = {
#     'easy' : r'img/endless_shift_easy.png',
#     'medium': r'img/endless_shift_easy.png',
#     'hard': r'img/endless_shift_hard.png',    
# }
# def play_endless_shift(level):
# '''Expecting in Main Menu'''


def waiting_for_main_menu(image):
    while is_image_on_screen(image, confidence=0.5) is False:
        logger.info("Waiting for main menu...")
        time.sleep(5)
    logger.info("Main menu found!")


def is_image_on_screen(image, confidence=0.5):
    if pyautogui.locateOnScreen(image, confidence) is None:
        return False
    return True


def locate_image_and_click(image, confidence=0.5, iter=5):
    while is_image_on_screen(image, confidence) is False:
        logger.info('Locating ' + os.path.basename(image) + '...')
       # time.sleep(1)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen(image))
    logger.info(os.path.basename(image) + ' found!')
    pyautogui.leftClick()


def iterate_image_click(image, iterate, delay=1):
    for _ in range (iterate):
        locate_image_and_click(image)
        pyautogui.leftClick()
        time.sleep(delay)


def write_and_enter(words):
    pyautogui.write(words)
    pyautogui.press('enter')



start()


# waiting_for_main_menu(r'G:\My Projects\dinerdash\img\menu_chalkboard.png')
# print(get_image_coordinate(r'G:\My Projects\dinerdash\img\menu_chalkboard.png'))
# locate_image_and_click(r'G:\My Projects\dinerdash\img\endless_shift.png')
# time.sleep(1)
# locate_image_and_click(r'G:\My Projects\dinerdash\img\restaurant_min.png')
# time.sleep(1)
# locate_image_and_click(r'G:\My Projects\dinerdash\img\endless_shift_easy.png')
# locate_image_and_click(r'G:\My Projects\dinerdash\img\lets_play.png', confidence=0.8)
# locate_image_and_click(r'G:\My Projects\dinerdash\img\flos_career.png')
# time.sleep(1)
# locate_image_and_click(r'G:\My Projects\dinerdash\img\new_player.png')
# #write_and_enter('Hello world!')  
# time.sleep(1)
# #locate_image_and_click(r'G:\My Projects\dinerdash\img\select_profile_play.png')

# locate_image_and_click(r'G:\My Projects\dinerdash\img\new_game.png')
# time.sleep(1)

# iterate_image_click(image=r'G:\My Projects\dinerdash\img\right_arrow.png',
#                     iterate=3)

#locate_image_and_click(r'G:\My Projects\dinerdash\img\2_red_ppl.png')