
import tkinter as tk
import sqlite3
from tkinter import Button, messagebox
import pandas as pd
from pandastable import Table 


def ventanaCentrosLogisticos():

    def generarTabla():
        tabla = tk.Toplevel()
        tabla.iconbitmap("interfazGraficaUsuario\icono2.ico")
        tabla.title("Visualización de Centros Logísticos")
        pt = Table(tabla, dataframe=df, enable_menus=True, showstatusbar=True)
        pt.show()
        pt.focus_force()
        
    

    ventana = tk.Tk()
    ventana.title("Centros logisticos")
    ventana.geometry("280x40")
    ventana.iconbitmap("interfazGraficaUsuario\icono2.ico")
    ventana.focus_force()
    # para pandastable es necesario usar frame
    frame = tk.Frame(ventana)
    frame.pack(fill='both', expand=True)

    botonGenerarTabla = Button(frame, text="Generar tabla", command=generarTabla)
    botonGenerarTabla.grid(row=0, column=0)


    conexion = sqlite3.connect("gestorInventariosdb.db")

    try:
        df = pd.read_sql_query("SELECT * FROM centrosLogisticos", con=conexion)
        # print(df)
    except:
        messagebox.showerror(title="Error", message="Ocurrió un error al cargar la base de datos.")

    

    ventana.mainloop()