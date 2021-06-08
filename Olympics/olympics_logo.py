"""
@author: GSS
"""
import turtle

 
wn = turtle.Screen()
wn.title("Olympics LOGO")

olymp = turtle.Turtle()
olymp.pensize(6) 
firstRowColors = ["blue", "black", "red"] 
for i in range(3):
  olymp.penup()
  olymp.pencolor(firstRowColors[i])
  olymp.goto(i*110, 0)
  olymp.pendown()
  olymp.circle(50)
 
secondRowColors = ["", "yellow", "", "green"]
for i in range(1, 4, 2):
  olymp.penup()
  olymp.pencolor(secondRowColors[i])
  olymp.goto(i*55, -50)
  olymp.pendown()
  olymp.circle(50)
  
turtle.done()