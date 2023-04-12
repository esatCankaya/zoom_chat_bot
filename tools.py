# use these tools to set neccessary coordinates of your screen.

# Get the current coordinates of the mouse cursor
x, y = pyautogui.position()

print(f"The current coordinates are: ({x}, {y})")



## getting coordinates of an area to screenshot.

# set the number of times to display the position of the mouse cursor
num_outputs = 8

# display the position of the mouse cursor every once in two second.
for i in range(num_outputs):
    x, y = pyautogui.position()
    print(f'x: {x}, y: {y}')
    time.sleep(2)
    
    
## extracting meeting ID from meeting url

meeting_url = 'https://us05web.zoom.us/j/84528601435?pwd=b1oxMDJXZUluN1Vla3AzdHpLUG5sUT09'
meeting_id = re.search(r"\d{9,}", meeting_url).group()
meeting_id
