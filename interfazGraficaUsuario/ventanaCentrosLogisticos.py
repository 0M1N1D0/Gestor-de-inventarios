
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
    ventana.geometry("280x100")
    ventana.iconbitmap("interfazGraficaUsuario\icono2.ico")
    ventana.focus_force()
    # para pandastable es necesario usar frame
    frame = tk.Frame(ventana)
    frame.pack(fill='both', expand=True)

    # *********** menu bar **********************
    menubar = tk.Menu(ventana)

    archivo = tk.Menu(menubar, tearoff=0)
    archivo.add_command(label="Cerrar", command=ventana.destroy)
    menubar.add_cascade(label="Archivo", menu=archivo)

    ayuda = tk.Menu(menubar, tearoff=0)
    ayuda.add_command(label="Manual de usuario", command=ventana.destroy)
    menubar.add_cascade(label="Ayuda", menu=ayuda)
    # ********************************************

    botonGenerarTabla = Button(frame, text="Generar tabla", command=generarTabla)
    botonGenerarTabla.grid(row=1, column=0)

    # conexicon a DB
    conexion = sqlite3.connect("gestorInventariosdb.db")
    # creación de df
    try:
        df = pd.read_sql_query("SELECT * FROM centrosLogisticos", con=conexion)
        # print(df)
    except:
        messagebox.showerror(title="Error", message="Ocurrió un error al cargar la base de datos.")

    ventana.config(menu=menubar)
    ventana.mainloop()