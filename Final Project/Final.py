from turtle import *
import os
import random
os.system("stty erase '^H'")
print ("Hello, this game is about adventure!")
print ("You came to world of shape. Many shape is in this world.")
print ("The goal of this game is escaping this world.")
print ("The shape of the keyhole is composed by some simple shape. The simple shapes are on the table. Use them for open the door.")
print ("Good luck!")
ask_start = input("Type (play) if you want to start this game")
if ask_start == "play":
   print ("It is a first level.")
   canvas = Screen()
   canvas.setup(400,200)
   sarah = Turtle()
   sarah.speed(10)
   for i in [0,1,2,3]: 
       sarah.forward(50)
       sarah.left(90)
   for i in [0,1,2]:
       sarah.forward(50)
       sarah.left(120)
   for i in [0,1,2]:
       sarah.forward(50)
       sarah.right(120)
   canvas.exitonclick()
   print ("1. Square")
   print ("2. Triangle")
   print ("3. Rectangle")
   level1_q = int(input("Which shape was used in the keyhole? Choose one number"))
   level1_q2 = int(input("Do you want to choose another shape? Choose one number"))
   if (level1_q == 1 or 2) and (level1_q2 == 1 or 2):
       print ("You opened the door.")
   else:
         print ("Try again")
         
   print ("This is the next level.")
   canvas = Screen()
   canvas.setup(400,200)
   sarah = Turtle()
   sarah.speed(10)
   for i in [0,1,2,3,4,5]: 
       sarah.forward(50)
       sarah.left(60)
   for i in [0,1,2,3,4,5]:
       for i in [0,1,2]:
          sarah.forward(50)
          sarah.left(120)
       sarah.forward(50)
       sarah.left(60)
   
   canvas.exitonclick()
   print ("1. Square")
   print ("2. Triangle")
   print ("3. Rectangle")
   print ("4. Hexagon")
   level2_q = int(input("Which shape was used in the keyhole? Choose one number"))
   level2_q2 = int(input("Do you want to choose another shape? Choose one number"))
   if (level1_q == 2 or 4) and (level1_q2 == 2 or 4):
       print ("You opened the door.")
   else:
         print ("Try again")
         
   print ("This is the final level.")
   canvas = Screen()
   canvas.setup(400,200)
   sarah = Turtle()
   sarah.speed(10)
   for i in [0,1,2,3,4,5,6,7]: 
    sarah.forward(50)
    sarah.left(40)
    for i in [0,1,2,3,4,5]:
           for i in [0,1,2]:
             sarah.forward(50)
             sarah.left(120)
           sarah.forward(50)
           sarah.left(60)
   canvas.exitonclick()
   print ("1. Square")
   print ("2. Triangle")
   print ("3. decagon")
   print ("4. Hexagon")
   print ("5. trapezoid")
   print ("6. Rectangle")
   print ("7. Diamond")
   level3_q = int(input("Which shape was used in the keyhole? Choose one number"))
   level3_q2 = int(input("Do you want to choose another shape? Choose one number"))
   level3_q3 = int(input("Do you want to choose another shape? Choose one number"))
   level3_q4 = int(input("Do you want to choose another shape? Choose one number"))
   if (level3_q == 2 or 3 or 5 or 7) and (level3_q2 == 2 or 3 or 5 or 7) and (level3_q3 == 2 or 3 or 5 or 7) and (level3_q4 == 2 or 3 or 5 or 7):
       print ("You opened all of the door. Congratulation!!!!!")
   else:
         print ("Try again, Cheer up!")
