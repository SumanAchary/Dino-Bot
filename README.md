# How to Run the Dinosaur Game Automation Script

This guide will help you run a Python script that automates the dinosaur game. The script uses the `pyautogui`, `PIL`, and `numpy` libraries to detect objects in the game and make the dinosaur jump.

## Prerequisites

Before you can run the script, you need to have Python installed on your computer. You also need to install the following Python libraries:

- `pyautogui`
- `PIL`
- `numpy`

You can install these libraries using pip:

```bash
pip install pyautogui pillow numpy
```

## Running the Script

1. **Save the script**: Copy the Python script and save it as a `.py` file on your computer.

2. **Open the game**: Open the dinosaur game in your web browser. You can access it by turning off your internet and trying to load a page in Google Chrome, or by going directly to `chrome://dino` in your Chrome address bar.

3. **Run the script**: Navigate to the directory where you saved the `.py` file in your terminal or command prompt, and run the script using Python:

```bash
python filename.py
```

Replace `filename.py` with the name of your Python file.

4. **Start playing**: As soon as you run the script, it will automatically start playing the game. The dinosaur will jump whenever it detects an object in its path.

## Notes

- The script is set up for a specific screen resolution. If your screen resolution is different, you might need to adjust the coordinates in the `Cordinates` class.
- The object detection is based on pixel values. If the game's appearance changes (due to browser updates, different browsers, or extensions/themes), you might need to adjust the detection condition in the `imageGrab()` function.
- Make sure not to move your mouse after running the script, as it might interfere with the automated mouse movements.

Enjoy watching your dinosaur conquer new heights! 😊
