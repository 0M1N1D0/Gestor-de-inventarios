
from tkinter import messagebox
from pandastable import Table
import tkinter as tk
import pandas as pd
import sqlite3
from tkinter.ttk import Combobox
import unidecode
from tkinter import ttk


def ventanaEstatusShopping():

    #***********************************************************************
    # FUNCIONES
    #***********************************************************************

    # inhabilita los widgets de entrada de datos 
    # usada en la creación de la ventana
    def inhabilita_widgets_producto():  
        paises_cb.config(state=tk.DISABLED)
        texto_codigo.config(state=tk.DISABLED)
        boton_buscar.config(state=tk.DISABLED)


    def inhabilita_widgets_general():
        paises_gen_cb.config(state=tk.DISABLED)
        boton_generar.config(state=tk.DISABLED)
        

    # habilita los widgets del LabelFrame producto
    def habilita_widgets_producto():
        paises_cb.config(state=tk.NORMAL)
        texto_codigo.config(state=tk.NORMAL)
        boton_buscar.config(state=tk.NORMAL)


    # habilita los widgets del LabelFrame general
    def habilita_widgets_general():
        paises_gen_cb.config(state=tk.NORMAL)
        boton_generar.config(state=tk.NORMAL)


    def check_press():

        if check_var_prod.get() == 1:
            habilita_widgets_producto()
            inhabilita_widgets_general()

        if check_var_general.get() == 1:
            habilita_widgets_general()
            inhabilita_widgets_producto()

        if check_var_prod.get() == 1 and check_var_general.get() == 1:
            inhabilita_widgets_producto()
            inhabilita_widgets_general()

        if check_var_prod.get() == 0 and check_var_general.get() == 0:
            inhabilita_widgets_producto()
            inhabilita_widgets_general()

    def limpia_datos():
        paises_cb.delete(0,100)
        texto_codigo.delete("1.0", "end")
        paises_gen_cb.delete(0,100)

    # genera el DF con el país y producto ingresados.
    # cuando se cierra la tabla, limpia los datos.
    def buscar_producto():

        def cerrando_tabla():
            tabla.destroy()
            limpia_datos()

        pais = paises_cb.get()
        pais = unidecode.unidecode(pais)
        nombre_tabla = "estatusShopping" + pais

        #***********************************************************************
        # CONEXION A DB Y CREACION DE DF 
        #***********************************************************************
        conexion = sqlite3.connect("gestorInventariosdb.db")

        try:
            df = pd.read_sql_query(f"SELECT * FROM {nombre_tabla}", con=conexion)
        except:
            messagebox.showerror(message="El código ingresado no se encuentra en la base de datos.")
            messagebox.showwarning(message="El código ingresado debe ser en formato CORBIZ (a 7 dígitos).\nEjemplo: 2603201")
            limpia_datos()

        else:
            codigo = texto_codigo.get("1.0", "end")
            try:
                codigo = int(codigo)
            except:
                messagebox.showerror(message="El código ingresado no se encuentra en la base de datos.")
                messagebox.showwarning(message="El código ingresado debe ser en formato CORBIZ (a 7 dígitos).\nEjemplo: 2603201")
                limpia_datos()
            else:
                df_codigo = df[df['SKU'] == int(codigo)]
                

                if df_codigo.empty:
                    messagebox.showerror(message="El código ingresado no se encuentra en la base de datos.")
                    messagebox.showwarning(message="El código ingresado debe ser en formato CORBIZ (a 7 dígitos).\nEjemplo: 2603201")
                    limpia_datos()
                else:

                    tabla = tk.Toplevel()
                    tabla.title("Estatus shopping support")
                    tabla.iconbitmap("interfazGraficaUsuario\icono2.ico")
                    tabla.resizable(False, False)
                    pt = Table(
                            tabla, 
                            dataframe=df_codigo, 
                            enable_menus=False, 
                            showstatusbar=False, 
                            editable=False, 
                            width=1000, 
                            height=40
                        )
                    pt.show()
                    tabla.protocol("WM_DELETE_WINDOW", cerrando_tabla)


    # genera el DF con el país y producto ingresados.
    # cuando se cierra la tabla, limpia los datos.
    def buscar_pais():

        def cerrando_tabla_pais():
            tabla_gen.destroy()
            limpia_datos()


        pais = paises_gen_cb.get()
        
        if pais == "":
            messagebox.showerror(message="El país no se a ingresado o no se encuentra en la base de datos.")
        else:
            pais = unidecode.unidecode(pais)
            nombre_tabla = "estatusShopping" + pais


            #***********************************************************************
            # CONEXION A DB Y CREACION DE DF 
            #***********************************************************************
            conexion = sqlite3.connect("gestorInventariosdb.db")

            try:
                df = pd.read_sql_query(f"SELECT * FROM {nombre_tabla}", con=conexion)
            except:
                messagebox.showerror(message="El país ingresado no se encuentra en la base de datos.")
                limpia_datos()

            else:
                tabla_gen = tk.Toplevel()
                tabla_gen.title(f"Estatus shopping support {pais}")
                tabla_gen.iconbitmap("interfazGraficaUsuario\icono2.ico")
                pt = Table(
                                tabla_gen, 
                                dataframe=df, 
                                enable_menus=False, 
                                showstatusbar=False, 
                                editable=False, 
                                width=900, 
                                height=500
                            )
                pt.show()
                tabla_gen.protocol("WM_DELETE_WINDOW", cerrando_tabla_pais)


    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return("break")


    def boton_buscar_presionado(event):
        buscar_producto()


    def boton_generar_presionado(event):
        buscar_pais()


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
    label_frame_producto = tk.LabelFrame(root, text="Producto", padx=10, pady=10)
    label_frame_general = tk.LabelFrame(root, text="General", padx=10, pady=10)
    
   

    #***********************************************************************
    # POSICIONAMIENTO DE FRAMES
    #***********************************************************************
    frame_checks.grid(row=0)
    label_frame_producto.grid(row=1, pady=5)
    label_frame_general.grid(row=3, pady=5)
    

    #***********************************************************************
    # CREACION DE WIDGETS
    #***********************************************************************
    
    # variables que obtendrpan el valor del checkbutton
    check_var_prod = tk.IntVar()
    check_var_general = tk.IntVar()

    # en frame_checks
    check_producto = ttk.Checkbutton(
        frame_checks, 
        text='Por producto', 
        variable=check_var_prod, 
        command=check_press
    )

    check_general = ttk.Checkbutton(
        frame_checks, 
        text='General', 
        variable=check_var_general, 
        command=check_press
    )


    # en label_frame_producto
    label_pais = tk.Label(label_frame_producto, text="País")
    paises_cb = Combobox(label_frame_producto)
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
    label_codigo_producto = tk.Label(label_frame_producto, text="Código producto")
    texto_codigo = tk.Text(label_frame_producto, height=1, width=15, bd=2)
    boton_buscar = ttk.Button(label_frame_producto, text="Buscar", width=10, command=buscar_producto)

    label_pais_gen = tk.Label(label_frame_general, text="País")
    paises_gen_cb = Combobox(label_frame_general)
    paises_gen_cb['values'] = [
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
    boton_generar = ttk.Button(label_frame_general, text="Generar", width=10, command=buscar_pais)

    #***********************************************************************
    # POSICIONAMIENTO DE WIDGETS
    #***********************************************************************
    
    # en frame_checks
    check_producto.grid(row=0, column=0)
    check_general.grid(row=0, column=1)

    # en label_frame_producto
    label_pais.grid(row=0, column=0)
    paises_cb.grid(row=0, column=1)
    label_codigo_producto.grid(row=0, column=2, padx=[15, 0])
    texto_codigo.grid(row=0, column=3)
    boton_buscar.grid(row=0, column=4, ipadx=5, ipady=5, padx=[15,0])
    
    # en label_frame_general
    label_pais_gen.grid(row=0, column=0)
    paises_gen_cb.grid(row=0, column=1)
    boton_generar.grid(row=0, column=2, ipadx=5, ipady=5, padx=[15,0])

    #***********************************************************************
    # COMPORTAMIENTO DE WIDGETS
    #***********************************************************************
    #check_producto.select()
    texto_codigo.bind("<Tab>", focus_next_widget)
    boton_buscar.bind("<Return>", boton_buscar_presionado)
    boton_generar.bind("<Return>", boton_generar_presionado)

    #***********************************************************************
    # CONFGURACION DE WIDGETS
    #***********************************************************************
    texto_codigo.configure(font=("arial", 9))
    root.config(menu=menubar)
    inhabilita_widgets_general()
    inhabilita_widgets_producto()
    # root.mainloop()