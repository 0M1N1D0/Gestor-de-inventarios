import tkinter as tk
import sqlite3
import pandas as pd
from tkinter import messagebox
from pandastable import Table 

def ventanaInventarioGeneral():
    # *************** conexión a DB y obtención del DF **********************
    # conexicon a DB
    conexion = sqlite3.connect("gestorInventariosdb.db")
    # creación de df
    try:
        df = pd.read_sql_query("SELECT * FROM inventarioGeneral", con=conexion)
        # print(df)
    except:
        messagebox.showerror(title="Error", message="Ocurrió un error al cargar la base de datos.")
    # **********************************************************************
    tabla = tk.Toplevel()
    tabla.iconbitmap("interfazGraficaUsuario\icono2.ico")
    tabla.title("Inventario general")
    pt = Table(tabla, dataframe=df, enable_menus=True, showstatusbar=True, editable=True)
    pt.show()
    pt.focus_force()