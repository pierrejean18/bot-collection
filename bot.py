import time
import pyautogui

pyautogui.PAUSE = 0

time.sleep(8)

cookie = (970, 394)

couleurame = (238,238,238)

x = 1910
upgradey = [746 ,654, 555, 467, 379, 301, 231, 160 ]

while True:
    for i in range(100):
        pyautogui.click(cookie[0], cookie[1])

    for y in upgradey:
        if pyautogui.pixel(x, y) == couleurame:
            pyautogui.click(x, y)




