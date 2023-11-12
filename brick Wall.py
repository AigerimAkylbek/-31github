import turtle

def drawsquare(Height):
    turtle.pendown()
    for i in range (4):
        turtle.forward(Height)
        turtle.right(90)

def drawrectangle(Length, Height):
    turtle.pendown
    for i in range (2):
        turtle.forward(Length)
        turtle.right(90)
        turtle.forward(Height)
        turtle.right(90)
    
def drawRowofBricks(numbricks, Length, Height):
    x = turtle.xcor()
    for i in range(numbricks):
        drawrectangle(Length, Height)
        turtle.setx(turtle.xcor() + Length)
    
def drawOffSetBricks(numbricks, Length, Height):
    x = turtle.xcor()
    drawsquare(Height)
    turtle.setx(turtle.xcor()+  Height)
    for i in range (0,numbricks-1):
        drawrectangle(Length,Height)
        turtle.setx(turtle.xcor()+ Length)
    drawsquare(Height)

def colms(ncolms,numbricks,Length, Height):
    x = turtle.xcor()
    y = turtle.ycor()
    for i in range(ncolms):
        if i%2==0:
            drawRowofBricks(numbricks, Length,Height)
            turtle.penup()
            turtle.sety(turtle.ycor()+Height)
            turtle.setx(0)
            turtle.pendown()
        else:
            drawOffSetBricks(numbricks,Length, Height)
            turtle.penup()
            turtle.sety(turtle.ycor()+Height)
            turtle.setx(0)
            turtle.pendown()
        turtle.penup()

def main():
    ncolms = 10
    numbricks = 5
    Height = 25
    Length = 50
    colms(ncolms, numbricks,Length,Height)

main()
turtle.done()