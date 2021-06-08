"""
@author: GSS
"""
import turtle
from time import sleep
ch=turtle.Turtle()
turtle.colormode(255)
wn = turtle.Screen()
wn.title("Chrome LOGO")
r=120
ch.speed(2)
ch.seth(-150)
ch.up()


# Red Part
ch.color(219, 50, 54)
ch.begin_fill()
ch.fd(r)
ch.down()
ch.right(90)
ch.circle(-r, 120)
ch.fd(r*3**.5)
ch.left(120)
ch.circle(2*r, 120)
ch.left(60)
ch.fd(r*3**.5)
ch.end_fill()


#  Green Part
ch.left(180)
ch.color(60, 186, 84)
ch.begin_fill()
ch.fd(r*3**.5)
ch.left(120)
ch.circle(2*r, 120)
ch.left(60)
ch.fd(r*3**.5)
ch.left(180)
ch.circle(-r, 120)
ch.end_fill()


#  Yellow Part
ch.left(180)
ch.circle(r, 120)
ch.color(244, 194, 13)
ch.begin_fill()
ch.circle(r, 120)
ch.right(180)
ch.fd(r*3**.5)
ch.right(60)
ch.circle(-2*r, 120)
ch.right(120)
ch.fd(r*3**.5)
ch.end_fill()


#  Blue Part
ch.up()
ch.left(90)
ch.fd(r/20)
ch.seth(60)
ch.color(72, 133, 237)
ch.down()
ch.begin_fill()
ch.circle(ch.distance(0,0))
ch.end_fill()
ch.ht()
sleep(0.8)

turtle.done()
