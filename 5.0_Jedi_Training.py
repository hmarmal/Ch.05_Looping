  #Sign your name:Malsawmthara Hmar

'''
 1. Make the following program work.
   '''
print("hello")
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
      x = int(input("Enter a number: "))
      total = total + x
print("The total is:", total)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2,101,2):
    print(i)

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i=11
while i>0:
    i -= 1
    print(i)
print("Blast off!!")

'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
h= random.randrange(1,11)
print(h)

'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
print("This program takes seven numbers and returns the sum.")
total = 0
p=0
z=0
n=0
for i in range(7):
      x = int(input("Enter a number: "))
      if x>0:
          p+=1
      elif x==0:
          z+=1
      else:
          n+=1
      total = total + x
print("The total is:", total)
print("The count of\nPositive entries:",p)
print("Equals to 0:",z ,"\n# of negative numbers:",n)