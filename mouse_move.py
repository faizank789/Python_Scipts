import pyautogui
import time

while True:
    # Move the mouse cursor to a random position
    pyautogui.moveTo(x=100, y=100, duration=0.25)

    # Wait for 30 seconds
    time.sleep(30)
