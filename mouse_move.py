# first download required packages
# apt install python3-pip git -y
# pip3 install --upgrade pip
# sudo apt-get install python3-tk python3-dev -y
# pip3 install pyautogui

import pyautogui
import time

while True:
    # Move the mouse cursor to a random position
    pyautogui.moveTo(x=100, y=100, duration=0.25)

    # Wait for 30 seconds
    time.sleep(30)

    
  
