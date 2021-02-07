import os
import subprocess
import logging
import time
import logger
import pyautogui 
import pygetwindow as gw
# Pillow is needed/ pip install pillow

DINERDASH_EXEC_PATH = r'D:\Diner Dash\Diner Dash.exe'
logger = logging.getLogger(__name__)
logger.info('Opening Dinerdash...')
subprocess.Popen(DINERDASH_EXEC_PATH)
logger.info('Waiting 10seconds for mainmenu...')
time.sleep(10)
logger.info('Locating Diner Dash window...')
dinerdash_window = gw.getWindowsWithTitle('Diner Dash')[0]
logger.info('Is Diner Dash window active: ' + str(dinerdash_window.isActive))
#dinerdash_window.activate()

def locate_image_and_click(image_path):
    pyautogui.moveTo(pyautogui.locateCenterOnScreen(image_path))
    pyautogui.leftClick()

def iterate_image_click(image_path, iterate, delay=1):
    for _ in range (iterate):
        locate_image_and_click(image_path)
        pyautogui.leftClick()
        time.sleep(delay)

def write_and_enter(words):
    pyautogui.write(words)
    pyautogui.press('enter')

# time.sleep(1)
# locate_image_and_click(r'G:\My Projects\dinerdash\img\flos_career.png')
# time.sleep(1)
# locate_image_and_click(r'G:\My Projects\dinerdash\img\new_player.png')
# #write_and_enter('Hello world!')  
# time.sleep(1)
# #locate_image_and_click(r'G:\My Projects\dinerdash\img\select_profile_play.png')

# locate_image_and_click(r'G:\My Projects\dinerdash\img\new_game.png')
# time.sleep(1)

# iterate_image_click(image_path=r'G:\My Projects\dinerdash\img\right_arrow.png',
#                     iterate=3)

locate_image_and_click(r'G:\My Projects\dinerdash\img\2_red_ppl.png')