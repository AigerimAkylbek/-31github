import turtle

def drawSquare(size, x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    size = 42
    
def main():
    squareSize = int(input("Enter the size of the square:"))
    drawSquare(squareSize, y=100, x=-200)
    print (f"squareSize is still{squareSize}")

main()
turtle.done()