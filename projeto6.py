#Automatizando Magic Piano Tiles
# quais são os passos manuais que devo transformar em código
import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

pyautogui.click(1472, 374, duration=1)

# Aqui no 'def' temos criado uma função de click
def click(x, y):
    win32api.SetCursorPos((x, y))  # Setou a posição do cursor, onde o mouse deve estar posicionado, também manda se movimentar
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0) # Aperta, pressionou o mouse
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0) # Soltou

# Enquanto usuário não apertar o número 1 no teclado, executa:
while keyboard.is_pressed('1') == False:
    
     # pixelMatchesColor = Função para verificar se dentro de uma determinada coordenada, uma determinada cor está presente  
    if pyautogui.pixelMatchesColor(1364, 310, (0, 0, 0)):
        click(1364, 310)
    if pyautogui.pixelMatchesColor(1435, 306, (0, 0, 0)):
        click(1435, 306)
    if pyautogui.pixelMatchesColor(1502, 298, (0, 0, 0)):
        click(1502, 298)
    if pyautogui.pixelMatchesColor(1568, 297, (0, 0, 0)):
        click(1568, 297)

