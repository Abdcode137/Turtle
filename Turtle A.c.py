import turtle

turtle.Screen().bgcolor("Orange")

board = turtle.Turtle()

board.forward(100)
board.right(90)
board.forward(100)
board.right(90)
board.forward(100)
board.right(90)
board.forward(100)

board.penup()
board.forward(120)
board.right(90)

board.pendown()

board.right(120)
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
turtle.done()