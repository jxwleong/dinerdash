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
        logger.info('Executing Dinerdash...')
        proc = subprocess.Popen(exec_path)
        logger.info('App executed with PID: ' + str(proc.pid))

    else:
        logger.info('Dinerdash is already running...')


def active_window_if_not_active(window):
    if not window.isActive:
        logger.info(str(window.title) + ' is not active, activating now...')
        window.activate()
        logger.info(str(window.title) + ' activated')
    else:
        logger.info(str(window.title) + ' is active')


def get_dinerdash_window(window_name):
    while True:
        try:
            return gw.getWindowsWithTitle(window_name)[0]
        except IndexError:
            continue
        
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

def get_image_coordinate(path):
    try:
        image_location = pyautogui.locateOnScreen(path)
    except:
        logger.error("Image not found!")
    else:
        return pyautogui.center(image_location)

launch_dinerdash(process_name='Diner Dash.exe', exec_path=DINERDASH_EXEC_PATH)
logger.info('Locating Diner Dash window...')
dinerdash_window = get_dinerdash_window('Diner Dash') 
active_window_if_not_active(dinerdash_window)
waiting_for_main_menu(r'G:\My Projects\dinerdash\img\menu_chalkboard.png')
print(get_image_coordinate(r'G:\My Projects\dinerdash\img\menu_chalkboard.png'))
locate_image_and_click(r'G:\My Projects\dinerdash\img\endless_shift.png')
time.sleep(1)
locate_image_and_click(r'G:\My Projects\dinerdash\img\restaurant_min.png')
time.sleep(1)
locate_image_and_click(r'G:\My Projects\dinerdash\img\endless_shift_easy.png')
locate_image_and_click(r'G:\My Projects\dinerdash\img\lets_play.png', confidence=0.8)
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