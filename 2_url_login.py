### 2 ### this code takes meeting url and opens meeting with web browser ###

# you have to import pyautogui, pytesseract, time, os, re libraries before running the code. 
# I am using Jupiter Notebook, change importing ways according to your source-code editor.

import pyautogui
import pytesseract
import webbrowser
import re
import time

# you can change the start time for the code to start now or later.

# set the start time to 9:00 AM
# start_time = time.strptime("09:00:00", "%H:%M:%S")

# Get the start time
start_time = time.time()

## open zoom with url and extract meeting ID
meeting_url = 'https://us05web.zoom.us/j/86261882770?pwd=Z1FlemQxb3g1a204czZOaVJIS0hJZz09'
meeting_id = re.search(r"\d{9,}", meeting_url).group()

# Open the meeting URL in a web browser
webbrowser.open(meeting_url)
time.sleep(5)

# Click the "Launch Meeting" button. (find the button place in your screen with functions above)
pyautogui.click(x=836, y=514)
time.sleep(5)

# Click the "allow" button.(find the button place in your screen with functions above)
pyautogui.click(x=1020, y=552)
time.sleep(30)

# Click the "chat" button.(find the button place in your screen with functions above)
pyautogui.click(x=496, y=847)

# Define the region (chat box) to capture (enter coordinates of top_left and botton_right corners)
x1, y1, x2, y2 = 1228, 55, 1589, 729

# once you set right coordinates, set a time for loop to work and set set how often you want it to run.

burda_count = 0
Burda_count = 0

print('Starting loop...')

# Loop until at least 2 hours have elapsed
while time.time() - start_time < 7200:

    # Take a screenshot of the region
    screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))

    # Convert the screenshot to a string using OCR
    text = pytesseract.image_to_string(screenshot)
    burda_count = text.count('burda')
    
    # Check if the string "..." is present in the screenshot
    if bburdaCount + burda_count >= 3:
        # If the word is found, perform some tasks with pyautogui
        pyautogui.moveTo(836, 32)
        pyautogui.click()
        pyautogui.typewrite('buradayım')
        pyautogui.press('enter')
        break

    # Wait for 31 seconds before taking the next screenshot
    time.sleep(31)
    
print('Loop finished.')
