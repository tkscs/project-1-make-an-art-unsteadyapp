from turtle import *
import math
tracer(0)
itterations = 4
def drawTriangle(x,y,size):
  up()
  goto(x,y)
  down()
  angle = 120
  setheading(120)
  for i in range(0,3):
    forward(size)
    right(angle)
#triangleStarting
up()
goto(200,-100)
down()
length = 500
setheading(180)
for i in range(3):
  forward(length)
  right(120)
triangleCorner = [(200,-100)]
for i in range(0,itterations):
  for j in range(0,len(triangleCorner)):
    x,y = triangleCorner[j]
    drawTriangle(x-(length/2),y,length/2)
    triangleCorner.append((x-(length/2),y))
    relevent = y+math.sqrt(math.pow(0.5*length,2)-math.pow(0.25*length,2))
    triangleCorner.append((x-(length/4),relevent))
  length = length/2
update()
exitonclick()