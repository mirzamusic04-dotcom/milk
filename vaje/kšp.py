import random as r
computer = r.choice(['R', 'P', 'S'])
player = input("Your choice:")[0].lower()
if computer == "R" and player == "P":
    print("you won :)")
if computer == "S" and player == "P":
    print("you lost too bad")
if computer == "S" and player =="R":
    print("you won :)")   
if computer == "P" and player =="R":
    print("you lost too bad")
if computer == "P" and player =="S":
    print("you won :)") 
if computer == "R" and player =="S":
    print("you lost too bad")                    