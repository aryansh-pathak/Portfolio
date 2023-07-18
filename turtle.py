# Aryansh Pathak



import turtle

import random
from random import randint

#main function
def main():

  draw_background(t,s)

  draw_shape(t)

#defined all turtles and properties
t = turtle.Turtle() 
t2 = turtle.Turtle()
t3 = turtle.Turtle()
s = t.getscreen()
s.addshape("ezgif.com-gif-maker.gif")
t2.shape("ezgif.com-gif-maker.gif")
t.penup()
t.speed(0)
t2.speed(0)
t2.penup()
t2.goto(100,200)
t3.penup()
t3.speed(0)
t3.pencolor = "white"

#general rectangle function defined
def draw_rectangle(t, x, y, heading, pensize, line_color, fill_color, width, height):
 angle = 90
 t.penup()
 t.setheading(heading)
 t.pensize(pensize)
 t.goto(x, y)
 t.pencolor(line_color)
 t.pendown()
 t.fillcolor(fill_color)
 t.begin_fill()
 t.forward(height)
 t.left(angle)
 t.forward(width)
 t.left(angle)
 t.forward(height)
 t.left(angle)
 t.forward(width)
 t.end_fill()
 t.penup()

#general circle function defined
#moon
def draw_circle(t, x, y, heading, pensize, line_color, fill_color, radius, extent, steps):
  t.setheading(heading)
  t.pensize(pensize)
  t.goto(x,y)
  t.pencolor(line_color)
  t.pendown()
  t.fillcolor(fill_color)
  t.begin_fill()
  t.circle(radius) 
  t.end_fill()
  t.penup()

#general triangle function defined
def draw_triangle(t, x, y, heading, pensize, line_color, fill_color, angle, side_length):
  t.setheading(heading)
  t.pensize(pensize)
  t.goto(x,y)
  t.pendown()
  t.pencolor(line_color)
  t.fillcolor(fill_color)
  t.begin_fill()
  for i in range(3):
    t.forward(side_length)
    t.left(angle)
  t.end_fill() 
  t.penup()

#mountains called through the triangle function
#mountains
def draw_mountains(t):
  draw_triangle(t,-250,60,0,10,"White","#523A28",120,80)
  draw_triangle(t,-170,60,0,10,"White","#523A28",120,60)
  draw_triangle(t,-110,60,0,10,"White","#523A28",120,75)
  draw_triangle(t,-35,60,0,10,"White","#523A28",120,100)
  draw_triangle(t,65,60,0,10,"White","#523A28",120,85)
  draw_triangle(t,150,60,0,10,"White","#523A28",120,90)

#moon called through the circle function
def draw_moon(t):
  draw_circle(t,200,180,20,20,"Beige","Beige",25,None,None)

#draw shape function for the houses
def draw_shape(t):
  #drawhouse1
  #drawroof
  draw_triangle (t,-195,6,0,2,"White","Orange",120,50)
  #drawrectangle1
  draw_rectangle (t, -190, -50, 0, 10, "white", "white",50, 40)
  draw_rectangle (t, -180, -50, 0, 5, "black","black", 25, 15)
  #drawhouse2
  #drawroof
  draw_triangle (t,0,-5,0,2,"White","Purple",120,50)
  #drawrectangle2
  draw_rectangle (t, 5, -60, 0, 10, "white", "white",50, 40)
  draw_rectangle (t, 15, -60, 0, 5, "black","black", 25, 15)
  #drawhouse3
  #draw_roof
  draw_triangle (t,-100,-25,0,2,"White","Red",120,50)
  #drawrectangle3
  draw_rectangle (t, -95, -80, 0, 10, "white", "white",50, 40)
  draw_rectangle (t, -85, -80, 0, 5, "black","black", 25, 15)
  #drawhouse4
  #draw_roof
  draw_triangle (t,145,-25,0,2,"White","Lime",120,50)
  #drawrectangle4
  draw_rectangle (t, 150, -81, 0, 10, "white", "white",50, 40)
  draw_rectangle (t, 160, -81, 0, 5, "black","black", 25, 15)

#star function defined
def draw_star(t3, x, y, heading, pensize):
  t3.penup()
  t3.setheading(heading)
  #t3.line_color(line_color)
  #t3.fill_color(fill_color)
  turns = 5
  t3.begin_fill()
  t3.pendown()
  t3.end_fill()
  while turns > 0:
    t3.forward(25)
    t3.left(145)
    turns = turns - 1
  t3.end_fill()
  num_stars = 0
  while num_stars < 10:
    x = randint(-200,200)
    y = randint(100,300)
    t3.penup()
    t3.goto(x,y)
    t3.speed(0)
    t3.pendown()
    num_stars = num_stars + 1


#background function defined
def draw_background(t,s):
  s.setup(width=500, height=500)
  s.bgcolor("#05263B")
  draw_mountains(t)
  draw_moon(t)
 #conditional expressions
 #random integers
 #background loop
  turns = 5 
  t3.begin_fill()
  while turns > 0:
    t3.forward(25)
    t3.left(145)
    turns = turns - 1
  t3.end_fill()
  num_stars = 0
  while num_stars < 30:
    x = randint(-500,500)
    y = randint(100,200)
    t3.penup()
    t3.goto(x,y)
    t3.pendown()
    num_stars = num_stars + 1
    draw_star(t3,x,y,0,10)

#Name and UIN
t.write
t.goto(-275, 225)
t.pencolor("white")
t.write("UIN: 674665754 Name: Aryansh Pathak", font=('arial', 13, 'normal'))

#main function
main()
