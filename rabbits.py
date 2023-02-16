import csv

def do_research(cages, adults, babies):
    total = 1
    teens = 0
    month = 1
    my_list = [month, adults + teens, babies, total]
    
    header = ['Month, ', 'Adults, ', 'Babies, ', "Total"]

    data = []

    while total < cages: 
        #write to csv file
        adults += teens
        teens = babies
        babies = adults
        total = adults + teens + babies
        month += 1
        my_list = [month, adults + teens, babies, total]
        print(my_list)
        if total > cages:
            print("cages will run out at month", month)
            break

    with open('run_rabbits', 'w') as file:
        file.writelines(header)
        file.writelines(data)
    print('done')

do_research(500,1,0)   




    

