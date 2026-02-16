import random
my_random= random.randint(1000,9999)
New_random= int(input("Enter a 4_digits PIN code: \n"))

if len(str(New_random))!= 4:
    print("please Enter 4 digits!")
elif my_random == New_random:
    print("Conratulation! PIN code matched.")
else:
    print("Failure! PIN code did not match!")
    print(f"The combuter generatedthis PIN: {my_random}")