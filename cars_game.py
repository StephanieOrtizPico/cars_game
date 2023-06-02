from tkinter import *
from tkinter import messagebox
import random

#---------------------
# VARIABLES GLOBALES
#--------------------

BASE = 1060
ALTURA = 360

#--------------------
# FUNCIONES DE LA APP
#--------------------

# salir
def salir():
    messagebox.showinfo("Plataforma Guanentá 2.0", "La app se va a cerrar")
    ventana_principal.destroy()

#--------------------
# VENTANA PRINCIPAL
#--------------------

ventana_principal = Tk()
ventana_principal.title("Carrera 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("1100x500")
ventana_principal.config(bg="white")

#----------------------
# Frame de graficacion
#----------------------

frame_graficacion = Frame(ventana_principal)    
frame_graficacion.config(bg="red", width=1080, height=380)
frame_graficacion.place(x=10, y=10)

#----------------------
# Frame de controles
#----------------------

frame_controles = Frame(ventana_principal)    
frame_controles.config(bg="red", width=1080, height=90)
frame_controles.place(x=10, y=400)

#--------------------------------
# barra menu
#--------------------------------
barra_menu = Menu()
ventana_principal.config(menu=barra_menu)

menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Salir", menu=menu_salir)

# creacion canvas 

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="ivory4")
c.place(x=10, y=10)

# Linea divisoria

c.create_line(0, 180, 960, 180, width=8, fill="white")
c.create_line(0, 180, 930, 180, width=8, fill="red")
c.create_line(0, 180, 900, 180, width=8, fill="white")
c.create_line(0, 180, 870, 180, width=8, fill="red")
c.create_line(0, 180, 840, 180, width=8, fill="white")
c.create_line(0, 180, 810, 180, width=8, fill="red")
c.create_line(0, 180, 780, 180, width=8, fill="white")
c.create_line(0, 180, 750, 180, width=8, fill="red")
c.create_line(0, 180, 720, 180, width=8, fill="white")
c.create_line(0, 180, 690, 180, width=8, fill="red")
c.create_line(0, 180, 660, 180, width=8, fill="white")
c.create_line(0, 180, 630, 180, width=8, fill="red")
c.create_line(0, 180, 600, 180, width=8, fill="white")
c.create_line(0, 180, 570, 180, width=8, fill="red")
c.create_line(0, 180, 540, 180, width=8, fill="white")
c.create_line(0, 180, 510, 180, width=8, fill="red")
c.create_line(0, 180, 480, 180, width=8, fill="white")
c.create_line(0, 180, 450, 180, width=8, fill="red")
c.create_line(0, 180, 420, 180, width=8, fill="white")
c.create_line(0, 180, 390, 180, width=8, fill="red")
c.create_line(0, 180, 360, 180, width=8, fill="white")
c.create_line(0, 180, 330, 180, width=8, fill="red")
c.create_line(0, 180, 300, 180, width=8, fill="white")
c.create_line(0, 180, 270, 180, width=8, fill="red")
c.create_line(0, 180, 240, 180, width=8, fill="white")
c.create_line(0, 180, 210, 180, width=8, fill="red")
c.create_line(0, 180, 180, 180, width=8, fill="white")
c.create_line(0, 180, 150, 180, width=8, fill="red")
c.create_line(0, 180, 120, 180, width=8, fill="white")
c.create_line(0, 180, 90, 180, width=8, fill="red")
c.create_line(0, 180, 60, 180, width=8, fill="white")
c.create_line(0, 180, 30, 180, width=8, fill="red")

# Lineas adicionales

c.create_line(0, 170, 1060, 170, width=4, fill="yellow")
c.create_line(0, 190, 1060, 190, width=4, fill="yellow")
c.create_line(0, 8, 1060, 8, width=4, fill="yellow")
c.create_line(0, 354, 1060, 354, width=4, fill="yellow")

# Lineas punteadas del piso, pista 1

c.create_line(230, 90, 270, 90, width=3, fill="white")
c.create_line(310, 90, 350, 90, width=3, fill="white")
c.create_line(390, 90, 430, 90, width=3, fill="white")
c.create_line(470, 90, 510, 90, width=3, fill="white")
c.create_line(550, 90, 590, 90, width=3, fill="white")
c.create_line(630, 90, 670, 90, width=3, fill="white")
c.create_line(710, 90, 750, 90, width=3, fill="white")
c.create_line(790, 90, 830, 90, width=3, fill="white")
c.create_line(870, 90, 910, 90, width=3, fill="white")

# Lineas punteadas del piso, pista 2

c.create_line(230, 270, 270, 270, width=3, fill="white")
c.create_line(310, 270, 350, 270, width=3, fill="white")
c.create_line(390, 270, 430, 270, width=3, fill="white")
c.create_line(470, 270, 510, 270, width=3, fill="white")
c.create_line(550, 270, 590, 270, width=3, fill="white")
c.create_line(630, 270, 670, 270, width=3, fill="white")
c.create_line(710, 270, 750, 270, width=3, fill="white")
c.create_line(790, 270, 830, 270, width=3, fill="white")
c.create_line(870, 270, 910, 270, width=3, fill="white")

# Variables creación linea de salida
x = 130
y = 0

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

# Variables creación linea de meta
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

# boton play
bt_play = Button(frame_controles,text="Play")
bt_play.place(x=500, y=30, width=100, height=30)


ventana_principal.mainloop()