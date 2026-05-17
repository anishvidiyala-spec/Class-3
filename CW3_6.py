card = input("Do you have an admit card (Yes/No): ")
fees = input("Did you pay the exam fees (Yes/No): ")

if card == "Yes" and fees == "Yes":
    print("You can enter the exam hall")
else:
    print("You are not allowed to enter the hall.")