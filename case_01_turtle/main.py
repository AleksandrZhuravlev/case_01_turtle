## Case-study #1
# Developers:   Zhuravlev Aleksandr (),
#               Starnovskiy Sergey (),
#                Drachev Nikita().
import turtle
def square(x, y, size,color, tilt):
        # todo:(zhuravlev aleksandr) make sqare drawing function
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.rt(tilt)
        turtle.rt(90)
        turtle.fd(size)
        turtle.rt(90)
        turtle.fd(size)
        turtle.rt(90)
        turtle.fd(size)
        turtle.rt(90)
        turtle.fd(size)
        return (0)
pass
#todo:(zhuravlev aleksandr) make sqare drawing function
pass
def triangle_regular(x,y,size,color,tilt):
#todo:(Starnovskiy Sergey) make triangle drawing function
        turtle.penup()
        turtle.goto(x, y)
        turtle.fd(size/2)
        turtle.pendown()
        turtle.rt(tilt)
        turtle.rt(60)
        turtle.fd(size)
        turtle.rt(120)
        turtle.fd(size)
        turtle.rt(120)
        turtle.fd(size)
        return (0)
pass
def Parallelogram(x,y,size,color,tilt):
#todo:(Drachev Nikita) make Parallelogram drawing function
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.rt(tilt)
        turtle.rt(60)
        turtle.fd(size)
        turtle.rt(30)
        turtle.fd(size)
        turtle.rt(150)
        turtle.fd(size)
        turtle.rt(30)
        turtle.fd(size)
pass





