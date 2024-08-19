import pyautogui
import webbrowser
from time import sleep

'''
 Projeto Desafio - Entrar no Instagram, pesquisar a conta da Seleção Brasileira, 
 depois curtir e comentar a última foto, e em seguida apresentar uma janela com 
 'Parabéns, Automação concluída !'
'''

webbrowser.open_new('https://www.instagram.com/')
sleep(3)

imagem = pyautogui.locateOnScreen('pesquisarig.png')
pyautogui.click(imagem[0], imagem[1], duration = 2)

sleep(2)

pyautogui.typewrite('cbf_futebol')
pyautogui.click(1033,194, duration=2)

sleep(2)

pyautogui.scroll(-350)

imagem2 = pyautogui.locateCenterOnScreen('foto_ig_cbf.png')
pyautogui.click(imagem2[0], imagem2[1], duration = 2)

sleep(2)

imagem3 = pyautogui.locateCenterOnScreen('like.png')
pyautogui.click(imagem3[0], imagem3[1], duration = 1)

sleep(1)

imagem4 = pyautogui.locateCenterOnScreen('coment.png')
pyautogui.click(imagem4[0], imagem4[1], duration = 1)

sleep(1)

imagem5 = pyautogui.locateCenterOnScreen('add_coment.png')
pyautogui.click(imagem5[0], imagem5[1], duration = 1)

pyautogui.typewrite('Brasil!')
pyautogui.press('enter')

pyautogui.alert(text = 'Parabéns, Automação concluída !', title = 'Atenção', button= 'Ok')
