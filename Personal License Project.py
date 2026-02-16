print("Welcome to our application!")
age= int(input("Please enter your age? \n"))
license= input("Do you have a License? (Enter 'Yes' or 'No' )\n")

if age >=18 and license.lower()=="yes":
    print("You can use our app!")
elif age < 18 or license.lower()== "no":
    print("sorry, you con't use our app!")
else:
    print(f"sorry, but {license} is not nuderstood!")