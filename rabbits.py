def do_research(cages, adults, babies):
    total = 1
    teens = 0
    month = 1
    my_list = [month, adults + teens, babies, total]

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









# my_file = open('run_rabbits.txt', 'w')

# my_list = [
    # []
# ]

# my_file.close()

do_research(500,1,0)   




    

