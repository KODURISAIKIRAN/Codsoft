import random
rock = """   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
gestures = [rock,paper,scissor]
print("              ____ROCK-PAPER-SCISSOR GAME____")
print()
print("Enter your choice for Rock:0,for paper:1,for scissor:2")
user = int(input())

if user<3:
    print("You choosed:")
    print(gestures[user])
    comp = random.randint(0,2)
    print("Computer choosed:")
    print(gestures[comp])
    if user == comp:
        print("Its Draw!")
    elif user == 2 and comp == 0 :
        print("You Lose :(")
    elif comp == 2 and user == 0 :
        print("You Win! :)")
    elif user < comp:
        print("You Lose :(")
    elif comp < user:
        print("You Win! :)")
else :
    print("User choice is Invalid You Lose :(")