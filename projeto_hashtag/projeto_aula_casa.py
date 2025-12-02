import pyautogui as pg
import pyperclip as pclip
import pandas as pd
import time
pg.PAUSE = 0.5
link_drive = "https://drive.google.com/drive/folders/1X4qQW6ODmQlWei1Ei_YZiS_vuFyH96F8"
email_link = r"https://mail.google.com/"

# pg.click -> clicar
# pg.press -> apertar 1 tecla
# pg.hotkey -> conjunto de teclas
# pg.write -> escreve um texto

# Passo 1: Entrar no sistema da empresa (no nosso caso é o link do drive)
pg.press("win")
pg.write("chrome")
time.sleep(1)
pg.press("enter")
pg.write(link_drive)
pg.press("enter")
time.sleep(3)

# Passo 2: Navegar no sistema e encontrar a base de vendas (entrar na pasta exportar)
#pg.click(, clicks=2) # Clicar na pasta Exportar

# Passo 3: Fazer o download da base de vendas
pg.click(x=365, y=480) # Selecionar o arquivo
pg.click(x=1265, y=483) # Clicar nos 3 pontinhos
time.sleep(3)
pg.click(x=992, y=381) # Clicar em fazer o download
pg.click(x=527, y=440) # Salvar como
time.sleep(5)

