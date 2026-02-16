attendees=["Alice", "Bob", "Charlie"]
for x in attendees:
    print(x)
    attend= input("Is this person attensing? (Yes/No): ").lower()
    if attend == "yes":
        print("Attendance confirmed")
    else:
        print("Attendance not confirmed")
    print("---------------")