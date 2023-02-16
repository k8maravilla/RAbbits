def do_research(cages, adults, babies):
    total = 1
    teens = 0
    month = 1


    while total < cages: 
        print(month, adults + teens, babies, total)
        adults += teens
        teens = babies
        babies = adults
        total = adults + teens + babies
        month += 1
        if total > cages:
            print(month, adults + teens, babies, total)
            print("cages will run out at month", month)
            break


do_research(500,1,0)   




    

