import pyautogui
import time

screenWidth, screenHeight = pyautogui.size() #Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position() # Mouse coordinates

# pyautogui.moveTo(1850, 690) # Move to Games Folder... moving to wrong spot??
# time.sleep(1)
# pyautogui.doubleClick()
time.sleep(1)
pyautogui.typewrite(['g', 'enter'])
time.sleep(5)
pyautogui.typewrite(['s', 's', 's', 'enter']) # Select Starcraft, Press enter
time.sleep(40)
# pyautogui.click('play-button.png') Try this later, click pos for now
pyautogui.moveTo(920, 930)
pyautogui.click()

