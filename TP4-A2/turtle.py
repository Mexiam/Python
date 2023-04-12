import turtle
turtle.setup(500, 500)


def dessiner_carre(x, y, c):


    turtle.up()
    turtle.goto(x-(1/2)*c, y-(1/2)*c)
    turtle.down()

    for i in range(4):
        turtle.forward(c)
        turtle.left(90)


def dessiner_cercle(x,y,r):
    turtle.up()
    turtle.goto(x, y-r)
    turtle.down()
    turtle.circle(r)


#dessiner_carre(100, 100, 20)
#dessiner_carre(0, 0, 60)

#dessiner_cercle(0, 0, 20)
#dessiner_cercle(0, 0, 60)
#dessiner_cercle(0, 0, 100)

dessiner_carre(0, 0, 100)
dessiner_cercle(0, 0, 50)


turtle.exitonclick()
