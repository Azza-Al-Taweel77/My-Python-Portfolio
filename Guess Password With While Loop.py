correct_password= "k9o4r5"
entered= input("Enter password: ")

while entered != correct_password:
    print("Incorrect password! Try again. ")
    entered= input("Enter password again: ")
print("Access Granted!")