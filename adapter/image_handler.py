import os
import sys
import logging
import time

import pyautogui
ROOT_DIR = os.path.abspath(os.curdir)
sys.path.insert(0, ROOT_DIR)

from common import get_refined_image_name

logger = logging.getLogger(__name__)


def is_image_on_screen(image, confidence=0.5):
    if pyautogui.locateOnScreen(image, confidence) is None:
        return False
    return True

def locate_image_and_click(image, confidence=0.5):
    image_name = os.path.basename(image)
    while is_image_on_screen(image, confidence) is False:
        logger.info(f'Locating {get_refined_image_name(image_name)} ...')
       # time.sleep(1)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen(image))
    logger.info(f'{get_refined_image_name(image_name)} found!')
    pyautogui.leftClick()

def get_image_coordinate(image):
    try:
        image_location = pyautogui.locateOnScreen(image)
    except:
        logger.error("Image not found!")
    else:
        return pyautogui.center(image_location)    

def wait_for_image(image, confidence=0.5, delay=1):
    image_name = os.path.basename(image)
    while is_image_on_screen(image, confidence) is False:
        logger.info(f'Waiting for {get_refined_image_name(image_name)}...' )    
        time.sleep(delay)
    logger.info(f'{get_refined_image_name(image_name)} found!')
