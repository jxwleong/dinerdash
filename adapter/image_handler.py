import os
import logging
import time

import pyautogui

logger = logging.getLogger(__name__)


def is_image_on_screen(image, confidence=0.5):
    if pyautogui.locateOnScreen(image, confidence) is None:
        return False
    return True

def locate_image_and_click(image, confidence=0.5):
    while is_image_on_screen(image, confidence) is False:
        logger.info(f'Locating {os.path.basename(image)} ...')
       # time.sleep(1)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen(image))
    logger.info(f'{os.path.basename(image)} found!')
    pyautogui.leftClick()

def get_image_coordinate(image):
    try:
        image_location = pyautogui.locateOnScreen(image)
    except:
        logger.error("Image not found!")
    else:
        return pyautogui.center(image_location)    

def wait_for_image(image, confidence=0.5, delay=1):
    while is_image_on_screen(image, confidence) is False:
        logger.info(f'Waiting for {os.path.basename(image)}...' )    
        time.sleep(delay)
    logger.info(f'{os.path.basename(image)} found!')
