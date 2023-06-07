from turtle import *
from Color import set_theme
import random


#s es el tamaño
#l es el nivel de recursión

def tiling(x,y,s,l, mode = "straight"):
    #se alcanzó el nivel final
    #de recursión
    if l == 0:

        if mode == "straight":
            if random.random()<0.5:
                #vertical
                penup()
                goto(x,y-s)
                pendown()
                goto(x,y+s)

            else:
                #horizontal
                penup()
                goto(x-s,y)
                pendown()
                goto(x+s,y)

        elif mode =="diagonal":
            #  esquina sup. izquierda 
            if random.random()<0.5:
                
                penup()
                goto(x-s,y+s)
                pendown()
                goto(x+s,y-s)

            else:
            #esquina inferior izquierda
                penup()
                goto(x-s,y-s)
                pendown()
                goto(x+s,y+s)            

    else:
        
        s /=2
        l -= 1
        tiling(x-s,y+s,s,l, mode)
        tiling(x+s,y+s,s,l, mode)
        tiling(x-s,y-s,s,l, mode)
        tiling(x+s,y-s,s,l, mode)

set_theme(canvas_width=500, canvas_height=500,thickness=3)
tiling(0,0,400,4, mode ="diagonal" )
tracer(True)
exitonclick()