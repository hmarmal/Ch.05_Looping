'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
print('hey man you have to play my "escaping" game!')
print("So!! You are a red tiger and a hunter is trying to hunt you. ")
print("You have 6 times to drink, and just run 200 miles away from you current location.")
hun=-20
mi=0
thir=0
tir=0
can=6

done=False

while not done:
  water=random.randrange(1,21)
  if water==1:
      print("You have found a water place to drink from!") # water place 1 in 20
      can=6
      thir=0
      tir=0
  if thir>4 and thir<6:
      print("You are thirsty drink quick!")
  elif thir>6:
      print("You died of thirst!")
      done=True
  elif tir>5 and tir<8:
      print("You are getting tired")
  elif tir>8:
      print("You died from exhaustion")
      done=True
  elif mi-hun<0:
      print("The hunter caught you!")
      done=True
  elif mi-hun<15 and mi-hun>0:
      print("The hunter is getting close!!")
  elif mi>200:
      print("You won the game!!!!!")
      done=True



  print("A.Drink from you spiritual canteen")
  print("B.Run moderate speed")
  print("C.Run full speed")
  print("D.Stop for the night")
  print("E.Status check")
  print("Q.Quit")
  qu=str(input(" Choose one>>>>!!"))
  if qu.lower()=="q":
      done=True
  elif qu.lower()=="e":
      print("Miles traveled:",mi)
      print("Available drinks from canteen:",can)
      print("The hunter is",mi-hun,"miles behind you.")
  elif qu.lower()=="d":
      tir=0
      print("You regained your energy!")
      num1 =random.randrange(7,15) #hunter
      hun+=num1
  elif qu.lower()=="c":
      num2=random.randrange(10,21) #random travel
      mi+=num2
      print("Miles traveled",mi)# miles traveled
      thir+=1
      num3=random.randrange(1,4)
      tir+=num3
      num1 = random.randrange(7, 15)  # hunter
      hun += num1
  elif qu.lower()=="b":
      num2 = random.randrange(5, 13)  # random travel
      mi += num2
      print("Miles traveled", mi)  # miles traveled
      thir+=1
      tir+=1
      num1 = random.randrange(7, 15)  # hunter
      hun += num1
  elif qu.lower()=="a":
      if can>0:
          can-=1
          thir=0
      else:
          print("Wow there!! sorry you have no more water in your canteen.")
  else:
      print("Not an option")