import cmath
import turtle
import time
turtle.setup(500, 500)
turtle.pensize(10)
turtle.color("blue")
#print(z)
#print(z.real)
#print(z.imag)
#print(z.conjugate())
#print(abs(z))
#print(cmath.sqrt(-1))
#print(cmath.phase(z))
#
#c = cmath.phase(complex(-1.0, 0.0))
#print(c)
#c = cmath.phase(complex(-1.0, -0.0))
#print(c)


def dessiner_n_uplets(n):
    turtle.up()
    Z = complex(1, 0)
    mod, arg = cmath.polar(Z)
    k=0
    a = complex(0, 2 * k * cmath.pi / n)
    z = mod * cmath.exp(a)
    turtle.goto(z.real * 100, z.imag * 100)
    turtle.down()
    for k in range(1, n+1):
        a = complex(0, 2 * k * cmath.pi / n)
        z = mod * cmath.exp(a)
        turtle.goto(z.real*100, z.imag*100)
    turtle.up()

def iterationTriangles(n):
    turtle.speed(1.5)
    for i in range(3, n+1):
        turtle.clear()
        dessiner_n_uplets(i)
        time.sleep(1)


def tourner(n, angle=0):
    turtle.up()
    Z = complex(1, 0)
    mod, arg = cmath.polar(Z)
    k = 0
    a = complex(0, angle + 2 * k * cmath.pi / n)
    z = mod * cmath.exp(a)
    turtle.goto(z.real * 100, z.imag * 100)
    turtle.down()
    for k in range(1, n + 1):
        a = complex(0, angle + 2 * k * cmath.pi / n)
        z = mod * cmath.exp(a)
        turtle.goto(z.real * 100, z.imag * 100)
    turtle.up()

def iterationTriangleRotation(n, iteration):
    turtle.speed('fastest')
    turtle.hideturtle()
    for i in range(n):
        turtle.clear()
        tourner(iteration, i*cmath.pi/10)
        #time.sleep(0.5)
#iteration(50)

iterationTriangleRotation(100, 3)


turtle.exitonclick()