name= input("Enter the names attendees separated by commas: ")
list= name.split(", ")
for y in list:
    print(f"\n {y}")
    response= input("Is this person attending? (Yes/No): \n").lower()
    if response == "yes":
        print("Attendance confirmed")
    else:
        print("Attendance not confirmed")
    print("----------")