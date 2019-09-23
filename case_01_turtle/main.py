## Case-study #1
# Developers:   Zhuravlev Aleksandr (),
#               Starnovskiy Sergey (),
#                Drachev Nikita().
import turtle
import time
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
        turtle.rt(60)
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

def man2():
    #draws figure 5 from example
    square(170, 50, 40, 'yellow', 45)
    triangle_regular(141,-55,70,'red',165)
    triangle_regular(70, 15, 70, 'orange', 165)
    Parallelogram(112,-122,40,'lightgreen',0)
    triangle_regular(191,-102,50,'lightblue',345)
    triangle_regular(175,-133,30,'violet',165)
    triangle_regular(120,-115,30,'pink',255)
def main():
    man1()
    man2()
    hare()
    fish()
    time.sleep(3)
main()