import PySimpleGUI as sg
import random
from random import randint
import csv
sg.theme('DarkAmber') #värviteema

number = randint(2, 72) 


andmed = [] 
csvfail = open('list.csv', encoding='UTF-8')
loetudCSV = csv.reader(csvfail, delimiter=',')
 
for rida in loetudCSV:
    andmed.append(rida)
csvfail.close()

word = (andmed[number][0])
print(andmed[number][0])
print(andmed[number][1])


with open('list.csv', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)
    # This skips over the first line in the .csv
    next(reader)
    answer1 = (random.choice([line[1] for line in reader]))
#print(answer1)

with open('list.csv', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)
    # This skips over the first line in the .csv
    next(reader)
    answer2 = (random.choice([line[1] for line in reader]))
#print(answer2)

answer3 = (andmed[number][1])
#print(answer3)

answer_list = [answer1, answer2, answer3]
random.shuffle(answer_list)
#print(answer_list[0])



paigutus = [
            [sg.Text('Choose the right translation for: ', font=("Helvetica", 10))],
            [sg.Text( word, font=("Helvetica", 14))],
            [sg.Submit(answer_list[0])],
            [sg.Submit(answer_list[1])],
            [sg.Submit(answer_list[2])],
            [sg.Cancel('Quit')]
]

#akna loomine
aken = sg.Window('Pengulino', paigutus, size=(400,200))



#sündmuste tsükkel
while True:  
    syndmus, v22rtused = aken.read()
    if syndmus == sg.WIN_CLOSED or syndmus == 'Quit':
            break
        
        
    if syndmus == (answer_list[0]):
        if (answer_list[0]) == (andmed[number][1]):
            sg.Popup('Right answer.')
        else:
            sg.Popup('Wrong answer.')

              
    if syndmus == (answer_list[1]):
        if (answer_list[1]) == (andmed[number][1]):
            sg.Popup('Right answer.')
        else:
            sg.Popup('Wrong answer.')


    if syndmus == (answer_list[2]):
        if (answer_list[2]) == (andmed[number][1]):
            sg.Popup('Right answer.')
        else:
            sg.Popup('Wrong answer.')

aken.close()