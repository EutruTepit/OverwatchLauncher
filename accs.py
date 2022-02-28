#!python3

# Grab base from https://github.com/AmirrezaM21/OverwatchAutoLogin

import time
import pyautogui as pag
import numpy as np
import json
from getpass import getpass


class Accs:
    def __init__(self):
        self.accs = self.openJson()
    
    def openJson(self):
        try:
            with open("accs.json") as jsonfile:
                jsonFile = json.load(jsonfile)
            return jsonFile
        except:
            return {}
    
    def saveJson(self):
        with open("accs.json", "w") as jsonfile:
            json.dump(self.accs, jsonfile, indent=4)

    def login(self, index):
        pag.typewrite(self.accs[str(index)]['email'])
        time.sleep(0.1)
        pag.press('tab')
        pag.typewrite(self.accs[str(index)]['password'])
        time.sleep(0.1)
        pag.press('enter')

    def addAcont(self):
        email = input("Email: ")
        password = getpass("Password: ")

        self.accs[str(len(self.accs)+1)] = {"email": email, "password": password}

        self.saveJson()