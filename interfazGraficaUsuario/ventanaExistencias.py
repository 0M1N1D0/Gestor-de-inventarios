
import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Combobox
import pandas as pd
from pandastable import Table
import unidecode # elimina tildes y acentos

global df_existencias_centros
global listado_almacenes
global almacen
almacen = ""
listado_almacenes = []


def ventanaExistencias():

    # ************************************************************************
    # FUNCIONES
    # ************************************************************************
    
    # genera la tabla
    def generartabla():
        
        # limpia los combobox y el Text y cierra ventana. 
        def on_closing():
            global df_existencias_centros
            global listado_almacenes
            global almacen
            global listado_almacenes
            nonlocal paises_cb
            nonlocal almacenes_cb
            nonlocal texto_producto
            df_existencias_centros = None
            listado_almacenes = []
            almacen = ""
            paises_cb.delete(0, 100)
            almacenes_cb.delete(0, 100)
            texto_producto.delete("1.0", "end")
            tabla.destroy()
            

            
        
        global df_existencias_centros
        tabla = tk.Toplevel()
        tabla.iconbitmap("interfazGraficaUsuario\icono2.ico")
        tabla.title("Existencias SAP")
        tabla.geometry("900x500")
        pt = Table(tabla, dataframe=df_existencias_centros, enable_menus=True,
                   showstatusbar=True, editable=True)
        pt.show()
        pt.focus_force()
        
        tabla.protocol("WM_DELETE_WINDOW", on_closing)
        
        

    # crea el DF con el país seleccionado
    def seleccion_pais():
        global df_existencias_centros
        pais = paises_cb.get()
        pais = unidecode.unidecode(pais)
        pais = "existencias" + pais

        # ************************************************************************
        # CONEXION A DB Y CREACION DE DATAFRAME
        # ************************************************************************
        conexion = sqlite3.connect("gestorInventariosdb.db")
        # creación de df
        try:
            df_existencias = pd.read_sql_query(
                f"SELECT * FROM {pais}", con=conexion)
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

        crea_lista_almacenes(df_existencias_centros)
        # buscar_nombre_producto(df_existencias_centros)


    # crea una lista con los almacenes del país seleccionado
    def crea_lista_almacenes(df):
        global listado_almacenes
        # obtiene registros de columna de almacenes
        listado_almacenes = df['Concep búsqueda 1']
        # quita los duplicados
        listado_almacenes = listado_almacenes.drop_duplicates()
        # los convierte a lista
        listado_almacenes = list(listado_almacenes)


    # si se ingreso nombre de producto, crea un DF con el nombre del producto
    def buscar_nombre_producto():
        global df_existencias_centros
        global almacen
        nombre_producto = texto_producto.get(1.0, "end-1c")
        nombre_producto = nombre_producto.upper()
        
       
        if nombre_producto and almacen != "":
            df_existencias_centros = df_existencias_centros[
                df_existencias_centros['Descripción'].str.contains(nombre_producto)]
            df_existencias_centros = df_existencias_centros[
                df_existencias_centros['Concep búsqueda 1'].str.contains(almacen)]
        elif almacen:
            df_existencias_centros = df_existencias_centros[
                df_existencias_centros['Concep búsqueda 1'].str.contains(almacen)]
        elif nombre_producto or almacen == "":
            df_existencias_centros = df_existencias_centros[
                df_existencias_centros['Descripción'].str.contains(nombre_producto)]

        generartabla()


    def on_select_pais(event):
        seleccion_pais()
        almacenes_cb['values'] = listado_almacenes


    def on_select_almacen(event):
        global almacen
        almacen = almacenes_cb.get()
        almacen = almacen.upper()
        

    # comportamiento TAB
    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return("break")

    # comportamiento

    def presionado(event):
        buscar_nombre_producto()

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
    paises_cb['values'] = [
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
    ]

    label_almacen = tk.Label(ventana, text="Almacén")
    almacenes_cb = Combobox(ventana)
    almacenes_cb['values'] = listado_almacenes
    label_producto = tk.Label(ventana, text='Producto')
    texto_producto = tk.Text(ventana, height=1, width=30, bd=2)
    boton_generar = tk.Button(ventana, text='Generar',
                              command=buscar_nombre_producto)

    # ************************************************************************
    # POSICIONAMIENTO DE WIDGETS
    # ************************************************************************
    label_pais.grid(row=0, column=0, padx=[0, 10], pady=[0, 10], sticky="e")    
    paises_cb.grid(row=0, column=1, pady=[0, 10], sticky="w")
    label_almacen.grid(row=1, column=0, padx=[0, 10], pady=[0, 10])
    almacenes_cb.grid(row=1, column=1, pady=[0, 10], sticky="w")
    label_producto.grid(row=2, column=0, padx=[0, 10], pady=[0, 10], sticky="e")
    texto_producto.grid(row=2, column=1, pady=[0, 10])
    boton_generar.grid(row=3, columnspan=2, ipadx=5, ipady=5)

    # ************************************************************************
    # CONFIGURACION DE WODGETS
    # ************************************************************************
    texto_producto.configure(font=("arial", 10))

    # ************************************************************************
    # Comportamiento
    # ************************************************************************
    paises_cb.bind("<<ComboboxSelected>>", on_select_pais)
    almacenes_cb.bind("<<ComboboxSelected>>", on_select_almacen)
    texto_producto.bind("<Tab>", focus_next_widget)
    boton_generar.bind("<Return>", presionado)

    # ************************************************************************
    # FIN DE VENTANA
    # ************************************************************************
    ventana.config(menu=menubar)
    ventana.mainloop()
