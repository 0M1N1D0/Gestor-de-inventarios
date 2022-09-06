
import tkinter as tk
import sqlite3
from tkinter import Button, messagebox
import pandas as pd
from pandastable import Table 


def ventanaExistencias():

    ventana = tk.Tk()
    ventana.title("Centros logisticos")
    ventana.geometry("280x70")
    ventana.iconbitmap("interfazGraficaUsuario\icono2.ico")
    ventana.focus_force()

    frame = tk.Frame(ventana)
    frame.pack(fill='both', expand=True)

    # *********** menu bar **********************
    menubar = tk.Menu(ventana)

    archivo = tk.Menu(menubar, tearoff=0)
    archivo.add_command(label="Cerrar", command=ventana.destroy)
    menubar.add_cascade(label="Archivo", menu=archivo)

    ayuda = tk.Menu(menubar, tearoff=0)
    ayuda.add_command(label="Manual de usuario")
    menubar.add_cascade(label="Ayuda", menu=ayuda)

    ventana.config(menu=menubar)
    ventana.mainloop()