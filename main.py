from turtle import *
import math
tracer(0)
itterations = 8 #integer
def drawTriangle(x,y,size,uptriangle = True):
  up()
  goto(x,y)
  down()
  if(uptriangle!=-1):
    angle = 120
    setheading(120)
    for i in range(0,3):
      forward(size)
      right(angle)
  else:
    angle = 120
    setheading(90)
    pencolor("pink")
    forward(size/2)
    right(90)
    forward(size/2)
    setheading(180)
    pencolor("black")
    for i in range(0,3):
      forward(size)
      right(angle)
def triangleStarting():
  up()
  goto((triangleCorner[0][0],triangleCorner[0][1]))
  down()
  setheading(180)
  for i in range(3):
    forward(length)
    right(120)
draw = "normal"
if(draw == "normal"):
  length = 1000 # float
  length2 = length/2
  triangleCorner = [(length/2,-length/2)]
  triangleStarting()
  for i in range(0,itterations):
    for j in range(0,len(triangleCorner)):
      x,y = triangleCorner[j]
      drawTriangle(x-(length/2),y,length/2)
      triangleCorner.append((x-(length/2),y))
      relevent = y+math.sqrt(math.pow(0.5*length,2)-math.pow(0.25*length,2))
      triangleCorner.append((x-(length/4),relevent))
    length = length/2
  length = length2*2
  triangleCorner = [((length),(-length/2))]
  length = length2 # float
  triangleStarting()
  for i in range(0,itterations):
    for j in range(0,len(triangleCorner)):
      x,y = triangleCorner[j]
      drawTriangle(x-(length/2),y,length/2)
      triangleCorner.append((x-(length/2),y))
      relevent = y+math.sqrt(math.pow(0.5*length,2)-math.pow(0.25*length,2))
      triangleCorner.append((x-(length/4),relevent))
    length = length/2
else:
  #only draw in the middle triangles
  length = 500 # float
  length2 = length/2
  triangleCorner = [[length/2,-length/2,1]]
  triangleStarting()
  for i in range(0,itterations):
    for j in range(0,len(triangleCorner)):
      x,y,UpOrDown = triangleCorner[j]
      if(UpOrDown):
        drawTriangle(x,y,length/2,UpOrDown)
      triangleCorner.append([x,y+length/2,UpOrDown*-1])
      relevent = y+math.sqrt(math.pow(0.5*length,2)-math.pow(0.25*length,2))
    length = length/2
hideturtle()
update()
exitonclick()