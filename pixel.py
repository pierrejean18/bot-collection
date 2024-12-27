import time
import pyautogui

time.sleep(5)

coords = pyautogui.position()

print(coords, '=', pyautogui.pixel(coords.x,coords.y))