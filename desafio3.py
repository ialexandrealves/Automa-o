import  pyautogui
import webbrowser
from time import sleep

# Aprendendo a utilizar o scroll

webbrowser.open_new_tab('https://cursoautomacao.netlify.app/?_gl=1*1k1u3ct*_ga*NjU5MDA0ODMuMTcyMjE5MTY2OQ..*_ga_37GXT4VGQK*MTcyMjg5OTc4NC4yMi4xLjE3MjI5MDMwNTkuMC4wLjA.')
pyautogui.click(1075,302, duration=1.5)
sleep(2)
pyautogui.scroll(-1700)
pyautogui.click(829,407, duration=1.5)
pyautogui.typewrite('Arthur silva')
pyautogui.click(819,438, duration=1.5)
sleep(2)
pyautogui.click(1205,185, duration=1.5)
pyautogui.scroll(1700)
pyautogui.scroll(-3200)
pyautogui.click(889,125, duration=1.5)
sleep(2)
pyautogui.click(829,218, duration=1.5)
sleep(1)
pyautogui.click(829,218, duration=1.5)
 