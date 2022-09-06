import tkinter as tk
import sqlite3
from tkinter import Button, messagebox
import pandas as pd
from pandastable import Table 


def ventanaCentrosLogisticos():

    def generarTabla(df):
        tabla = tk.Toplevel()
        tabla.iconbitmap("interfazGraficaUsuario\icono2.ico")
        tabla.title("Visualización de Centros Logísticos")
        pt = Table(tabla, dataframe=df, enable_menus=True, showstatusbar=True, editable=True)
        pt.show()
        pt.focus_force()


    def configurarDF():

        estado = textoEstado.get(1.0, "end-1c") # parametros requeridos para guardar el texto
        ciudad = textoCiudad.get(1.0, 'end-1c')
        estado = estado.capitalize()
        ciudad = ciudad.capitalize()

        if not estado and not ciudad:
            generarTabla(df)
        elif estado and ciudad:
            df_filtrado = df[(df['Estado'].str.contains(estado)) & (df['Nombre'].str.contains(ciudad))]
            generarTabla(df_filtrado)
        elif estado:
            df_filtrado = df[df['Estado'].str.contains(estado)]
            generarTabla(df_filtrado)
        else:
            df_filtrado = df[df['Nombre'].str.contains(ciudad)]
            generarTabla(df_filtrado)


    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return("break")


    def presionado(event):
        configurarDF()


    ventana = tk.Tk()
    ventana.title("Centros logisticos")
    # ventana.geometry("275x115")
    ventana.iconbitmap("interfazGraficaUsuario\icono2.ico")
    ventana.focus_force()
    ventana.resizable(False, False)
    ventana.configure(padx=10, pady=10)
    # para pandastable es necesario usar frame
    # frame = tk.Frame(ventana)
    # frame.pack(fill='both', expand=True, pady=15)

    # *********** menu bar **********************
    menubar = tk.Menu(ventana)

    archivo = tk.Menu(menubar, tearoff=0)
    archivo.add_command(label="Cerrar", command=ventana.destroy)
    menubar.add_cascade(label="Archivo", menu=archivo)

    ayuda = tk.Menu(menubar, tearoff=0)
    ayuda.add_command(label="Manual de usuario")
    menubar.add_cascade(label="Ayuda", menu=ayuda)
    # ********************************************

    # *************** conexión a DB y obtención del DF **********************
    # conexicon a DB
    conexion = sqlite3.connect("gestorInventariosdb.db")
    # creación de df
    try:
        df = pd.read_sql_query("SELECT * FROM centrosLogisticos", con=conexion)
        # print(df)
    except:
        messagebox.showerror(title="Error", message="Ocurrió un error al cargar la base de datos.")
    # **********************************************************************
    
    # ************** widgets ******************************************
    labelEstado = tk.Label(ventana, text="Estado:")
    textoEstado = tk.Text(ventana, height=1, width=25)
    labelCiudad = tk.Label(ventana,text="Ciudad:")
    textoCiudad = tk.Text(ventana, height=1, width=25)
    botonGenerarTabla = Button(ventana, text="Generar", command=configurarDF, width=10)

    # ******************* posicion widgets **************************
    labelEstado.grid(row=0, column=0, padx=10)
    textoEstado.grid(row=0, column=1, padx=15)
    labelCiudad.grid(row=1, column=0, padx=10, pady=[10,0])
    textoCiudad.grid(row=1, column=1, padx=15, pady=[10,0])
    botonGenerarTabla.grid(row=2, columnspan=2, pady=[15,0], ipadx=5, ipady=5)

    
    # *************** comportamientos **************************************
    textoEstado.focus_force() 
    textoEstado.bind("<Tab>", focus_next_widget)
    textoCiudad.bind("<Tab>", focus_next_widget)
    botonGenerarTabla.bind("<Return>", presionado)

    # ***************** configuraciones *******************************
    textoEstado.configure(font=("arial", 10))
    textoCiudad.configure(font=("arial", 10))


    ventana.config(menu=menubar)
    ventana.mainloop()