
#Butterfly's head

import turtle
head = turtle.Turtle()
head.speed(0)
head.width(30)
head.penup()
head.right(90)
head.forward(-120)
head.pendown()
head.color("white")
head.circle(10)
head.right(135)
head.color("black")
head.circle(5)
head.forward(10)
head.color("white")
head.circle(10)



#---------------------------------

#The first Half

import turtle
rainbow = ["red", "orange", "yellow", "green", "red"]
arc = turtle.Turtle()
arc.speed(0)
arc.width(60)
arc.penup()
arc.forward(-100)
arc.pendown()
x = 6
for color in rainbow:
    arc.color(color)
    for line in range(10):
        arc.forward(12)
        arc.right(x)
        arc.forward(15)
        
    #Retour à la ligne
    arc.penup()

    for line in range(10):
        arc.forward(-15)
        arc.right(-x+1)
        arc.forward(-15)
    arc.pendown()
arc.hideturtle()
#---------------------------------

#The second Half
import turtle
rainbow = ["red", "orange", "yellow", "green", "red"]
arc = turtle.Turtle()
arc.speed(0)
arc.width(60)
arc.penup()
arc.forward(100)
arc.pendown()
x = 6
for color in rainbow:
    arc.color(color)
    for line in range(10):
        arc.forward(-12)
        arc.right(-x)
        arc.forward(-15)
        
    #Retour à la ligne
    arc.penup()

    for line in range(10):
        arc.forward(15)
        arc.right(x-1)
        arc.forward(15)
    arc.pendown()
arc.hideturtle()
#---------------------------------
    
#The final balck line

import turtle
blackline = turtle.Turtle()
blackline.speed(0)
blackline.width(60)
blackline.penup()
blackline.forward(-100)
for line in [1,2,3,4]:
    for line in range(10):
        blackline.forward(12)
        blackline.right(6)
        blackline.forward(15)
       
        
    #At line

    for line in range(10):
        blackline.forward(-15)
        blackline.right(-5)
        blackline.forward(-15)
        
#Drawing the final line        
blackline.pendown()    

for line in range(10):
    blackline.color("red")
    blackline.forward(12)
    blackline.right(6)
    blackline.forward(15)  
arc.hideturtle()

#Eyes
     
import turtle
eyes = turtle.Turtle()
eyes.penup()
eyes.right(90)
eyes.forward(-128)
eyes.left(90)
eyes.pendown()
eyes.width(10)
eyes.circle(5)
eyes.forward(5)
eyes.penup()
eyes.forward(20)
eyes.pendown()
eyes.circle(5)
eyes.forward(5)
