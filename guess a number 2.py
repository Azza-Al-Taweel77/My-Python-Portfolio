import random
correct_number= random.randint(1,10)
guess= int(input("Guess a number between 1 and 10: "))

while guess != correct_number:
    if guess > correct_number:
        guess= int(input("Too hight! Try again: "))
    else:
        guess= int(input("Too low! Try again: "))

print("Congratulation! You guessed a number.")