
from pandastable import Table
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import pandas as pd
import sqlite3
import unidecode

def estatusDP():

    global error_df 
    error_df = False

    #***********************************************************************
    # FUNCIONES
    #***********************************************************************

    def obtener_df_general():

        pais = paises_cb.get()
        pais = unidecode.unidecode(pais)
        nombre_tabla = "estatusDP" + pais

        conexion = sqlite3.connect("gestorInventariosdb.db")

        try:
            df_general = pd.read_sql_query(f"SELECT * FROM {nombre_tabla}", con=conexion)
        except:
            messagebox.showerror(title="Error", message="Error al consultar base de datos.")
            global error_df
            error_df = True
            limpia_campos()
            inhabilita_widgets()
            root.focus_force()
        else:
            return df_general


    def obtener_texto_producto():
        producto = texto_producto.get(1.0, "end-1c")
        producto = producto.upper()
        return producto # aún puede retornan valores incorrectos


    def obtener_df_final():
        df_general = obtener_df_general()
        producto = obtener_texto_producto()

            
        if producto == "":
            genera_tabla(df_general)
        else:
            try:
                df_final = df_general[df_general['Material'].str.contains(producto)]
            except:
                messagebox.showerror(message="Error al consultar la información.")
                limpia_campos()
                root.focus_force()
            else:
                if df_final.empty:
                    messagebox.showerror(title="Error", message="El nombre del producto no se encuentra en la base de datos.")
                    limpia_campos()
                    inhabilita_widgets()
                    root.focus_force()
                else:
                    genera_tabla(df_final)


    def genera_tabla(df):

        global error_df

        def on_closing():
            limpia_campos()
            inhabilita_widgets()
            tabla.destroy()

        if error_df:
            limpia_campos()
            inhabilita_widgets()
            error_df = False
    
        else:
            tabla = tk.Toplevel()
            tabla.iconbitmap("interfazGraficaUsuario\icono2.ico")
            tabla.title("Estatus planeación de la demada")
            tabla.geometry("700x300")
            pt = Table(tabla, dataframe=df, enable_menus=False, showstatusbar=False, editable=False)
            pt.show()
            pt.focus_force()

            tabla.protocol("WM_DELETE_WINDOW", on_closing)
        
           
    def limpia_campos():
        paises_cb.delete(0,100)
        texto_producto.delete("1.0", "end")



    def focus_siguiente_widget(event):
        event.widget.tk_focusNext().focus()
        return("break")

    def presionado(event):
        obtener_df_final()

    
    def inhabilita_widgets():
        texto_producto.config(state=tk.DISABLED)
        boton_generar.config(state=tk.DISABLED)

    def habilita_widgets():
        texto_producto.config(state=tk.NORMAL)
        boton_generar.config(state=tk.NORMAL)

    def cb_seleccionado(event):
        habilita_widgets()

    #***********************************************************************
    # CREACION DE ROOT
    #***********************************************************************
    root = tk.Toplevel()
    root.focus_force()
    root.title("Estatus planeación de la demanda")
    root.iconbitmap("interfazGraficaUsuario\icono2.ico")
    root.resizable(False, False)
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
    label_pais = tk.Label(root, text="País")
    paises_cb = Combobox(root)
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

    label_producto = tk.Label(root, text="Nombre de producto")
    texto_producto = tk.Text(root, height=1, width=15, bd=2)
    boton_generar = tk.Button(root, text="Generar", width=10, command=obtener_df_final)


    #***********************************************************************
    # POSICIONAMIENTO DE WIDGETS
    #***********************************************************************
    label_pais.grid(row=0, column=0)
    paises_cb.grid(row=0, column=1)
    label_producto.grid(row=0, column=2, padx=[15,0])
    texto_producto.grid(row=0, column=3)
    boton_generar.grid(row=0, column=4, padx=[15,0], ipadx=5, ipady=5)


    #***********************************************************************
    # COMPORTAMIENTO DE WIDGETS
    #**********************************************************************
    texto_producto.bind("<Tab>", focus_siguiente_widget)
    paises_cb.bind("<<ComboboxSelected>>", cb_seleccionado)
    boton_generar.bind("<Return>", presionado)

    #***********************************************************************
    # CONFGURACION DE WIDGETS
    #***********************************************************************
    root.config(menu=menubar)
    texto_producto.configure(font=("arial", 9))

    inhabilita_widgets()
    




