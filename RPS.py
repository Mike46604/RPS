import random
yourscore = 0
computerscore = 0
#Gives a value of zero to yourscore and computerscore

def game():
    global yourscore
    global computerscore
#Brings the values yourscore and computerscore into the function. 
    player = input("Enter your choice (rock/paper/scissors):")
    while (player != "rock" and player != "paper" and player != "scissors"):
        print(player)
        player = input("Invalid Input. Enter your choice (rock/paper/scissors): ")
    computer = random.randint(0, 2)
    if (computer == 0):
        computer = "rock"
    elif (computer == 1):
        computer = "paper"
    elif (computer == 2):
        computer = "scissors"
 #Assigns a number to a position and randomly picks from those numbers. 
    if (player == computer):
        print("Draw!")
        print("Your Score:", yourscore, "Computer Score:", computerscore)
    elif (player == "rock"):
        if (computer == "paper"):
            print("Computer wins!")
            computerscore = computerscore + 1
            print("Your Score:", yourscore, "Computer Score:", computerscore)
        else:
            print("You win!")
            yourscore = yourscore + 1
            print("Your Score:", yourscore, "Computer Score:", computerscore)
    elif (player == "paper"):
        if (computer == "rock"):
            print("You win!")
            yourscore = yourscore + 1
            print("Your Score:", yourscore, "Computer Score:", computerscore)
        else:
            print("Computer wins!")
            computerscore = computerscore + 1
            print("Your Score:", yourscore, "Computer Score:", computerscore)
    elif (player == "scissors"):
        if (computer == "rock"):
            print("Computer wins!")
            computerscore = computerscore + 1
            print("Your Score:", yourscore, "Computer Score:", computerscore)
        else:
            print("You win!")
            yourscore = yourscore + 1
            print("Your Score:", yourscore, "Computer Score:", computerscore)

    print("Your choice: " + player + "\nComputer choice: " + computer + "\nThank you for playing!")

    input("Press Enter to play again")
    
    
while True:
    game() 
    #loops the function so that it can be played again
