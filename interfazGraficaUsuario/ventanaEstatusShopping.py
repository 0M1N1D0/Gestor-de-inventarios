import tkinter as tk
import pandas as pd
import sqlite3
from tkinter.ttk import Combobox



def ventanaEstatusShopping():


    #***********************************************************************
    # FUNCIONES
    #***********************************************************************
    def check_prod_press():
        print(check_var_prod.get())

    #***********************************************************************
    # CREACION DE ROOT
    #***********************************************************************
    root = tk.Toplevel()  
    root.title("Estatus Shopping Support")
    root.resizable(False, False)
    root.iconbitmap("interfazGraficaUsuario\icono2.ico")
    root.configure(padx=10, pady=10)
    root.focus_force()

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
    # CREACION DE FRAMES
    #***********************************************************************
    frame_checks = tk.Frame(root)
    label_frame_producto = tk.LabelFrame(root, text="Producto")
    label_frame_general = tk.LabelFrame(root, text="General")

    #***********************************************************************
    # POSICIONAMIENTO DE FRAMES
    #***********************************************************************
    frame_checks.grid(sticky="n")
    label_frame_producto.grid()
    label_frame_general.grid(sticky="s")
    

    #***********************************************************************
    # CREACION DE WIDGETS
    #***********************************************************************
    
    # variables que obtendrpan el valor del checkbutton
    check_var_prod = tk.IntVar()
    check_var_general = tk.IntVar()

    # en frame_checks
    check_producto = tk.Checkbutton(frame_checks, text='Por producto', variable=check_var_prod, command=check_prod_press)
    check_general = tk.Checkbutton(frame_checks, text='General', variable=check_var_general)

    # en label_frame_producto
    label_pais = tk.Label(label_frame_producto, text="País")
    paises_cb = Combobox(label_frame_producto)
    label_codigo_producto = tk.Label(label_frame_producto, text="Código producto")
    texto_codigo = tk.Text(label_frame_producto, height=1, width=15, bd=2)
    boton_buscar = tk.Button(label_frame_producto, text="Buscar")

    #***********************************************************************
    # POSICIONAMIENTO DE WIDGETS
    #***********************************************************************
    
    # en frame_checks
    check_producto.grid(row=0, column=0)
    check_general.grid(row=0, column=1)

    # en label_frame_producto
    label_pais.grid(row=0, column=0)
    paises_cb.grid(row=0, column=1)
    label_codigo_producto.grid(row=0, column=2)
    texto_codigo.grid(row=0, column=3)
    boton_buscar.grid(row=0, column=4)
    

    #***********************************************************************
    # COMPORTAMIENTO DE WIDGETS
    #***********************************************************************
    #check_producto.select()


    #***********************************************************************
    # CONFGURACION DE WIDGETS
    #***********************************************************************
    texto_codigo.configure(font=("arial", 10))
    root.config(menu=menubar)
    # root.mainloop()