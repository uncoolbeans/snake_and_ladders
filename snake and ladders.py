#snake and ladders 
import random as rnd
def dice():
    return rnd.randint(1,6)

def snake_ladders():
    pos = 0
    rolls = 0
    squareslist = ["start"]
    snakeSquares = [12,17,23,36,45]
    ladderSquares = [15,19,25,37,42]
    for i in range(1,51):
        squareslist.append([i,0])
    for item in snakeSquares:
        squareslist[item][1] = "snake"
    for item in ladderSquares:
        squareslist[item][1] = "ladder"
    print(squareslist)
    while pos < 50:
        uselessInput = input("Press enter to roll dice: ")
        steps = dice()
        rolls += 1
        pos += steps
        print(f"You rolled {steps}.\nYour position is {pos}.")
        if pos <= 50:
            if squareslist[pos][1] == "snake":
                pos -= 5
                print(f"You hit a snake! You go back 5 steps, your new position is {pos}.")
            elif squareslist[pos][1] == "ladder":
                pos += 5
                print(f"You hit a ladder! You go forward 5 steps, your new position is {pos}.")

    print(f"You have reached the end! You took {rolls} rolls of the dice to finish the game!")
        
        


        

snake_ladders()