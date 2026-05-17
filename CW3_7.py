student_id = input("Do you have your Student ID (Yes/No): ")
permission_slip = input("Did you get a permission slip from your teacher (Yes/No): ")

if student_id == "Yes" or permission_slip == "Yes":
    print("Entry Allowed")
else:
    print("Entry Denied")
    