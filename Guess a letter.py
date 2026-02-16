import random
words= ["office", "panda", "cabin", "ginger"]
choice= random.choice(words)
guessed= input("Please guess a latter: ").lower()

for letter in choice:
    if guessed == letter:
        print("Right")
    else:
        print("Wrong")