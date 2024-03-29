## Case-study #1
# Developers:   Zhuravlev Aleksandr (30),
#               Starnovskiy Sergey (50),
#                Drachev Nikita(30).
import turtle
import time
def square(x, y, size,color, tilt):

    #function drawing square
    #param x: first coordinate of left angle
    #:param y: second coordinate of left angle
    #:param size: length of sides
    #:param color: color of figure
    #:param tilt: incline of figure
    #:return:

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

def hare():
    triangle_regular(300,0,50,'red',90)
    square(302,10,20,'orange',315)
    Parallelogram(312,12,20,'lightgreen',225)
    triangle_regular(302,-40,20,'pink',0)
    triangle_regular(250,-102,50,'yellow',0)
    triangle_regular(288,-69,35,'lightblue',315)
    triangle_regular(317,-104,25,'purple',225)
    pass

def fish():
    triangle_regular(400,0,50,'red',0)
    square(420,-50,20,'orange',0)
    triangle_regular(450,-52,50,'yellow',225)
    triangle_regular(452,-25,35,'lightblue',90)
    Parallelogram(368,-28,30,'lightgreen',45)
    triangle_regular(390,-81,30,'pink',45)
    triangle_regular(388,-51,30,'purple',315)
    pass

def man1():
    #draws figure 4 from example
    square(0,50,35,'orange',45)
    turtle.up()

    triangle_regular(-50,-52,80,'red',165)
    Parallelogram(-80,-41,40,'lightgreen',90)
    triangle_regular(-24,-26,80,'yellow',255)
    triangle_regular(-22,-80,50,'cyan',30)
    triangle_regular(-24,-180,40,'violet',255)
    triangle_regular(-130, -129, 40, 'pink', 120)
    turtle.rt(225)
def hare():
    triangle_regular(0,0,50,'red',90)
    square(2,10,20,'orange',315)
    Parallelogram(12,12,20,'lightgreen',225)
    triangle_regular(2,-40,20,'pink',0)
    triangle_regular(-50,-102,50,'yellow',0)
    triangle_regular(-12,-69,35,'lightblue',315)
    triangle_regular(17,-104,25,'purple',225)
    pass

def man2():
    #draws figure 5 from example
    square(170, 50, 40, 'yellow', 45)
    triangle_regular(141,-55,70,'red',165)
    triangle_regular(70, 15, 70, 'orange', 165)
    Parallelogram(112,-122,40,'lightgreen',0)
    triangle_regular(191,-102,50,'lightblue',345)
    triangle_regular(175,-133,30,'violet',165)
    triangle_regular(120,-115,30,'pink',255)
def Helicopter():
    square(-450,0,20,"orange",315)
    triangle_regular(-397,-22,30,"pink", 180)
    triangle_regular(-415,-45,30,"purple", 314)
    triangle_regular(-355,-55,50,"yellow", 45)
    triangle_regular(-353,15,50,"red", 315)
    triangle_regular(-413,15,40,"blue", 45)
    Parallelogram(-353,15,30,"green",90)
    pass
def ship():
    Parallelogram(-200,0,30,"green",-45)
    triangle_regular(-122,0,30,"blue",-90)
    square(-119,47,32,"orange",315)
    triangle_regular(-165,3,29,"pink", 0)
    triangle_regular(-169,75,50,"red", 225)
    triangle_regular(-172,60,50,"yellow", -180)
    triangle_regular(-148,80,20,"purple", -135)
    pass
def main():
    turtle.setheading(0)
    hare()
    turtle.setheading(0)
    fish()
    turtle.setheading(0)
    ship()
    turtle.setheading(0)
    Helicopter()
    turtle.setheading(0)
    time.sleep(3)
main()
