
import tkinter as tk
import sqlite3
from tkinter import Button, messagebox
import pandas as pd
from pandastable import Table 

def ventanaExistencias():

    
    
    def generartabla():
        # tabla = tk.Toplevel()
        # tabla.iconbitmap("interfazGraficaUsuario\icono2.ico")
        # tabla.title("Inventario general")
        pt = Table(frame_tabla, dataframe=df_existencias_centros, enable_menus=True, showstatusbar=True, editable=True)
        pt.show()
        

    # *************** conexión a DB y obtención del DF **********************
    # conexicon a DB
    conexion = sqlite3.connect("gestorInventariosdb.db")
    # creación de df
    try:
        df_existencias = pd.read_sql_query("SELECT * FROM existencias", con=conexion)
        df_centrosLogisticos = pd.read_sql_query("SELECT * FROM centrosLogisticos", con=conexion)
    except:
        messagebox.showerror(title="Error", message="Ocurrió un error al cargar la base de datos.")

    # merge 
    df_existencias_centros = pd.merge(left=df_existencias, right=df_centrosLogisticos, how='left', on='Centro')
    # filtrado de columnas
    df_existencias_centros = df_existencias_centros[['Centro', 'Nombre', 'Código', 'Descripción', 'Existencias']]
    
    conexion.close()
    # **********************************************************************

    ventana = tk.Tk()
    ventana.title("Centros logisticos")
    #ventana.geometry("280x70")
    ventana.iconbitmap("interfazGraficaUsuario\icono2.ico")
    ventana.focus_force()
    #ventana.configure(padx=10, pady=10)

    frame_opciones = tk.Frame(ventana)
    frame_tabla = tk.Frame(ventana)
    
    frame_opciones.grid(sticky="n")
    frame_tabla.grid(sticky="s")

    # *********** menu bar **********************
    menubar = tk.Menu(ventana)

    archivo = tk.Menu(menubar, tearoff=0)
    archivo.add_command(label="Cerrar", command=ventana.destroy)
    menubar.add_cascade(label="Archivo", menu=archivo)

    ayuda = tk.Menu(menubar, tearoff=0)
    ayuda.add_command(label="Manual de usuario")
    menubar.add_cascade(label="Ayuda", menu=ayuda)
    # ********************************************

    # ****************** creacion de widgets **********************
    label_centro = tk.Label(frame_opciones, text='Centro')
    texto_centro = tk.Text(frame_opciones, height=1, width=30)
    boton_generar = tk.Button(frame_opciones, text='Generar', command=generartabla)

    # ***************** colocacion de widgets ********************
    label_centro.grid(row=0, column=0)
    texto_centro.grid(row=0, column=1)
    boton_generar.grid(row=1, columnspan=2)
    # **************** configuraciones de widgets *************************
    texto_centro.configure(font=("arial", 10))


    ventana.config(menu=menubar)
    ventana.mainloop()