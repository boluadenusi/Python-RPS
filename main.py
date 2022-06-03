import random 

print("Welcome to Rock, Paper and Scissors")
print("-----------------------------------")

choices = ["R", "P", "S"]

CPU = random.choice (choices);
player = None

while player not in choices:
 player = input("\nChoose one of R, P, or S?:" )
 if(player == "R" or player == "P" or player == "S"):
     break
 else:
        print("Invalid input. Let's try that again. \n Try your pick in CAPS!")

if player == CPU:
    print("Player:", player, " | CPU:", CPU)
    print("No WINNER, No LOSER!")
    player = input("\n Let's have a tie-breaker\nChoose one of R, P, or S?:" )


if player == "R" and CPU == "P":
    print("Player:", player, "| CPU:", CPU)
    print("You LOSE!")

elif player == "R" and CPU == "S":
    print("Player:", player, "| CPU:", CPU)
    print("You WIN!")

elif player == "P" and CPU == "S":
    print("Player:", player, "| CPU:", CPU)
    print("You LOSE!")

elif player == "P" and CPU == "R":
    print("Player:", player, "| CPU:", CPU)
    print("You WIN!")

elif player == "S" and CPU == "P":
    print("Player:", player, "| CPU:", CPU)
    print("You WIN!")

elif player == "S" and CPU == "R":
    print("Player:", player, "| CPU:", CPU)
    print("You LOSE!")

print("Game over! Thanks for playing")