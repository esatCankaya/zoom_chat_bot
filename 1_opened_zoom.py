### 1 ### if you already open zoom and zoom chat yourself, run this code

# you have to import pyautogui, pytesseract, time, os, re libraries before running the code. 
# I am using Jupiter Notebook, change importing ways according to your source-code editor.
import pyautogui
import pytesseract
import time
import os
import re

# you can change the start time for the code to start now or later.

# Set the start time to 9:00 AM
#start_time = time.strptime("09:00:00", "%H:%M:%S")

# Get the start time
start_time = time.time()

# Define the region to capture (enter coordinates of top_left and botton_right corners)
x1, y1, x2, y2 = 1228, 55, 1589, 729

# define words to look for
burda_count = 0
burdaCount = 0

print('Starting loop...')

# Loop until at least 2 hours have elapsed.(adjust according to meeting time)
while time.time() - start_time < 7200:

    # Take a screenshot of the region(chatbox)
    screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))

    # Convert the screenshot to a string using OCR
    text = pytesseract.image_to_string(screenshot)
    burda_count = text.count('burda')
    burdaCount = text.count('Burda')
    
    # Check if the string "..." is present in the screenshot
    if burdaCount + burda_count >= 3:
        # If the word is found, perform some tasks with pyautogui
        pyautogui.moveTo(836, 32)
        pyautogui.click()
        pyautogui.typewrite('burdayim')
        pyautogui.press('enter')
        break
    
    # Wait for 31 seconds before taking the next screenshot
    time.sleep(31)
    
print('Loop finished.')

