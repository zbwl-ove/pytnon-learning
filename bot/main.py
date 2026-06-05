

import pyautogui
import time 
#a code to get the mouse position and print it to the console
while True:
    x, y = pyautogui.position()
    print(f"Mouse position: ({x}, {y})")
    time.sleep(2) #wait for 1 second before getting the mouse position again
    