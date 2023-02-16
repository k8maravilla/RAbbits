import csv

def do_research(cages, adults, babies):
    total = 1
    teens = 0
    month = 1
    my_list = [month, adults + teens, babies, total]
    
    header = [ 
        
        #Table of rabbit pairs
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
            data.append("cages will run out at month " + str(month))
            break

    with open('run_rabbits', 'w') as file:
        file.writelines(header)
        file.writelines(data)
    print('done')

do_research(500,1,0)   




    

