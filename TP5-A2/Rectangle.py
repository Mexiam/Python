from Shape import Shape

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__( x, y)
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def setWidth(self, width):
        self.__width = width
    def setHeight(self, height):
        self.__height = height
    def draw(self, turtle):
        turtle.up()
        turtle.goto(self.getX() - (1 / 2) * self.__width, self.getY() - (1 / 2) * self.getHeight())
        turtle.down()
        turtle.forward(self.__width)
        turtle.left(90)
        turtle.forward(self.__height)
        turtle.left(90)
        turtle.forward(self.__width)
        turtle.left(90)
        turtle.forward(self.__height)
        turtle.left(90)
        turtle.up()

