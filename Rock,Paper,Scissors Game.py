import random
print("Welcome to the Rock, Paper, Scissors game: ")
press= input("Press Enter to continue or type (Help) for the rules help: ")

if press.capitalize() == "Help": 
    print("                ⁎⁎⁎⁎⁎⁎⁎⁎⁎⁎⁎ RULES ⁎⁎⁎⁎⁎⁎⁎⁎⁎⁎⁎")
    print("""             
                          1) You choose and computer choose 
                          2) Rock smashes Scissors -> Rock wins 
                          3) Scissors cut paper -> Scissors win
                          4) Paper ciners Rock -> Paper wins""")

rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice= input("Please enter your chose (Rock, Paper or Scissors): ").lower()
if choice not in ["rock", "paper", "scissors"]:
    print("Invild Chose! ")
    exit()
else:
    if choice== "rock":
        print(f"You chose: \n{rock}")
    elif choice== "paper":
        print(f"You chose: \n{Paper}")
    else:
        print(f"You chose: \n{scissors}")

computer= random.choice(["rock","paper", "scissors"])
if computer== "rock":
    print(f"Computer chose: \n{rock}")
elif computer== "paper":
    print(f"Computer chose: \n{Paper}")
elif computer== "scissors":
    print(f"Computer chose: \n{scissors}")

if choice == computer:
    print("it's a tie")
elif(choice == "rock" and computer == "scissors") or (choice== "paper" and computer == "rock") or (choice == "scissors" and computer == "paper"):
    print(f"You Win! {choice} beats {computer}")
else:
    print(f"You lost! {choice} beats {computer}")