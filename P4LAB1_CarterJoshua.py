#Joshua Carter
#03/25/24
#P4LAB1
#Making turtles move around lol

import turtle          
win = turtle.Screen()  
ben = turtle.Turtle()

# add some display options
ben.pensize(4)            # increase pensize (takes integer)
ben.pencolor("purple")     # set pencolor (takes string)
ben.shape("turtle")

for item in range(4):
    #actions to happen
    ben.forward(100)
    ben.left(90)
  

print()

for item in range(3):
    #actions to happen
    ben.forward(100)          
    ben.left(120)            

