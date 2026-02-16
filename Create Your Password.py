import random
import string

print("\nwelcome to the password generator!\n".title())

total= int(input("Enter the  total number of characters in the password: "))
letters= int(input("Enter the number of letters in the password: "))
numbers= int(input("Enter the number of numbers in the password: "))
symbols= int(input("Enter the number of symbols in the password: "))
total_items= []

new_total= letters + numbers + symbols

if total == new_total:
    password= random.choices(string.ascii_letters, k= letters)
    digits= random.choices(string.digits, k= numbers)
    new_symbols= random.choices(string.punctuation, k= symbols)

    total_items.extend(password)
    total_items.extend(digits)
    total_items.extend(new_symbols)

    random.shuffle(total_items)
    the_list= "".join(total_items)
    print(f"Generated Password: {the_list}")
    
else:
    print("invilid input. the sum of letters, numbers, and symbols doen't match the password!")