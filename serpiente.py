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
cabeza.direction = "left"

#funciones

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

    if cabeza.direction == "rigth":
        x = cabeza.xcor()
        cabeza.setx(x + 20)


while True:
    wn.update()

    mov()
    time.sleep(posponer)
   










