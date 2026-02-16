import random
print("Welcome to 'whose wallet?' ")
print("You will give me a list of names, and i will pick a person to pay ")
names= input("If you're ready, enter the names seapareted by a comman: ").split(", ")
print(f"Please ask '{random.choice(names)}' yo take out his wallet. Dinner is on him")