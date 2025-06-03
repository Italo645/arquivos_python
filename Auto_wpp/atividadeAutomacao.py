import os 
os.system ("cls")

import pyautogui 
import time


# pyautogui.press('win')
# time.sleep(2)
# pyautogui.write('chrome')
# time.sleep(2)
# pyautogui.press('enter')

#Mais de uma tecla em conjunto
# pyautogui.hotkey('alt', 'f4')

time.sleep(1)
pyautogui.press('win')
time.sleep(1)
pyautogui.write('crhome')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl','shift', 'n')
time.sleep(1)

pyautogui.write('gmail.com')
time.sleep(2)
pyautogui.press('enter')

time.sleep(3)
pyautogui.write('italoo765999@gmail.com')
time.sleep(4)
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(x=1192, y=658)
time.sleep(4)
pyautogui.click(x=1176, y=574)
123

