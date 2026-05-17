people = int(input("How many people are in the hall?: "))

if people > 40:
    print("Extra Invigilator Needed")
elif people >25:
    print("Special Attention Required")
elif people < 10:
    print("Exam Hall Under Utilized")
else:
    print("Normal Duty")
