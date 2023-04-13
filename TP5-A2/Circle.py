from Shape import Shape

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.__radius = radius
    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius
    def draw(self, turtle):
        turtle.up()
        turtle.goto(self.getX(), self.getY() - self.getRadius())
        turtle.down()
        turtle.circle(self.getRadius())
        turtle.up()
