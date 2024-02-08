import turtle

screen = turtle.Screen()
screen.bgcolor("black")
pen = turtle.Turtle()
pen.speed(0)  
def draw_heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.setheading(60)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()

# Function to write a message
def write_message(message):
    pen.up()
    pen.goto(0, -200)
    pen.color('white')
    pen.write(message, align='center', font=('Courier', 24, 'bold'))

# Draw heart
draw_heart()

# Write message
write_message("Happy Valentine's Day! AFREEN ")

# Hide the turtle and display the result
pen.hideturtle()
screen.mainloop()
