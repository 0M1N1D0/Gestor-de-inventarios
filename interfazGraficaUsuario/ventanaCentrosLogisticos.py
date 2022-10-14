from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import Button, messagebox
from tkinter.ttk import Combobox
import pandas as pd
from pandastable import Table


def ventanaCentrosLogisticos():

    # ************************************************************************
    # CONEXION A DB Y CREACION DE DATAFRAME
    # ************************************************************************
    conexion = sqlite3.connect("gestorInventariosdb.db")
    # creación de df
    try:
        df = pd.read_sql_query("SELECT * FROM centrosLogisticos", con=conexion)
        # print(df)
    except:
        messagebox.showerror(
            title="Error", message="Ocurrió un error al cargar la base de datos.")

    # TODO: en el manual de ayuda aclarar que la columna código postal, los valores
    # en blanco se tienen que llenar con 0 en el excel, antes de hacer la actualización,
    # sino aparecerán con decimal, ejemplo: 44770.00

    # ************************************************************************
    # FUNCIONES
    # ************************************************************************
    def generarTabla(df):
        tabla = tk.Toplevel()
        tabla.iconbitmap("interfazGraficaUsuario\icono2.ico")
        tabla.title("Visualización de Centros Logísticos")
        pt = Table(tabla, dataframe=df, enable_menus=True,
                   showstatusbar=True, editable=True)
        pt.show()
        pt.focus_force()

    def configurarDF():
        pais = paises_cb.get()
        if pais and pais != "Todos":
            df_filtrado = df[df['País'] == pais]
            generarTabla(df_filtrado)
        else:
            generarTabla(df)

    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return("break")

    def presionado(event):
        configurarDF()


    # ************************************************************************
    # CREACION DE VENTANA
    # ************************************************************************
    ventana = tk.Tk()
    ventana.title("Centros SAP")
    # ventana.geometry("300x150")
    ventana.iconbitmap("interfazGraficaUsuario\icono2.ico")
    ventana.focus_force()
    ventana.resizable(False, False)
    ventana.configure(padx=10, pady=10)
    # para pandastable es necesario usar frame
    # frame = tk.Frame(ventana)
    # frame.pack(fill='both', expand=True, pady=15)

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

    # creción de combobox
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

    botonGenerarTabla = ttk.Button(
        ventana, text="Generar", command=configurarDF, width=10)

    # ************************************************************************
    # POSICIONAMIENTO DE WIDGETS
    # ************************************************************************
    label_pais.grid(row=0, column=0, padx=[25, 10])
    paises_cb.grid(row=0, column=1, padx=[0, 25])
    botonGenerarTabla.grid(row=2, columnspan=2, pady=[15, 0], ipadx=5, ipady=5)

    # ************************************************************************
    # COMPORTAMIENTO
    # ************************************************************************
    # textoEstado.focus_force()
    # textoEstado.bind("<Tab>", focus_next_widget)
    paises_cb.bind("<Tab>", focus_next_widget)
    botonGenerarTabla.bind("<Return>", presionado)

    # ***************** configuraciones *******************************
    # textoEstado.configure(font=("arial", 10))
    # textoCiudad.configure(font=("arial", 10))

    ventana.config(menu=menubar)
    ventana.mainloop()
