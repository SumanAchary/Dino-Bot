from datetime import time  # Import the 'time' module from the 'datetime' package (not used in the code).
import pyautogui  # Import the 'pyautogui' library for automating mouse and keyboard inputs.
from PIL import ImageGrab, ImageOps  # Import modules from the 'PIL' (Pillow) library for image processing.
import time  # Import the 'time' module for adding delays.
from numpy import *  # Import the 'numpy' library for numerical operations.

# Define a class 'Cordinates' to store coordinates as class attributes.
class Cordinates():
    replayBtn = (480, 577)  # Coordinates of the replay button on the screen.
    dinasaur = (246, 540)  # Coordinates of the dinosaur object.

# Function to restart the game by clicking the replay button.
def restartGame():
    pyautogui.click(Cordinates.replayBtn)

# Function to simulate pressing the spacebar.
def pressSpace():
    pyautogui.keyDown('space')  # Press the spacebar key.
    time.sleep(0.05)  # Sleep for a short duration.
    print("Object detected: Jump")
    pyautogui.keyUp('space')  # Release the spacebar key.

# Function to capture and process a portion of the screen.
def imageGrab():
    # Define a box (region of interest) around the dinosaur object.
    box = (
        Cordinates.dinasaur[0] + 34, Cordinates.dinasaur[1],
        Cordinates.dinasaur[0] + 190, Cordinates.dinasaur[1] + 30)
    # Capture the image within the defined box.
    image = ImageGrab.grab(box)
    # Convert the image to grayscale.
    grayImage = ImageOps.grayscale(image)
    # Convert the grayscale image to a numpy array.
    a = array(grayImage.getcolors())
    print('****')
    # Sum all pixel values in the grayscale image.
    imageGrab = a.sum()
    return imageGrab

# Function to continuously perform actions while an object is detected.
def jumpWhileObject():
    restartGame()  # Restart the game.
    while True:  # Infinite loop.
        # If the sum of pixel values in the captured image is not equal to 4927 (some detection condition),
        if imageGrab() != 4927:
            print('image grab = ' + str(imageGrab()))
            pressSpace()  # Perform a jump action.
            time.sleep(0.01)  # Sleep briefly to control the loop speed.

# Call the 'jumpWhileObject()' function to start the automation.
jumpWhileObject()
