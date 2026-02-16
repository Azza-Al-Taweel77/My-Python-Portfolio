import random
words= ["bad", "nice", "apple", "online", "careful", "cat", "fat", "shorts"]
random_word= random.choice(words)
display= ["_"] * (len(random_word))
lives= 6
print(" ".join(display))
print("""
+---+
      |
      |
      |
      |
=========|
""")

hangman_list= [
"""
+---+
  | |
    |
      |
      |
      |
=========""",
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
=========""", 
"""
+---+
  | |
  O |
/|\ |
      |
      |
=========""", 
"""
+---+
  | |
  O |
/|\ |
/ |
      |
=======""", 
"""
+---+
  | |
  O |
/|\ |
/ \ |
      |
========="""]
choice_letter =[]
while "_" in display and lives > 0:
    guessed= input("Please guess a letter: ").lower()
    if guessed in choice_letter:
         print(f"You already guessed that. Try again.")
         print(f"You have {lives} more tries")
         continue
    choice_letter.append(guessed)
    if guessed not in random_word:
            lives -= 1
            print(hangman_list[5-lives])


    for position in range(len(random_word)):
         if random_word[position] == guessed:
             display[position] = guessed
    print(display)
    print(f"You have {lives} more tries")
if ("".join(display)) == random_word:
      print("""
                  ***********
                    YOU WIN!
                  ***********

                                    """)
      
else:

      print(f"""You have {lives} more trist
      

                             You lost!  



              {hangman_list[-1]}""")

