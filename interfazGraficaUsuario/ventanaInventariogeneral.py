import tkinter as tk
import sqlite3
from tkinter.ttk import Combobox
import pandas as pd
from tkinter import messagebox
from pandastable import Table 
import unidecode # elimina los acentos y tildes del nombre pais 

def ventanaInventarioGeneral():

    def seleccion_pais():
        pais = comboB_pais.get()
        pais = unidecode.unidecode(pais)
        pais = "inventarioGeneral" + pais
        
         # conexicon a DB
        conexion = sqlite3.connect("gestorInventariosdb.db")
        # creación de df
        try:
            df = pd.read_sql_query(f"SELECT * FROM {pais}", con=conexion)
            # print(df)
        except:
            messagebox.showerror(title="Error", message="Ocurrió un error al cargar la base de datos.")

        conexion.close()

        buscarProducto(df)

    def buscarProducto(df):
        '''
            Filtra el DF con el texto ingresado. 
        '''
    
        producto = textoBuscar.get(1.0, "end-1c")
        producto = producto.upper()

        if producto:
            df_filtrado = df[df['Texto breve de material'].str.contains(producto)]
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
    label_pais = tk.Label(ventana, text="País")
    comboB_pais = Combobox(ventana, width=15)
    labelBuscar = tk.Label(ventana, text="Buscar")
    textoBuscar = tk.Text(ventana, height=1, width=30)
    botonGenerar = tk.Button(ventana, text="Generar", command=seleccion_pais)

    comboB_pais['values'] = (
        'Argentina',
        'Bolivia',
        'Brasil',
        'Chile',
        'Colombia',
        'Costa Rica',
        'Dominicana',
        'Ecuador',
        'El Salvador',
        'España',
        'Guatemala',
        'Honduras',
        'Italia',
        'México',
        'Nicaragua',
        'Nigeria',
        'Panamá',
        'Paraguay',
        'Perú',
        'Rusia',
        'Uruguay',
        'USA'
    )
    
    # ****************** posición widgets *****************************
    label_pais.grid(row=0, column=0, pady=[0, 15], sticky="e")
    comboB_pais.grid(row=0, column=1, padx=[10,0], pady=[0, 15], sticky="w")
    labelBuscar.grid(row=1, column=0)
    textoBuscar.grid(row=1, column=1, padx=[10,0])
    botonGenerar.grid(columnspan=2, pady=[15,0], ipadx=10, ipady=5)
    
    # ***************** configuraciones *******************************
    textoBuscar.configure(font=("arial", 10))

    # *************** comportamientos **************************************
    textoBuscar.focus_force() 
    textoBuscar.bind("<Tab>", focus_next_widget)
    botonGenerar.bind("<Return>", presionado)


    ventana.config(menu=menubar)
    ventana.mainloop()

  

