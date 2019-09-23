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
        turtle.color(color)
        turtle.begin_fill()
        turtle.rt(tilt)
        turtle.rt(90)
        turtle.fd(size)
        turtle.rt(90)
        turtle.fd(size)
        turtle.rt(90)
        turtle.fd(size)
        turtle.rt(90)
        turtle.fd(size)
        turtle.end_fill()
        return (0)
pass
#todo:(zhuravlev aleksandr) make sqare drawing function
pass
def triangle_regular(x,y,size,color,tilt):
#todo:(Starnovskiy Sergey) make triangle drawing function
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(color)
        turtle.begin_fill()
        turtle.rt(tilt)
        turtle.fd(size)
        turtle.rt(90)
        turtle.fd(size)
        turtle.rt(135)
        turtle.fd(size)
        turtle.end_fill()
        return (0)
pass
def Parallelogram(x,y,size,color,tilt):
#todo:(Drachev Nikita) make Parallelogram drawing function
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(color)
        turtle.begin_fill()
        turtle.rt(tilt)
        turtle.rt(45)
        turtle.fd(size)
        turtle.rt(45)
        turtle.fd(size)
        turtle.rt(135)
        turtle.fd(size)
        turtle.rt(45)
        turtle.fd(size)
        turtle.end_fill()
        return (0)
pass



def Helicopter():
 square(0,0,20,"orange",315)
 triangle_regular(53,-22,30,"pink", 180)
 triangle_regular(35,-45,30,"purple", 314)
 triangle_regular(95,-55,50,"yellow", 45)
 triangle_regular(97,15,50,"red", 315)
 triangle_regular(37,15,40,"blue", 45)
 Parallelogram(97,15,30,"green",90)


pass
Helicopter()