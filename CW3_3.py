boys = int(input("How many boys are in the class: "))
girls = int(input("How many girls are in the class: "))

if boys == girls:
    print("Equal seating")
elif boys > girls:
    print("Larger Section of Boys")
elif boys < girls:
    print("Larger Section of Girls")
else:
    print("Normal Distrubution")
