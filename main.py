
import turtle
import time
#variables
size = 65
sides =int(input("number from 3 to 10:\t"))
angle = 360/sides
color = "teal"

#define function
def drw_poly():
    turtle.color(color)
    #outline color
    turtle.begin_fill()

    for i in  range(sides):

        turtle.forward(size)
        turtle.left(angle)


    for i in range(sides):


        turtle.forward(size)
        turtle.left(angle)
        turtle.penup()
        turtle.goto(-130, 0)
        turtle.pendown()
    #fill color
    turtle.end_fill()
    turtle.hideturtle()

    #maintain screen after execution
    turtle.mainloop()


#call function
if (sides >=3 and sides<=10):
    drw_poly()
else:
    print("sides cannot be out of range")