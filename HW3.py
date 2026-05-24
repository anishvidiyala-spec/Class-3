print("Smart Home Security System")
print("1. Check Door Access")
print("2. Check Security Alert")
print("3. Exit")

choice = int(input("Choose your option(1/2/3) :"))

if choice == 1:
    passcode = input("Is the passcode entered?(yes/no): ")
    present_owner = input("Is the owner present(yes/no): ")
    time = int(input("What is the hour(0-23)?"))

    if time >= 6 and time <=18:
        print("Door Access Granted")
elif choice == 2:
    door = input("Is the door open?(yes/no): ")
    owner_present = input("Is the owner present(yes/no): ")

    if door.lower() == "yes" and owner_present.lower() == "no":
        print("Security Alarm Triggered")
    else: 
        print("No Alert")
else:
    print("You have exited the system.")  
    


