# Zerar Game Guitar Flash com PyAutoGUI

import pyautogui
import keyboard
from time import sleep

# Conhecendo o pixelMatchesColor

while keyboard.is_pressed('1') == False:

    #pixelMatchesColor - Verifica se dentro de uma determinada coordenada, uma determinada cor está presente
    if pyautogui.pixelMatchesColor(1291, 760, (12, 152, 33)):
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1378, 761, (254, 15, 23)):
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1468, 761, (244, 244, 64)):
        pyautogui.press('a')
        sleep(0.05)


