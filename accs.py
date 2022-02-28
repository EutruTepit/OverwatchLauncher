# Grab base from https://github.com/AmirrezaM21/OverwatchAutoLogin

import time
import pyautogui as pag
import json


class Accs:
    def __init__(self):
        self.accs = self.openJson()
    
    def openJson(self):
        try:
            with open("accs.json", encoding='utf-8') as jsonfile:
                jsonFile = json.load(jsonfile)
            return jsonFile
        except:
            return {}
    
    def saveJson(self):
        with open("accs.json", "w") as jsonfile:
            json.dump(self.accs, jsonfile, indent=4)

    def login(self, index):
        pag.typewrite(self.accs[index]['email'])
        time.sleep(0.1)
        pag.press('tab')
        pag.typewrite(self.accs[index]['password'])
        time.sleep(0.1)
        pag.press('enter')

    def addAcont(self, newAcc):  
        self.accs[newAcc['btag']] = {"email": newAcc["email"], "password": newAcc["password"]}

        self.saveJson()
    
    def delAcont(self, delacc):
        self.accs.pop(delacc)
        
        self.saveJson()
        return delacc
        
    def btagList(self):
        return list(self.accs.keys())