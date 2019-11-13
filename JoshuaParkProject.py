#program files
import turtle
turtle.colormode(255)
bob = turtle.Turtle()
turtle.bgcolor("black")

bob.width(2)
bob.speed(15)

for times in range(250):
    c = (times*2,135,times*2)
    bob.color("blue")
    bob.circle(times*2)
    bob.left(20)

for times in range(200):
    bob.color("yellow")
    bob.circle(times*2) 









