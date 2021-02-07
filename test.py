import os
import subprocess
import logging
import time
import logger
import pyautogui 
import pygetwindow as gw
# Pillow is needed/ pip install pillow
import psutil

logger = logging.getLogger(__name__)
DINERDASH_EXEC_PATH = r'D:\Diner Dash\Diner Dash.exe'


def is_process_running(process_name):
    # source: https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


def launch_dinerdash(process_name, exec_path):
    if not is_process_running(process_name):
        logger.info('Opening Dinerdash...')
        _proc = subprocess.Popen(exec_path)
        logger.info('App Executed with PID: ' + str(_proc.pid))
        logger.info('Waiting 10seconds for mainmenu...')
        time.sleep(10)

    else:
        logger.info('Dinerdash is already running...')

launch_dinerdash(process_name='Diner Dash.exe', exec_path=DINERDASH_EXEC_PATH)

def active_window_if_not_active(window):
    if not window.isActive:
        logger.info(str(window.title) + 'is not active, activating now...')
        window.activate()
        logger.info(str(window.title) + 'activated')
    else:
        logger.info(str(window.title) + 'is active')


logger.info('Locating Diner Dash window...')
dinerdash_window = gw.getWindowsWithTitle('Diner Dash')[0]
active_window_if_not_active(dinerdash_window)

#dinerdash_window.activate()




def locate_image_and_click(image_path):
    logger.info('Locating ' + os.path.basename(image_path) + '...')
    pyautogui.moveTo(pyautogui.locateCenterOnScreen(image_path))
    logger.info('Select ' + os.path.basename(image_path) + '..')    
    pyautogui.leftClick()

def iterate_image_click(image_path, iterate, delay=1):
    for _ in range (iterate):
        locate_image_and_click(image_path)
        pyautogui.leftClick()
        time.sleep(delay)

def write_and_enter(words):
    pyautogui.write(words)
    pyautogui.press('enter')

time.sleep(1)
locate_image_and_click(r'G:\My Projects\dinerdash\img\endless_shift.png')
time.sleep(1)
locate_image_and_click(r'G:\My Projects\dinerdash\img\restaurant.png')
time.sleep(1)
locate_image_and_click(r'G:\My Projects\dinerdash\img\endless_shift_easy.png')
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

#locate_image_and_click(r'G:\My Projects\dinerdash\img\2_red_ppl.png')