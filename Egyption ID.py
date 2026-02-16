Nationality= input("Are you Egyption? Enter 'yes' or 'no' \n").lower()
if Nationality == "yes":
    age= input("Are you age above 15? Enter 'yes' or 'no' \n").lower()
    if age == "yes":
        print("you can have an ID.")
    else:
        print("please try agine when you have above 15!")
else:
    print("sorry, but only Egyption can use this service!")