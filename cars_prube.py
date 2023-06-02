import tkinter as tk
import random

class Carrera:
    def __init__(self, ventana, longitud_pista, num_corredores):
        self.ventana = ventana
        self.ventana.title("Carrera de Tortugas")
        self.canvas = tk.Canvas(ventana, width=600, height=400)
        self.canvas.pack()
        self.longitud_pista = longitud_pista
        self.num_corredores = num_corredores
        self.corredores = []
        self.finalizado = False

        self.dibujar_pista()
        self.crear_corredores()

    def dibujar_pista(self):
        self.canvas.create_line(50, 50, 50, 350)  # Línea de salida
        self.canvas.create_line(550, 50, 550, 350)  # Línea de meta

    def crear_corredores(self):
        colores = ["red", "green", "blue", "orange", "purple", "yellow"]
        distancia_entre_corredores = 300 / (self.num_corredores + 1)
        y = 50 + distancia_entre_corredores

        for i in range(self.num_corredores):
            tortuga = self.canvas.create_image(50, y, anchor=tk.NW, image=tortuga_imagen)
            self.corredores.append(tortuga)
            self.canvas.create_text(570, y, anchor=tk.W, text=f"Corredor {i+1}", fill=colores[i % len(colores)])
            y += distancia_entre_corredores

    def correr(self):
        while not self.finalizado:
            for i, corredor in enumerate(self.corredores):
                distancia_avance = random.randint(1, 10)
                self.canvas.move(corredor, distancia_avance, 0)
                x1, y1, x2, y2 = self.canvas.bbox(corredor)

                if x2 >= 550:
                    self.finalizado = True
                    self.mostrar_resultado(i+1)
                    break

            self.canvas.update()
            self.canvas.after(100)

    def mostrar_resultado(self, corredor_ganador):
        self.canvas.create_text(300, 200, text=f"¡El corredor {corredor_ganador} ha ganado!", font=("Arial", 20), fill="black")

# Crear la ventana principal
ventana = tk.Tk()

# Cargar imagen de tortuga
tortuga_imagen = tk.PhotoImage(file="img/nave2.png")

# Crear una instancia de la carrera
carrera = Carrera(ventana, 500, 6)

# Agregar un botón para comenzar la carrera
boton_carrera = tk.Button(ventana, text="¡Comenzar Carrera!", command=carrera.correr)
boton_carrera.pack()

# Ejecutar la ventana principal
ventana.mainloop()