# Bao Ying Choob
import random # for random what computer choose
print ("Welcome to Bao Ying Choob Game")
c_list= ["rock", "scissor", "paper"]
 
com_choice = random.choice(c_list) #Computer to random choice
player_choice=input("What do you choose? (rock, scissor,paper): ")
print(f"You chose: {player_choice}")
print(f"Computer chose: {com_choice}") #To show what computer chose

if player_choice == com_choice:
    print("The result : Draw ")
elif (player_choice == "rock" and com_choice == "paper") or \
    (player_choice == "paper" and com_choice == "scissor") or \
    (player_choice == "scissor" and com_choice == "rock"):
    print ("You LOSE T_T ")
else:
    print("Congratulations You WIN! *_* ")

              