import requests
import pyautogui
import pandas as pd
import subprocess
from time import sleep


class OpenDock:
    def __init__(self):
        pass

    def open_app_and_browse(self, app_name, site_name):
        # If the user wants to open an app and browse a website
        sleep(1)
        nome_do_aplicativo = app_name
        comando = f"start {nome_do_aplicativo}"
        subprocess.run(comando, shell=True)
        pyautogui.click(x=500, y=50)
        pyautogui.write(site_name)
        pyautogui.press("enter")

    def open_app(self, app_name):
        sleep(1)
        nome_do_aplicativo = app_name
        comando = f"start {nome_do_aplicativo}"
        subprocess.run(comando, shell=True)

    def open_dock_txt(self, dock_name):
        sleep(1)
        # If the user wants to open a specific document
        try:
            with open(
                f"C:\\Users\\Kauan\\OneDrive\\Área de Trabalho\\back-end\\Arquivo_txt\\{dock_name}.txt",
                "r",
            ) as arquivo:
                dados = arquivo.read()
                return print(dados)
        except FileNotFoundError:
            sleep(1)
            print("Perdão, não consegui localizar o documento")

    def open_dock_xlsx(self, dock_name):
        # If the user wants to open a specific document
        sleep(1)
        try:
            open_xlsx = pd.read_excel(
                f"C:\\Users\\Kauan\\OneDrive\\Área de Trabalho\\{dock_name}.xlsx"
            )
            opened_xlsx = pd.DataFrame(open_xlsx)
            print(opened_xlsx)
            print(open_xlsx.shape)
        except FileNotFoundError:
            sleep(1)
            print("Perdão, não consegui localizar o documento")
