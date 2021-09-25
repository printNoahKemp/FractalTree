import turtle
import random

'''Screen size (400,300)'''
turtle.setup(790,600)
turtle.speed(0)
turtle.delay(0)
turtle.ht()
#turtle.tracer(0,0)

'''Draw'''
def Draw():
    '''Setup'''
    turtle.bgcolor('black')
    turtle.pencolor('white')
    turtle.Screen().colormode(255)
    turtle.left(90)
    turtle.penup()
    turtle.setpos(0,-250)
    turtle.pendown()
    turtle.pensize(1)

    '''Branch'''
    Branch(120)

    '''End turtle'''
    #turtle.update()
    #turtle.tracer(2,2)
    turtle.done()

'''Branch'''
def Branch(steps):
    if steps > 20:
        turtle.forward(steps)
        turtle.right(30)
        Branch(steps*0.8)
        turtle.left(30)
        Branch(steps*0.8)
        turtle.left(30)
        Branch(steps*0.8)
        turtle.right(30)
        turtle.penup()
        turtle.backward(steps)
        turtle.pendown()

'''Run'''
if __name__ =="__main__":
    Draw()