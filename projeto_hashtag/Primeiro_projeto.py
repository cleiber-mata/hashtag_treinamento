import pyautogui as pg
import pandas as pd
import time
pg.PAUSE = 0.5
link_drive = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"

# Passo a passo do dessfio.
# Entrar no sistema da empressa;
    # Fazer login no sistema;
    # Abrir o navegador Chrome;
pg.press("win")
pg.write("chome")
pg.press("enter")
time.sleep(2)

    # Navegar até a base de dados;     
pg.write(link_drive)
pg.press("enter")
time.sleep(2)

# Exportar a base dedados;
# Calcular indicadores;
# Enviar as informações.

# pyautogui --> automações
# pandas --> dados
# openpyxl
# py -m pip install pandas pyautogui openpyxl

# pg.click --> clicar com o mouse
# pg.write --> escrever um texto
# pg.press --> pressiona uma tecla
# pg.hotkey --> combinações de teclas.
