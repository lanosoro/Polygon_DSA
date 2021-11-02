import turtle as t
t.setup(800,600,200,200)
sides =int(input("number from 3 to 10:\t"))
#define function to draw polygon shape
def draw_shape(sides):
    t.pensize(1) #set weight of lines
    t.pencolor("black") #set color of pen
    for i in range(sides):
        t.left(360/sides) #determine the shape from user input
        t.fd(300/sides)
#declare starting point on for the turtle
x =-400
y = 200
    #sides =int(input("number from 3 to 10:\t"))

#iterate through the number of sides input by user
for i in reversed(range(2,sides+1)):
    if (sides >= 3 and sides <= 10):
        t.speed(0) #set the speed of the turtle
        t.up() #shift the pen to the starting point
        t.goto(x,y) #turtle stating point
        t.down() #first mark by turtle
        t.begin_fill() #fill the color of the shape
        t.fillcolor("teal") #select color
        draw_shape(i) #call draw function
        t.end_fill()
        t.hideturtle() #hide the turtle cursor
        x = x + 100 # space btwn the shapes
        print(x)
        if x > 400:
            x = x - 800
            y = y - 100
    else:
        print("sides cannot be out of range") #exeption for when the range is exceeded negatively or positively


t.done()