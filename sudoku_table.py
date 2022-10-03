import turtle
def a():
  for i in range(10):
      if i % 3:
          turtle.width(1)
      elif i % 9:
          turtle.width(3)
      else:
          turtle.width(5)

      turtle.goto(0, 30*(9-i))
      turtle.goto(-270, 30*(9-i))
      turtle.goto(0, 30*(9-i))
def b():
    for i in range(10):
        if i % 3:
            turtle.width(1)
        elif i % 9:
            turtle.width(3)
        else:
            turtle.width(5)

        turtle.goto(-30*(9-i), 0)
        turtle.goto(-30*(9-i), 270)
        turtle.goto(-30*(9-i), 0)
turtle.speed(0)
a()
b()
d= input()