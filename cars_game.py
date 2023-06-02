from tkinter import *
import random

#---------------------
# VARIABLES GLOBALES
#--------------------

BASE = 1060
ALTURA = 360

#--------------------
# VENTANA PRINCIPAL
#--------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("1100x400")
ventana_principal.config(bg="white")

#----------------------
# Frame de graficacion
#----------------------

frame_graficacion = Frame(ventana_principal)    
frame_graficacion.config(bg="red", width=1080, height=380)
frame_graficacion.place(x=10, y=10)

# creacion canvas 

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="ivory4")
c.place(x=10, y=10)

# Variables creación lineas de salida
x = 130
y = 0

# linea de salida

c.create_rectangle(x + 60, y + 360, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 360, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 360, x + 20, y + 20, fill="black")

c.create_rectangle(x + 60, y + 340, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 340, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 340, x + 20, y + 20, fill="white")

c.create_rectangle(x + 60, y + 320, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 320, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 320, x + 20, y + 20, fill="black")

c.create_rectangle(x + 60, y + 300, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 300, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 300, x + 20, y + 20, fill="white")

c.create_rectangle(x + 60, y + 280, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 280, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 280, x + 20, y + 20, fill="black")

c.create_rectangle(x + 60, y + 260, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 260, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 260, x + 20, y + 20, fill="white")

c.create_rectangle(x + 60, y + 240, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 240, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 240, x + 20, y + 20, fill="black")

c.create_rectangle(x + 60, y + 220, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 220, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 220, x + 20, y + 20, fill="white")

c.create_rectangle(x + 60, y + 200, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 200, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 200, x + 20, y + 20, fill="black")

c.create_rectangle(x + 60, y + 180, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 180, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 180, x + 20, y + 20, fill="white")

c.create_rectangle(x + 60, y + 160, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 160, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 160, x + 20, y + 20, fill="black")

c.create_rectangle(x + 60, y + 140, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 140, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 140, x + 20, y + 20, fill="white")

c.create_rectangle(x + 60, y + 120, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 120, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 120, x + 20, y + 20, fill="black")

c.create_rectangle(x + 60, y + 100, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 100, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 100, x + 20, y + 20, fill="white")

c.create_rectangle(x + 60, y + 80, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 80, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 80, x + 20, y + 20, fill="black")

c.create_rectangle(x + 60, y + 60, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 60, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 60, x + 20, y + 20, fill="white")

c.create_rectangle(x + 60, y, x + 20, y + 20, fill="black")
c.create_rectangle(x, y, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y, x + 20, y + 20, fill="white")

c.create_rectangle(x + 60, y + 40, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 40, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 40, x + 20, y + 20, fill="black")

# Variables creación lineas de salida
x = 960
y = 0

c.create_rectangle(x + 105, y + 360, x + 20, y + 20, fill="white")
c.create_rectangle(x + 80, y + 360, x + 20, y + 20, fill="black")
c.create_rectangle(x + 60, y + 360, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 360, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 360, x + 20, y + 20, fill="black")

c.create_rectangle(x + 105, y + 340, x + 20, y + 20, fill="black")
c.create_rectangle(x + 80, y + 340, x + 20, y + 20, fill="white")
c.create_rectangle(x + 60, y + 340, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 340, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 340, x + 20, y + 20, fill="white")

c.create_rectangle(x + 105, y + 320, x + 20, y + 20, fill="white")
c.create_rectangle(x + 80, y + 320, x + 20, y + 20, fill="black")
c.create_rectangle(x + 60, y + 320, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 320, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 320, x + 20, y + 20, fill="black")

c.create_rectangle(x + 105, y + 300, x + 20, y + 20, fill="black")
c.create_rectangle(x + 80, y + 300, x + 20, y + 20, fill="white")
c.create_rectangle(x + 60, y + 300, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 300, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 300, x + 20, y + 20, fill="white")

c.create_rectangle(x + 105, y + 280, x + 20, y + 20, fill="white")
c.create_rectangle(x + 80, y + 280, x + 20, y + 20, fill="black")
c.create_rectangle(x + 60, y + 280, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 280, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 280, x + 20, y + 20, fill="black")

