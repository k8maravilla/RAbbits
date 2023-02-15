
adults = 0
babies = 0
total = 1
teens = 1
month = 1
cages = 500

while total < cages:
    print("start", adults + teens, babies, total)
    adults += teens
    teens = babies
    babies = adults
    total = adults + teens + babies




    

