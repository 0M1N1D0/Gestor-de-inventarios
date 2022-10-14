
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from pandastable import Table
from tkinter.ttk import Combobox
import sqlite3


def historico_tipo_kits():


    #***********************************************************************
    # FUNCIONES
    #***********************************************************************  

    def habilita_boton():
        boton_consultar.config(state=tk.NORMAL)

    
    def inhabilita_boton():
        boton_consultar.config(state=tk.DISABLED)

    
    def pais_seleccionado(event):
        habilita_boton()
    
    
    def boton_presionado(event):
        obtiene_df()


    def obtiene_df():
        pais = paises_cb.get()
      
        conexion = sqlite3.connect("gestorInventariosdb.db")

        try:
            df_general = pd.read_sql_query("SELECT * FROM historicoyTipoKits", con=conexion)
        except:
            messagebox.showerror(
                message="Ha ocurrido un error al consultar la información en la base de datos", 
                title="Error de consulta"
            )
            inhabilita_boton()
            paises_cb.delete(0,100)
        else:
            df_final = df_general[df_general['País'] == pais]
            if df_final.empty:
                messagebox.showerror(message="El país seleccionado no contiene información.", title="Error de consulta")
                paises_cb.delete(0,100)
                inhabilita_boton()
            else:
                generar_tabla(df_final)
    

    def generar_tabla(df):

        def on_closing():
            inhabilita_boton()
            paises_cb.delete(0,100)
            tabla.destroy()


        tabla = tk.Toplevel()
        tabla.title("Histórico y tipos de kits")
        tabla.iconbitmap("interfazGraficaUsuario\icono2.ico")
        tabla.geometry("950x700")

        pt = Table(tabla, dataframe=df, enable_menus=False, showstatusbar=False, editable=False)
        pt.show()
        pt.focus_force()

        tabla.protocol("WM_DELETE_WINDOW", on_closing)

    #***********************************************************************
    # CREACION DE ROOT
    #***********************************************************************    
    root = tk.Toplevel()
    root.iconbitmap("interfazGraficaUsuario\icono2.ico")
    root.title("Histórico y tipo de kits")
    root.resizable(False, False)
    root.focus_force()
    root.configure(padx=10, pady=10)


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
    label_pais = ttk.Label(root, text='País')
    paises_cb = Combobox(root)
    boton_consultar = ttk.Button(root, text='Consultar', command=obtiene_df)

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
    paises_cb.grid(row=0, column=1, padx=[5, 15])
    boton_consultar.grid(row=0, column=2, ipadx=10, ipady=5)


    #***********************************************************************
    # COMPORTAMIENTO DE WIDGETS
    #***********************************************************************
    inhabilita_boton()
    paises_cb.bind("<<ComboboxSelected>>", pais_seleccionado)
    boton_consultar.bind("<Return>", boton_presionado)



    root.config(menu=menubar)


