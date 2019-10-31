'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
q=False
w=0
l=0
import random
print("Hey! lets play Rock, Paper, or Scissors game!")
while not q:
    print("(1) is for Rock,...(2) is for Paper,...(3) is for Scissors")
    ll=str(input("give me a number or press 4 to quit"))
    tt= random.randrange(1,4)
    if tt==1:
        c=1
    elif tt==2:
        c=2
    else:
        c=3
    if ll=="1" and c==1:
        w+=0
        l+=0
        print("That was a tie, from a Rock and a Rock")
    elif ll=="1" and c==2:
        l+=1
        print("You lose... Rock and Paper")
    elif ll=="1" and c==3:
        w+=1
        print("You win! Rock and Scissors")
    elif ll=="2" and c==1:
        w+=1
        print("You win! Paper and Rock")
    elif ll=="2" and c==2:
        l+=0
        w+=0
        print("That was a tie, from a Paper and a Paper")
    elif ll=="2" and c==3:
        l+=1
        print("You lose... Paper and Scissors")
    elif ll=="3" and c==1:
        l+=1
        print("You lose... Scissors and Rock")
    elif ll=="3" and c==2:
        w+=1
        print("You win! Scissors and Paper")
    elif ll=="3" and c==3:
        w+=0
        l+=0
        print("That was a tie, from a Scissors and a Scissors")
    elif ll=="4":
        q=True
    else:
        print("not an option!")
print("Wins:",w,"\nLoss:",l)
