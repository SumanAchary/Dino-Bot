from datetime import time
import pyautogui
from PIL import ImageGrab, ImageOps
import time
from numpy import *

class Cordinates():
    replayBtn = (480, 577) # Coordinates of the replay button on the screen
    dinasaur = (246, 540) # Coordinates of the dinosaur Object

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Object detected : Jump")
    pyautogui.keyUp('space')
    # (280,617) Coordinates of the tree  (varies for different computers)
    # in case of any issues contact : suman.achary95@gmail.com

def imageGrab():
    box = (
        Cordinates.dinasaur[0] + 34, Cordinates.dinasaur[1], Cordinates.dinasaur[0] + 190, Cordinates.dinasaur[1] + 30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print('****')
    imageGrab = a.sum()
    return imageGrab

def jumpWhileObject():
    restartGame()
    while True:
        if imageGrab() != 4927:
            print('image grab = ' + str(imageGrab()))
            pressSpace()
            time.sleep(0.01)

jumpWhileObject()
