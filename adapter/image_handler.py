import os
import logging

import pyautogui

logger = logging.getLogger(__name__)


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

def get_image_coordinate(path):
    try:
        image_location = pyautogui.locateOnScreen(path)
    except:
        logger.error("Image not found!")
    else:
        return pyautogui.center(image_location)    