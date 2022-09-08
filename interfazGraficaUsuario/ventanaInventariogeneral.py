
import tkinter as tk
import sqlite3
import pandas as pd
from tkinter import messagebox
from pandastable import Table 

def ventanaInventarioGeneral():

    def buscarProducto():
        producto = textoBuscar.get(1.0, "end-1c")
        producto = producto.upper()

        if producto:
            df_filtrado = df[df['Descripción'].str.contains(producto)]
            generartabla(df_filtrado)
        else:
            generartabla(df)


    # función que genera la tabla 
    def generartabla(df):
        tabla = tk.Toplevel()
        tabla.iconbitmap("interfazGraficaUsuario\icono2.ico")
        tabla.title("Inventario general")
        pt = Table(tabla, dataframe=df, enable_menus=True, showstatusbar=True, editable=True, width=500, height=600)
        pt.show()
        pt.focus_force()


    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return("break")


    def presionado(event):
        buscarProducto()


    # *************** conexión a DB y obtención del DF **********************
    # conexicon a DB
    conexion = sqlite3.connect("gestorInventariosdb.db")
    # creación de df
    try:
        df = pd.read_sql_query("SELECT * FROM inventarioGeneral", con=conexion)
        # print(df)
    except:
        messagebox.showerror(title="Error", message="Ocurrió un error al cargar la base de datos.")

    conexion.close()
    # **********************************************************************


    # ************** creación de ventana root ******************************
    ventana = tk.Tk()
    ventana.title("Inventario general")
    ventana.resizable(False, False)
    ventana.iconbitmap("interfazGraficaUsuario\icono2.ico")
    ventana.configure(padx=15, pady=15)

    # *********** menu bar **********************
    menubar = tk.Menu(ventana)

    archivo = tk.Menu(menubar, tearoff=0)
    archivo.add_command(label="Cerrar", command=ventana.destroy)
    menubar.add_cascade(label="Archivo", menu=archivo)

    ayuda = tk.Menu(menubar, tearoff=0)
    ayuda.add_command(label="Manual de usuario")
    menubar.add_cascade(label="Ayuda", menu=ayuda)
    # ********************************************

    # ****************** creacion widgets *****************************
    labelBuscar = tk.Label(ventana, text="Buscar")
    textoBuscar = tk.Text(ventana, height=1, width=30)
    botonGenerar = tk.Button(ventana, text="Generar", command=buscarProducto)
    
    # ****************** posición widgets *****************************
    labelBuscar.grid(row=0, column=0)
    textoBuscar.grid(row=0, column=1, padx=[10,0])
    botonGenerar.grid(columnspan=2, pady=[15,0], ipadx=10, ipady=5)
    
    # ***************** configuraciones *******************************
    textoBuscar.configure(font=("arial", 10))

    # *************** comportamientos **************************************
    textoBuscar.focus_force() 
    textoBuscar.bind("<Tab>", focus_next_widget)
    botonGenerar.bind("<Return>", presionado)


    ventana.config(menu=menubar)
    ventana.mainloop()

  

