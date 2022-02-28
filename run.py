# Grab base from https://github.com/AmirrezaM21/OverwatchAutoLogin

from accs import Accs
import time
import os
import scaningScreen as scan
import inquirer

sample_img = ".\img\login.png"
launcher = ".\scripts\Overwatch.bat" # Bat just to force OW inicialize in high priority (a little better performace)


if __name__ == '__main__':
    accs = Accs()
    
    while True:
        choices = accs.btagList()
        choices.append("Add a new acc")
        choices.append("Exit")
        
        questions = [
            inquirer.List('answer',
                        message="Choose one of accs",
                        choices=choices,
                        carousel=True
                    ),
        ]
        addNewAcc = [
            inquirer.Text('btag', message="Btag"),
            inquirer.Text('email', message="Email"),
            inquirer.Password('password', message="Password")
        ]
        
        answers = inquirer.prompt(questions)

        if answers["answer"] == "Exit":
            exit()
        if answers["answer"] == "Add a new acc":
            newAcc = inquirer.prompt(addNewAcc)
            accs.addAcont(newAcc)
            time.sleep(0.5)
            os.system('cls')
        if answers["answer"] in accs.btagList():
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

    
    accs.login(answers['answer'])