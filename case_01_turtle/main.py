## Case-study #1
# Developers:   Zhuravlev Aleksandr (),
#               Starnovskiy Sergey (),
#                Drachev Nikita().
import turtle
def square(x, y, size, tilt):
#todo:(zhuravlev aleksandr) make sqare drawing function
    turtle.penup()
    turtle.goto(x,y)
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
def triangle_regular(x, y, size, color, tilt):
#todo:(Starnovskiy Sergey) make triangle drawing function
    pass
def circle(x, y, size, color):
#todo:(Drachev Nikita) make circle drawing function
    pass


