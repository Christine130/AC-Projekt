import PySimpleGUI as sg
import random
from random import randint
import csv
sg.theme('DarkBlue3') #värviteema

andmed = [] 
csvfail = open('list.csv', encoding='UTF-8')
loetudCSV = csv.reader(csvfail, delimiter=',')
 
for rida in loetudCSV:
    andmed.append(rida)
csvfail.close()


# main menu 
paigutus1 = [
            [sg.Text('Choose how many words you would like: ', font=("Helvetica", 10))],
            [sg.Submit("10")],
            [sg.Submit("20")],
            [sg.Submit("50")],
            [sg.Cancel('Quit')]
]


#akna loomine
aken = sg.Window('Pengulino', paigutus1, size=(400,200))
syndmus, v22rtused = aken.read()


#sündmuste tsükkel
while True:
    if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
        break
    aken.close()


    if syndmus == "10":
        i = 0
        punktid = 0
        while i <= 10:
            
            #print(i)
            i += 1
            
            number = randint(2, 204)
            word = (andmed[number][0])
            #print(andmed[number][0])
            #print(andmed[number][1])
            with open('list.csv', encoding='UTF-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                answer1 = (random.choice([line[1] for line in reader]))
            with open('list.csv', encoding='UTF-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                answer2 = (random.choice([line[1] for line in reader]))
            answer3 = (andmed[number][1])

            answer_list = [answer1, answer2, answer3]
            random.shuffle(answer_list)
            
            paigutus2 = [
            [sg.Text('Choose the right translation for: ', font=("Helvetica", 10))],
            [sg.Text( word, font=("Helvetica", 14))],
            [sg.Submit(answer_list[0])],
            [sg.Submit(answer_list[1])],
            [sg.Submit(answer_list[2])],
            [sg.Cancel('Quit')]
]
            

            aken = sg.Window('Pengulino', paigutus2, size=(400,200))
            syndmus, v22rtused = aken.read()
            
            if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                break
            aken.close()
                
                                    
            if syndmus == (answer_list[0]):
                if (answer_list[0]) == (andmed[number][1]):
                    punktid += 1
                    #print(punktid)
                    sg.Popup('Right answer.')
                    if i == 10:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/10" + "\n" + str(int(punktid) / 10 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
                else:
                    sg.Popup('Wrong answer.')
                    if i == 2:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/10"  + "\n" + str(int(punktid) / 10 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
            if syndmus == (answer_list[1]):
                if (answer_list[1]) == (andmed[number][1]):
                    punktid += 1
                    #print(punktid)
                    sg.Popup('Right answer.')
                    if i == 10:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/10"  + "\n" + str(int(punktid) / 10 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
                else:
                    sg.Popup('Wrong answer.')
                    if i == 10:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/10"  + "\n" + str(int(punktid) / 10 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
            if syndmus == (answer_list[2]):
                if (answer_list[2]) == (andmed[number][1]):
                    punktid += 1
                    #print(punktid)
                    sg.Popup('Right answer.')
                    if i == 10:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/10"  + "\n" + str(int(punktid) / 10 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
                else:
                    sg.Popup('Wrong answer.')
                    if i == 10:
                        paigutus3 = [
                        [sg.Text("Finished the game \n Your score: " + str(punktid) + "/10"  + "\n" + str(int(punktid) / 10 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
                    
 
 
 







    if syndmus == "20":
        i = 0
        punktid = 0
        while i <= 30:
            
            #print(i)
            i += 1
            
            number = randint(2, 204)
            word = (andmed[number][0])
            #print(andmed[number][0])
            #print(andmed[number][1])
            with open('list.csv', encoding='UTF-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                answer1 = (random.choice([line[1] for line in reader]))
            with open('list.csv', encoding='UTF-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                answer2 = (random.choice([line[1] for line in reader]))
            answer3 = (andmed[number][1])

            answer_list = [answer1, answer2, answer3]
            random.shuffle(answer_list)
            
            paigutus2 = [
            [sg.Text('Choose the right translation for: ', font=("Helvetica", 10))],
            [sg.Text( word, font=("Helvetica", 14))],
            [sg.Submit(answer_list[0])],
            [sg.Submit(answer_list[1])],
            [sg.Submit(answer_list[2])],
            [sg.Cancel('Quit')]
]
            

            aken = sg.Window('Pengulino', paigutus2, size=(400,200))
            syndmus, v22rtused = aken.read()
            
            if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                break
            aken.close()
                
                                    
            if syndmus == (answer_list[0]):
                if (answer_list[0]) == (andmed[number][1]):
                    punktid += 1
                    #print(punktid)
                    sg.Popup('Right answer.')
                    if i == 20:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/20" + "\n" + str(int(punktid) / 20 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
                else:
                    sg.Popup('Wrong answer.')
                    if i == 20:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/20" + "\n" + str(int(punktid) / 20 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
            if syndmus == (answer_list[1]):
                if (answer_list[1]) == (andmed[number][1]):
                    punktid += 1
                    #print(punktid)
                    sg.Popup('Right answer.')
                    if i == 20:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/20" + "\n" + str(int(punktid) / 20 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
                else:
                    sg.Popup('Wrong answer.')
                    if i == 20:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/20" + "\n" + str(int(punktid) / 20 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
            if syndmus == (answer_list[2]):
                if (answer_list[2]) == (andmed[number][1]):
                    punktid += 1
                    #print(punktid)
                    sg.Popup('Right answer.')
                    if i == 20:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/20" + "\n" + str(int(punktid) / 20 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
                else:
                    sg.Popup('Wrong answer.')
                    if i == 20:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/20" + "\n" + str(int(punktid) / 20 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
                    










    if syndmus == "50":
        i = 1
        punktid = 0
        while i <= 50:
            
            #print(i)
            i += 1
            
            number = randint(2, 204)
            word = (andmed[number][0])
            #print(andmed[number][0])
            #print(andmed[number][1])
            with open('list.csv', encoding='UTF-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                answer1 = (random.choice([line[1] for line in reader]))
            with open('list.csv', encoding='UTF-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                answer2 = (random.choice([line[1] for line in reader]))
            answer3 = (andmed[number][1])

            answer_list = [answer1, answer2, answer3]
            random.shuffle(answer_list)
            
            paigutus2 = [
            [sg.Text('Choose the right translation for: ', font=("Helvetica", 10))],
            [sg.Text( word, font=("Helvetica", 14))],
            [sg.Submit(answer_list[0])],
            [sg.Submit(answer_list[1])],
            [sg.Submit(answer_list[2])],
            [sg.Cancel('Quit')]
]
            

            aken = sg.Window('Pengulino', paigutus2, size=(400,200))
            syndmus, v22rtused = aken.read()
            
            if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                break
            aken.close()
                
                                    
            if syndmus == (answer_list[0]):
                if (answer_list[0]) == (andmed[number][1]):
                    punktid += 1
                    #print(punktid)
                    sg.Popup('Right answer.')
                    if i == 50:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/50" + "\n" + str(int(punktid) / 50 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
                else:
                    sg.Popup('Wrong answer.')
                    if i == 50:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/50" + "\n" + str(int(punktid) / 50 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
            if syndmus == (answer_list[1]):
                if (answer_list[1]) == (andmed[number][1]):
                    punktid += 1
                    #print(punktid)
                    sg.Popup('Right answer.')
                    if i == 50:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/50" + "\n" + str(int(punktid) / 50 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
                else:
                    sg.Popup('Wrong answer.')
                    if i == 50:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/50" + "\n" + str(int(punktid) / 50 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
            if syndmus == (answer_list[2]):
                if (answer_list[2]) == (andmed[number][1]):
                    punktid += 1
                    #print(punktid)
                    sg.Popup('Right answer.')
                    if i == 50:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/50" + "\n" + str(int(punktid) / 50 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
                else:
                    sg.Popup('Wrong answer.')
                    if i == 50:
                        paigutus3 = [
                        [sg.Text("Finished the game \nYour score: " + str(punktid) + "/50" + "\n" + str(int(punktid) / 50 * 100) + " %", font=("Helvetica", 10))],
                        [sg.Cancel('Quit')]
]
                        aken = sg.Window('Pengulino', paigutus3, size=(400,200))
                        syndmus, v22rtused = aken.read()
                        if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
                            break
                        
aken.close()
