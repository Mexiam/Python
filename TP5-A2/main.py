from Circle import Circle
from Rectangle import Rectangle

print("---------------------------------------ex1-----------------------------------------------")
c = Circle(10, 50, 100)
print(f"x={c.getX()}, y={c.getY()}, radius={c.getRadius()}")

c.setX(20)
c.setY(30)
c.setRadius(200)

print(f"x={c.getX()}, y={c.getY()}, radius={c.getRadius()}")

print("---------------------------------------ex2-----------------------------------------------")

r = Rectangle(10, 50, 100, 200)
print(f"x={r.getX()}, y={r.getY()}, width={r.getWidth()}, height={r.getHeight()}")

r.setX(20)
r.setY(30)
r.setWidth(50)
r.setHeight(40)

print(f"x={r.getX()}, y={r.getY()}, width={r.getWidth()}, height={r.getHeight()}")

print("---------------------------------------ex3-----------------------------------------------")

#import turtle
#r.draw(turtle)
#c.draw(turtle)
#turtle.exitonclick()
#
#def drawShape(shapes, turtle):
#    for i in range(len(shapes)):
