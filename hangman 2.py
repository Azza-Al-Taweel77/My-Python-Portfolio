import random
hangman=[
"""
+---+
  | |
      |
      |
      |
      |
=========
""", 
"""
+---+
  | |
  O |
      |
      |
      |
=========
""", 
"""
+---+
  | |
  O |
  | |
      |
      |
=========
""", 
"""
+---+
  | |
  O |
/| |
      |
      |
=========
""",
"""
+---+
  | |
  O |
/|\ |
      |
      |
=========
""", 
"""
+---+
  | |
  O |
/|\ |
/ |
      |
=======
""", 
"""
+---+
  | |
  O |
/|\ |
/ \ |
      |
=======
"""]

words= ["open", "photo", "respect", "car", "tired"]
guessed_words= []
random_words= random.choice(words)
display= ["_"] * (len(random_words))
print(" ".join(display))
print(hangman[0])
lives= 6
while "_" in display and lives > 0:
    print(" ".join(display))
    guessed= input("Please guess a letter: ")
    if guessed in guessed_words:
       print(f"You alresdy guessed that. Try again.")
       print(f"You have {lives} more tries")
       continue
    guessed_words.append(guessed)
    if guessed not in random_words:
       lives -= 1
       print(hangman[5-lives])
       print(f"You have {lives} more tries")
    for position in range(len(random_words)):
     if random_words[position] == guessed:
         display[position] = guessed
         print(display)
         print(f"You have {lives} more trise")

if lives == 0:
   print(f"""
         
                         YOU LOST!😭😭
         

         {hangman[-1]}


""")
else:
   
   print("""

                     ******************
                        YOU WIN!🤩🤩
                     ******************

""")