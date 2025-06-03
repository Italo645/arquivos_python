import os 
os.system ("cls")

import pyautogui 
import time


def espera(segundos=2):
    time.sleep(segundos)


def clique(x, y, delay=2):
    espera(delay)
    pyautogui.click(x = x, y = y)


def clique_duplo(x, y, delay=2):
      espera(delay)
      pyautogui.doubleClick(x = x, y = y)


def abrir_site(nome_site, delay=2):
     espera(delay)
     pyautogui.write(nome_site)
     espera(delay)
     pyautogui.press('enter')     
     espera(1)


def email(nome_email, delay=2):
     espera(delay)
     pyautogui.write(nome_email)
     espera(delay)
     pyautogui.press('enter')     
     espera(1)


def escrever(nome_escrever, delay=2):
     espera(delay)
     pyautogui.write(nome_escrever)
     espera(delay)
     pyautogui.press('enter')     
     espera(1)

def mais_teclas(tecla1='a', tecla2='b', tecla3='c'):
     espera()
     pyautogui.hotkey(tecla1, tecla2, tecla3)

# minimizar (x=1800, y=17)
# crhome(x=43, y=217)

# Verificar cursos do Senac em taquaralto

# clique(1800, 17)
# clique_duplo(43, 217)
# abrir_site('to.senac.br')
# clique(553, 707)
# clique(495, 879)
# clique(1377, 715)


#pegar arquivo
clique(1800, 17)
mais_teclas('win','e')
clique(105, 346)
clique_duplo(244, 455)
clique(315, 459)
mais_teclas('ctrl','c')
clique(1800, 17)
    

#email
clique(1800, 17)
clique_duplo(43, 217)
espera()
mais_teclas('ctrl', 'shift', 'n')
abrir_site('gmail.com')
espera(5)
email('italoo765999@gmail.com')
espera(30)
clique(34, 199)
escrever('mateusgn@to.senac.br')
clique(1463, 681)
mais_teclas('ctrl', 'v')
clique(1306, 995)
clique(1034, 185)

# "C:\Users\DBA_ITALO\Documents\python_prof_matheus\automacao3.py"
