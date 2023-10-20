import turtle
import time

posponer= 0.1

 
wn = turtle.Screen()

wn.title("Juego")
wn.bgcolor("black")
wn.setup(width= 600, height= 600)
wn.tracer(0)


#cabeza de serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#funciones

def arriba():
    cabeza.direction = "up"

def arriba():
    cabeza.direction = "down"    

def arriba():
    cabeza.direction = "left"

def arriba():
    cabeza.direction = "right"


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)        

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")


while True:
    wn.update()

    mov()
    time.sleep(posponer)
   










