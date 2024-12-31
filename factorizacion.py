# Patricia Zaragoza Palma 
# ingeniería en sistemas computacionales 
import sympy as sp
import tkinter as tk
from tkinter import messagebox

# Función para factorizar la ecuación
def factorizar_ecuacion():
    ecuacion_str = entrada_ecuacion.get()
    try:
        # Definir la variable simbólica
        x = sp.symbols('x')
        # Convertir la entrada en una expresión simbólica
        ecuacion = sp.sympify(ecuacion_str)
        # Factorizar la ecuación
        factorizacion = sp.factor(ecuacion)
        # Mostrar el resultado en un formato legible
        resultado = sp.pretty(factorizacion)
        # Actualizar la etiqueta con el resultado
        salida_factorizacion.config(text=f"Factorización: {resultado}")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al factorizar la ecuación: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Factorización de Ecuaciones")

# Crear y colocar los elementos de la interfaz
etiqueta_ecuacion = tk.Label(ventana, text="Introduce la ecuación a factorizar:")
etiqueta_ecuacion.pack()

entrada_ecuacion = tk.Entry(ventana, width=40)
entrada_ecuacion.pack()

boton_factorizar = tk.Button(ventana, text="Factorizar", command=factorizar_ecuacion)
boton_factorizar.pack()

salida_factorizacion = tk.Label(ventana, text="Factorización: ")
salida_factorizacion.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
