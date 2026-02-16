import random
print("Welcome to 'whose wallet?' ")
print("Tou will give me a list of names, and i will pick a person to pay")
names= input("If you're ready, enter the names separated by a comma: ")
Next_names= names.split(", ")
New_names=random.randint(0,len(Next_names))
random_person= Next_names[New_names]
print(f"Please ask {random_person} to take his wallet out. Dinner is on him")