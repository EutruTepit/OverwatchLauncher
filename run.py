# Grab base from https://github.com/AmirrezaM21/OverwatchAutoLogin

from accs import Accs
import time
import os
import scaningScreen as scan
import inquirer
import dirProce

if __name__ == '__main__':
    config = dirProce.openConfig()
    accs = Accs()
    
    while True:
        choices = accs.btagList()
        choices.append("Add a new acc")
        choices.append("Delete acc")
        choices.append("Exit")
        
        questions = [
            inquirer.List('answer',
                        message="Choose one of accs",
                        choices=choices,
                        carousel=True
                    ),
        ]
        
        answers = inquirer.prompt(questions)

        if answers["answer"] == "Exit":
            exit()
            
        if answers["answer"] == "Add a new acc":
            addNewAcc = [
                inquirer.Text('btag', message="Btag"),
                inquirer.Text('email', message="Email"),
                inquirer.Password('password', message="Password")
            ]
            
            newAcc = inquirer.prompt(addNewAcc)
            accs.addAcont(newAcc)
            
            time.sleep(0.5)
            os.system('cls')
            
        if answers["answer"] == "Delete acc":
            delacc = accs.btagList()
            delacc.append("Cancel")
            
            choicesDel = [
                inquirer.List('answer',
                        message="Choose to delete",
                        choices=delacc,
                        carousel=True
                    ),
            ]
            
            selectAcc = inquirer.prompt(choicesDel)
            
            if selectAcc['answer'] != "Cancel":
                os.system('cls')
                print("Acc deleted: ", accs.delAcont(selectAcc['answer']))
            else:
                time.sleep(0.5)
                os.system('cls')
                print("Operation canceled.")
            
        if answers["answer"] in accs.btagList():
            break
 
    print("Running Script...")
    print("Opening Overwatch client")

    os.system(config.get('commands', 'start_overwatch'))
   
    try:
        sample = scan.readImage(config.get('paths', 'sample_img'))
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