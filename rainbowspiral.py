import turtle
t = turtle.Turtle()
s = turtle.Screen()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
s.bgcolor('black')
t.speed('fastest')
t.hideturtle()
while True:
   for X in range(200):
     t.pencolor(colors[X%len(colors)])
     t.width(X/100 + 1)
     t.left(59)
     t.forward(X)
   t.right(239)
   for X in range(200, 0, -1):
     t.pencolor('black')
     t.width(X/100 + 7)
     t.forward(X)
     t.right(59)