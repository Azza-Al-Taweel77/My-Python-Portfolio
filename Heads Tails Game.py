import random 
print("Welcome to the Coin Guessing Game!")
print("Choose a method to toss the coin:")
print("1. Using random.random()" )
print("2. Using random.randint()")
guess= input("Enter Your Chose (1 or 2): \n")
if guess == "1":
    if random.random() >= 0.5:
        computer= "Heads"
    else:
        computer= "Tails"
elif guess == "2":
    if random.randint(0,1) == 0:
        computer= "Tails"
    else:
        computer= "Heads"
else:
    print("Invild chose. (Please select either 1 or 2)!")

your_guess= input("Enter your Guess (Heads or Tails) \n")

if your_guess.lower() == computer.lower():
    print("Congratulation! You Won.")
else:
    print("Sorry. You Lost!")

print(f"the computer's coin toss result was:{computer}")