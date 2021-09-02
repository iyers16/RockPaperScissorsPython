#! /usr/bin/env python3
import random
def validation(x):
    if(x=='r'):
        return(0)
    elif(x=='p'):
        return(1)
    elif(x=='s'):
        return(2)
    else:
        exit("Error...exiting now")

def playHand():
    rand = random.randint(0, 2)
    if(rand == 0):
        print("CPU played r")
    elif(rand == 1):
        print("CPU played p")
    elif(rand == 2):
        print("CPU played s")
    else:
        exit("Error...exiting now")
    return(rand)

def whoWon(uh, ch):
    if(uh==ch):
        print("Draw")
    elif((uh==0 and ch==1) or (uh==1 and ch==2) or (uh==2 and ch==0)):
        print("CPU Won!")
    elif((uh==0 and ch==2) or (uh==1 and ch==0) or (uh==2 and ch==1)):
        print("User Won!")
    else:
        exit("Error...exiting now")
    exit("Game Over!")


choice = input("Let's play rock, paper, scissors!Input r,p or s for rock, paper or scissors: ")
userHand = validation(choice)
cpuHand = playHand()
whoWon(userHand, cpuHand)