c.create_rectangle(x + 105, y + 260, x + 20, y + 20, fill="black")
c.create_rectangle(x + 80, y + 260, x + 20, y + 20, fill="white")
c.create_rectangle(x + 60, y + 260, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 260, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 260, x + 20, y + 20, fill="white")

c.create_rectangle(x + 105, y + 240, x + 20, y + 20, fill="white")
c.create_rectangle(x + 80, y + 240, x + 20, y + 20, fill="black")
c.create_rectangle(x + 60, y + 240, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 240, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 240, x + 20, y + 20, fill="black")

c.create_rectangle(x + 105, y + 220, x + 20, y + 20, fill="black")
c.create_rectangle(x + 80, y + 220, x + 20, y + 20, fill="white")
c.create_rectangle(x + 60, y + 220, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 220, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 220, x + 20, y + 20, fill="white")

c.create_rectangle(x + 105, y + 200, x + 20, y + 20, fill="white")
c.create_rectangle(x + 80, y + 200, x + 20, y + 20, fill="black")
c.create_rectangle(x + 60, y + 200, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 200, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 200, x + 20, y + 20, fill="black")

c.create_rectangle(x + 105, y + 180, x + 20, y + 20, fill="black")
c.create_rectangle(x + 80, y + 180, x + 20, y + 20, fill="white")
c.create_rectangle(x + 60, y + 180, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 180, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 180, x + 20, y + 20, fill="white")

c.create_rectangle(x + 105, y + 160, x + 20, y + 20, fill="white")
c.create_rectangle(x + 80, y + 160, x + 20, y + 20, fill="black")
c.create_rectangle(x + 60, y + 160, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 160, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 160, x + 20, y + 20, fill="black")

c.create_rectangle(x + 105, y + 140, x + 20, y + 20, fill="black")
c.create_rectangle(x + 80, y + 140, x + 20, y + 20, fill="white")
c.create_rectangle(x + 60, y + 140, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 140, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 140, x + 20, y + 20, fill="white")

c.create_rectangle(x + 105, y + 120, x + 20, y + 20, fill="white")
c.create_rectangle(x + 80, y + 120, x + 20, y + 20, fill="black")
c.create_rectangle(x + 60, y + 120, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 120, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 120, x + 20, y + 20, fill="black")

c.create_rectangle(x + 105, y + 100, x + 20, y + 20, fill="black")
c.create_rectangle(x + 80, y + 100, x + 20, y + 20, fill="white")
c.create_rectangle(x + 60, y + 100, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 100, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 100, x + 20, y + 20, fill="white")

c.create_rectangle(x + 105, y + 80, x + 20, y + 20, fill="white")
c.create_rectangle(x + 80, y + 80, x + 20, y + 20, fill="black")
c.create_rectangle(x + 60, y + 80, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 80, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 80, x + 20, y + 20, fill="black")

c.create_rectangle(x + 105, y + 60, x + 20, y + 20, fill="black")
c.create_rectangle(x + 80, y + 60, x + 20, y + 20, fill="white")
c.create_rectangle(x + 60, y + 60, x + 20, y + 20, fill="black")
c.create_rectangle(x, y + 60, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y + 60, x + 20, y + 20, fill="white")

c.create_rectangle(x + 105, y, x + 20, y + 20, fill="black")
c.create_rectangle(x + 80, y, x + 20, y + 20, fill="white")
c.create_rectangle(x + 60, y, x + 20, y + 20, fill="black")
c.create_rectangle(x, y, x + 20, y + 20, fill="black")
c.create_rectangle(x + 40, y, x + 20, y + 20, fill="white")

c.create_rectangle(x + 105, y + 40, x + 20, y + 20, fill="white")
c.create_rectangle(x + 80, y + 40, x + 20, y + 20, fill="black")
c.create_rectangle(x + 60, y + 40, x + 20, y + 20, fill="white")
c.create_rectangle(x, y + 40, x + 20, y + 20, fill="white")
c.create_rectangle(x + 40, y + 40, x + 20, y + 20, fill="black")


ventana_principal.mainloop()