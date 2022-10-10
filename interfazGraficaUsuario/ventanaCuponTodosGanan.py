import tkinter as tk
import pandas as pd
import unidecode
import sqlite3
from pandastable import Table
from tkinter.ttk import Combobox


def cuponTodosGanan():


    #***********************************************************************
    # FUNCIONES
    #***********************************************************************

    def generar_tabla(df):

        pt = Table(frame_inferior, dataframe=df, enable_menus=False,
                   showstatusbar=True, editable=False, width=1000, height=100)
        pt.show()
        inhabilitar_boton()


    def obtener_df():

        dicc_pais = {
            'Argentina':'AR',
            'Bolivia':'BO',
            'Brasil':'BR',
            'Chile':'CL',
            'Colombia':'CO',
            'Costa Rica':'CR',
            'Dominicana':'DO',
            'Ecuador':'EC',
            'El Salvador':'SV',
            'Unión Europea':'UE',
            'Guatemala':'GT',
            'Honduras':'', # no existe
            'México':'MX',
            'Nicaragua':'NI',
            'Panamá':'PA',
            'Paraguay':'PY',
            'Perú':'PE',
            'Uruguay':'UY',
            'USA':'US'
        }

        pais = dicc_pais[paises_cb.get()]
        
        conexion = sqlite3.connect("gestorInventariosdb.db")
        df_general = pd.read_sql_query("SELECT * FROM cuponTodosGanan", con=conexion)
        
        df = df_general[df_general['PAIS'] == pais] 

        generar_tabla(df)


    def inhabilitar_boton():
        boton_generar.config(state=tk.DISABLED)

    
    def habilitar_boton():
        boton_generar.config(state=tk.NORMAL)


    def on_select_pais(event):
        habilitar_boton()


    def presionado(event):
        obtener_df()

    #***********************************************************************
    # CREACION DE ROOT
    #***********************************************************************
    root = tk.Toplevel()
    root.iconbitmap("interfazGraficaUsuario\icono2.ico")
    root.title("Cupón todos ganan")
    root.resizable(False, False)
    root.configure(padx=10, pady=10)
    root.focus_force()


    #***********************************************************************
    # CREACION DE FRAMES
    #***********************************************************************
    frame_superior = tk.Frame(root)
    frame_inferior = tk.LabelFrame(root, padx=10, pady=10)


    #***********************************************************************
    # POSICIONAMIENTO DE FRAMES
    #***********************************************************************
    frame_superior.grid(sticky="w", pady=[0,15])
    frame_inferior.grid()


    # ************************************************************************
    # MENU BAR
    # ************************************************************************
    menubar = tk.Menu(root)

    archivo = tk.Menu(menubar, tearoff=0)
    archivo.add_command(label="Cerrar", command=root.destroy)
    menubar.add_cascade(label="Archivo", menu=archivo)

    ayuda = tk.Menu(menubar, tearoff=0)
    ayuda.add_command(label="Manual de usuario")
    menubar.add_cascade(label="Ayuda", menu=ayuda)


    #***********************************************************************
    # CREACION DE WIDGETS
    #***********************************************************************
    label_pais = tk.Label(frame_superior, text="País")
    paises_cb = Combobox(frame_superior)
    boton_generar = tk.Button(frame_superior, text="Generar", command=obtener_df)

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
        'Unión Europea',
        'Guatemala',
        'Honduras',
        'México',
        'Nicaragua',
        'Panamá',
        'Paraguay',
        'Perú',
        'Uruguay',
        'USA'
    ]


    #***********************************************************************
    # POSICIONAMIENTO DE WIDGETS
    #***********************************************************************
    label_pais.grid(row=0, column=0)
    paises_cb.grid(row=0, column=1, padx=[10,15])
    boton_generar.grid(row=0, column=2, ipadx=10, ipady=5)


    #***********************************************************************
    # CONFIGURACION DE WIDGETS
    #***********************************************************************    
    root.config(menu=menubar)
    # frame_superior.config(width=1000, height=200)
    frame_inferior.config(width=1000, height=180)


    #***********************************************************************
    # COMPORTAMIENTO DE WIDGETS
    #*********************************************************************** 
    inhabilitar_boton()
    paises_cb.bind("<<ComboboxSelected>>", on_select_pais)
    boton_generar.bind("<Return>", presionado)