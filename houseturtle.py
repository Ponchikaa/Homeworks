from turtle import *
import turtle

#cube
width(20)
color("red")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)


#doorofcube

left(90)
forward(75)
width(5)
color("purple")
left(90)
forward(75)
right(90)
forward(50)
right(90)
forward(75)

penup()
left(90)
forward(75)
left(90)
forward(200)
pendown()
width(10)
left(40)
forward(150)
left(95)
forward(150)
width(5)
penup()
left(90)
forward(80)
left(45)
pendown()
forward(50)
right(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)

penup()
shape("turtle")
right(90)
forward(400)
right(90)
forward(100)
right(90)
forward(350)
right(90)

turtle.write("I'm Home :)" , font=("Verdana",20, "normal") )



exitonclick()