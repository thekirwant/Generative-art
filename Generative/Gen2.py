from turtle import *
from Color import set_theme
import random

def draw_square(x,y,s):
    penup()
    goto(x-s/2, y-s/2)
    pendown()
    for i in range (4):
        forward(s)
        left(90)


set_theme(thickness=3)

noise = 5
size = 100
shrink = 15
for x in range(-500+size//2, 500, size):
    for y in range(-500+size//2, 500, size):
        #cuadrado más externo
        draw_square(x,y,size)

        #determinar compensasiones
        x_off=random.uniform(-noise, noise)
        y_off = random.uniform(-noise, noise)

        #dibujar los cuadrados internos
        for i in range (6):
            draw_square(x+i*x_off, y+i*y_off, size-i*shrink)




tracer (True)

exitonclick()