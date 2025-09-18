from turtle import *

speed(13)
itterations = 30
def drawItteration():
  pass
def drawTriangle(size):
  angle = 120
  setheading(120)
  for i in range(0,3):
    forward(size)
    right(angle)
up()
goto(200,-100)
down()
left(90)
setheading(180)
length = 500
for i in range(0,3):
    forward(length)
    right(120)
#((x1 + x2) / 2, (y1 + y2) / 2)
listOftriangles = [[(xcor(),ycor()),(xcor()-length,ycor()),(xcor()-(length/2),ycor()+(((length**2-((length/2)**2)))**(1/2)))]]
print(listOftriangles)
fillcolor("red")
pencolor("red")
for i in range(0,len(listOftriangles[0])):
  goto(listOftriangles[0][i][0],listOftriangles[0][i][1])
goto(listOftriangles[0][0][0],listOftriangles[0][0][1])
for k in range(0,itterations):
  for j in range(0,len(listOftriangles)):
    for i in range(0,len(listOftriangles[j])):
      x1,y1 = listOftriangles[j][i]
      x2 = listOftriangles[j][i][0]-length
      y2 = listOftriangles[j][i][1]
      up()
      goto((x1 + x2) / 2, (y1 + y2) / 2)
      down()
      drawTriangle(length/2)
      listOftriangles.append([(xcor(),ycor()),(xcor()-(length/2),ycor()),(xcor()-(length/4),ycor()-((((length/2)**2-((length/4)**2)))**(1/2)))])
  for p in range(0,j):
    listOftriangles.pop(j)
  length = length/2
exitonclick()