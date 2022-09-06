
import tkinter as tk
import sqlite3
from tkinter import E, Button, Label, messagebox
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
        if not estado:
            generarTabla(df)
        else:
            estado = estado.capitalize()
            estadoDF = df[df['Estado'].str.contains(estado)]
            generarTabla(estadoDF)

    ventana = tk.Tk()
    ventana.title("Centros logisticos")
    # ventana.geometry("280x70")
    ventana.iconbitmap("interfazGraficaUsuario\icono2.ico")
    ventana.focus_force()
    ventana.resizable(False, False)
    # para pandastable es necesario usar frame
    frame = tk.Frame(ventana)
    frame.pack(fill='both', expand=True, pady=15)

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
    labelEstado = Label(frame, text="Estado:")
    textoEstado = tk.Text(frame, height=1, width=20)
    botonGenerarTabla = Button(frame, text="Generar tabla", command=configurarDF)

    # ******************* posicion widgwts **************************
    labelEstado.grid(row=0, column=0, padx=10)
    textoEstado.grid(row=0, column=1, padx=15)
    botonGenerarTabla.grid(row=1, columnspan=2, pady=[15,0])


    ventana.config(menu=menubar)
    ventana.mainloop()