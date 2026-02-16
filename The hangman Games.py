import random
words= ["red", "apple", "offcie", "panda"]
random_word= random.choice(words)
len_word= len(random_word)
display= "_" *(len_word)
lives= 6
print(" ".join(display))
while "_" in display and lives > 0:
    guessed= input("Please enter you guess: ").lower()
    if guessed not in random_word:
       lives -= 1
    for position in range(len(random_word)):
      if random_word[position] == guessed:
        display[position]= guessed
    print(display)
    print(f"You have {lives} more tlies")

print("""\n
                    YOU LOST! 
 +---+
  | |
  O |
/|\ |
/ \ |
      |
=====================|
""")