#!python3

# Grab base from https://github.com/AmirrezaM21/OverwatchAutoLogin

from operator import index
from accs import Accs
import time
import os
import scaningScreen as scan

def choose(accs):
    print("Choose one of accs")

    lista = accs.btagList()
    
    lista.append("Add a new acc")
    lista.append("Exit")

    i = 0
    while(i < len(lista)):
        print(f"{i+1} -- {lista[i]}")
        i += 1

    resp = int(input("N°: "))

    while (resp > len(lista)):
        resp = int(input("N° not in list: "))

    return resp, i


sample_img = ".\img\login.png"
launcher = ".\scripts\Overwatch.bat" # Bat just to force OW inicialize in high priority (a little better performace)


if __name__ == '__main__':
    accs = Accs()
    
    while True:
        resp, i = choose(accs)
        
        if  resp == i:
            exit()
        
        if resp == i-1 : 
            accs.addAcont()
        else:
            break
    
    print("Running Script...")
    print("Opening Overwatch client")
    os.startfile(launcher)
   
    try:
        sample = scan.readImage(sample_img)
    except NameError:
        print("Can't open sample file!")
        print(NameError)
        exit()
    
    time.sleep(2)
    while not scan.locateOnScreen(sample):
        print("trying to locate element..")
        time.sleep(0.12)
    time.sleep(0.1)
    
    index = accs.btagList()
    
    accs.login(index[resp-1])