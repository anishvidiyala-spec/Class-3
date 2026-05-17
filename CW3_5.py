weekend = input("Is it a Weekend? (Yes/No): ")
holiday = input("Is it a holiday (Yes/No): ")

if weekend == "Yes" or holiday == "Yes":
    print("Shop is closed")
else:
    print("Shop is open")