# Grab base from https://github.com/AmirrezaM21/OverwatchAutoLogin

import cv2
import pyautogui as pag
import numpy as np

def readImage(path : str):
    return cv2.imread(path)

def locateOnScreen(image):
    screen = getScreen()
    compression = 0.5
    screen, image = compress(screen, image, compression)
    threshold = 0.70
    loc = findImage(screen, image, threshold)  
    return not isEmpty(loc)

def getScreen():
    screen = None
    try:
        screen = pag.screenshot()
    except:
        print("Can't get screenshot!")
    screen = pilToNumpy(screen)
    return screen

def compress(screen, sample, rate):
    return resize(screen, rate), resize(sample, rate)

def findImage(screen, image, threshold):
    res = cv2.matchTemplate(screen, image, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    return loc

def isEmpty(array):
    return not list(array[0])

def pilToNumpy(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

def resize(img, scale):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized