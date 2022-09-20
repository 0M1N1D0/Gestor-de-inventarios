
import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Combobox
import pandas as pd
from pandastable import Table


def ventanaExistencias():
    
    # ************************************************************************
    # FUNCIONES
    # ************************************************************************
    
    # genera la tabla  
    def generartabla():
        tabla = tk.Toplevel()
        tabla.iconbitmap("interfazGraficaUsuario\icono2.ico")
        tabla.title("Existencias SAP")
        pt = Table(tabla, dataframe=df_existencias_centros, enable_menus=True,
                   showstatusbar=True, editable=True)
        pt.show()
        
    
    # comportamiento TAB
    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return("break")
    
    
    # comportamiento
    def presionado(event):
        generartabla()

    # ************************************************************************
    # CONEXION A DB Y CREACION DE DATAFRAME
    # ************************************************************************
    conexion = sqlite3.connect("gestorInventariosdb.db")
    # creación de df
    try:
        df_existencias = pd.read_sql_query(
            "SELECT * FROM existencias", con=conexion)
        df_centrosLogisticos = pd.read_sql_query(
            "SELECT * FROM centrosLogisticos", con=conexion)
    except:
        messagebox.showerror(
            title="Error", message="Ocurrió un error al cargar la base de datos.")

    # merge
    df_existencias_centros = pd.merge(
        left=df_existencias, right=df_centrosLogisticos, how='left', on='Centro')
    # filtrado de columnas
    df_existencias_centros = df_existencias_centros[[
        'Centro', 'Concep búsqueda 1', 'Código', 'Descripción', 'Existencias']]

    conexion.close()
    
    
    # ************************************************************************
    # CREACION DE VENTANA
    # ************************************************************************
    ventana = tk.Tk()
    ventana.title("Existencias SAP")
    # ventana.geometry("280x70")
    ventana.resizable(False, False)
    ventana.iconbitmap("interfazGraficaUsuario\icono2.ico")
    ventana.focus_force()
    ventana.configure(padx=10, pady=10)

    # ************************************************************************
    # MENU BAR
    # ************************************************************************
    menubar = tk.Menu(ventana)

    archivo = tk.Menu(menubar, tearoff=0)
    archivo.add_command(label="Cerrar", command=ventana.destroy)
    menubar.add_cascade(label="Archivo", menu=archivo)

    ayuda = tk.Menu(menubar, tearoff=0)
    ayuda.add_command(label="Manual de usuario")
    menubar.add_cascade(label="Ayuda", menu=ayuda)
    

    # ************************************************************************
    # CREACION DE WIDGETS
    # ************************************************************************
    label_pais = tk.Label(ventana, text="País")
    
    # combobox 
    paises_cb = Combobox(ventana)

    paises_cb['values'] = (
        'Todos',
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
    
    label_producto = tk.Label(ventana, text='Producto')
    texto_centro = tk.Text(ventana, height=1, width=30)
    boton_generar = tk.Button(ventana, text='Generar', command=generartabla)

    # ************************************************************************
    # POSICIONAMIENTO DE WIDGETS
    # ************************************************************************
    label_pais.grid(row=0, column=0, padx=[0,10], pady=[0,10], sticky="e")
    paises_cb.grid(row=0, column=1, pady=[0,10], sticky="w")
    label_producto.grid(row=1, column=0, padx=[0,10], pady=[0,10])
    texto_centro.grid(row=1, column=1, pady=[0,10])
    boton_generar.grid(row=2, columnspan=2, ipadx=5, ipady=5)
    
    # ************************************************************************
    # CONFIGURACION DE WODGETS
    # ************************************************************************
    texto_centro.configure(font=("arial", 10))
    
    # ************************************************************************
    # Comportamiento
    # ************************************************************************
    texto_centro.bind("<Tab>", focus_next_widget)
    boton_generar.bind("<Return>", presionado)
        
    # ************************************************************************
    # FIN DE VENTANA
    # ************************************************************************
    ventana.config(menu=menubar)
    ventana.mainloop()
