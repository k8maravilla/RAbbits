'''
Project Name: rabbits, rabbits, rabbits
Author: Kaleb Maravilla
Due Date: 02/17/2023
Course: CS1400-001

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.

    - when converting a list to string you just have to concatenate the integers and turn them into the string individually
    - it is important to pay attention to where you are defining your variables and then calling on them, otherwise they may not work
'''

import csv

def do_research(cages, adults, babies):
    teens = 0
    month = 1
    total = adults + teens + babies
    #my_list = [month, adults + teens, babies, total]
    
    header = [ 
        
        '# Table of rabbit pairs\n'
        'Month, ', 'Adults, ', 'Babies, ', "Total"
        ]

    data = []

    my_string = '\n' + str(month)+', ' + str(adults + teens) + ', ' + str(babies) + ', '+ str(total) + '\n'
    data.append(my_string)
    

    while total < cages: 
        #write to csv file
        adults += teens
        teens = babies
        babies = adults
        total = adults + teens + babies
        month += 1
        my_string = str(month)+', ' + str(adults + teens) + ', ' + str(babies) + ', '+ str(total) + '\n'
        data.append(my_string)
        if total > cages:
            data.append("# Cages will run out in month " + str(month))
            break

    with open('rabbits.csv', 'w') as file:
        file.writelines(header)
        file.writelines(data)

do_research(500,1,0)   




    

