### 2 ### this code takes meeting ID and opens meeting with zoom app ###

# you have to import pyautogui, pytesseract, time, os, re libraries before running the code. 
# I am using Jupiter Notebook, change importing ways according to your source-code editor.

import pyautogui
import pytesseract
import os
import time

# you can change the start time for the code to start now or later.

# Set the start time to 9:00 AM
#start_time = time.strptime("09:00:00", "%H:%M:%S")

# Get the start time
start_time = time.time()

# define a meeting ID and Password to enter the meeting
meeting_id = '84528601435'
password = 'L657qa'

# opens zoom with a given path.
zoom_path = '/Applications/zoom.us.app'
os.system(f'open {zoom_path}')

# Wait for the Zoom application to open
time.sleep(10)

# Click the "Join Meeting" button.(find the button place in your screen with functions above)
pyautogui.click(x=570, y=547)
time.sleep(2)

# typing the meeting ID and enter.
pyautogui.typewrite(meeting_id)
pyautogui.press('enter')
time.sleep(4)

# entering the password
pyautogui.typewrite(password)
pyautogui.press('enter')
time.sleep(15)

# Click the "chat" button.(find the button place in your screen with functions above)
pyautogui.click(x=496, y=847)
time.sleep(1)

# Define the region (chat box) to capture (enter coordinates of top_left and botton_right corners)
x1, y1, x2, y2 = 1228, 55, 1589, 729

burda_count = 0
burdaCount = 0

print('Starting loop...')

# Loop until at least 2 hours have elapsed
while time.time() - start_time < 7200:

    # Take a screenshot of the region
    screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))

    # Convert the screenshot to a string using OCR
    text = pytesseract.image_to_string(screenshot)

    # Check if the string "..." is present in the screenshot
     if burdaCount + burda_count >= 3:
        # If the word is found, perform some tasks with pyautogui
        pyautogui.moveTo(836, 32)
        pyautogui.click()
        pyautogui.typewrite('burdayim')
        pyautogui.press('enter')
        break

    # Wait for 1 minute before taking the next screenshot
    time.sleep(60)
    
print('Loop finished.')
