import tkinter as tk

def actualizar_estatus_shopping():

    #***********************************************************************
    # CREACION DE ROOT
    #***********************************************************************
    root = tk.Tk()
    root.title("Estatus shopping por producto")
    root.resizable(False, False)
    root.iconbitmap("interfazGraficaUsuario\icono2.ico")
    root.configure(padx=10, pady=10)
    #root.geometry("1300x300")
    root.focus_force()

    '''
    ESTRUCTURA DE ROOT
    -root
        -frame1
        -frame2
            -label_frame
                -sub_frame1
                -sub_frame2
                -sub_frame3
    '''


    # ************************************************************************
    # CREACION DE FRAMES
    # ************************************************************************
    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    label_frame = tk.LabelFrame(frame2, text="Estatus")
    sub_frame1 = tk.Frame(label_frame)
    sub_frame2 = tk.Frame(label_frame)
    sub_frame3 = tk.Frame(label_frame)
    
    # ************************************************************************
    # POSICIONAMIENTO DE FRAMES
    # ************************************************************************
    frame1.grid(sticky="wn")
    frame2.grid(sticky="s")
    label_frame.grid()
    sub_frame1.grid(padx=10, sticky="w")
    sub_frame2.grid(padx=10, pady=[0,10])
    sub_frame3.grid()


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


    # ************************************************************************    
    # CREACION DE WIDGETS
    # ************************************************************************
    label_codigo = tk.Label(frame1, text="Código de producto")
    texto_codigo = tk.Text(frame1, height=1, width=20, bd=2)
    boton_buscar = tk.Button(frame1, text="Buscar", width=10)
    
    label_sku = tk.Label(sub_frame1, text="Código")
    label_nombre = tk.Label(sub_frame1, text="Nombre de producto")
    label_estatus = tk.Label(sub_frame1, text="Estatus principal")
    label_telemark = tk.Label(sub_frame2, text="Telemarketing")
    label_tijuana = tk.Label(sub_frame2, text="Tijuana")
    label_colroma = tk.Label(sub_frame2, text="Colonia Roma")
    label_villahermosa = tk.Label(sub_frame2, text="Villahermosa")
    label_lapaz = tk.Label(sub_frame2, text="La Paz")
    label_sanluis = tk.Label(sub_frame2, text="San Luis")
    label_hermosillo = tk.Label(sub_frame2, text="Hermosillo")

    texto_sku = tk.Text(sub_frame1, height=1, width=15, bd=2)
    texto_nombre = tk.Text(sub_frame1, height=1, width=15, bd=2)
    texto_estatus = tk.Text(sub_frame1, height=1, width=15, bd=2)
    texto_telemark = tk.Text(sub_frame2, height=1, width=15, bd=2)
    texto_tijuana = tk.Text(sub_frame2, height=1, width=15, bd=2)
    texto_colroma = tk.Text(sub_frame2, height=1, width=15, bd=2)
    texto_villahermosa = tk.Text(sub_frame2, height=1, width=15, bd=2)
    texto_lapaz = tk.Text(sub_frame2, height=1, width=15, bd=2)
    texto_sanluis = tk.Text(sub_frame2, height=1, width=15, bd=2)
    texto_hermosillo = tk.Text(sub_frame2, height=1, width=15, bd=2)

    boton_cancelar = tk.Button(sub_frame3, width=10, text="Cancelar", command=root.destroy)
    boton_confirmar = tk.Button(sub_frame3, width=10, text="Confirmar")


    '''
    texto_codigo.insert(tk.INSERT, "Test")
    '''
    
    # ************************************************************************    
    # POSICIONAMIENTO DE WIDGETS
    # ************************************************************************
    label_codigo.grid(row=0, column=0, pady=[0, 10])
    texto_codigo.grid(row=0, column=1, padx=[10, 20], pady=[0, 10])
    boton_buscar.grid(row=0, column=2, pady=[0, 10], ipadx=5, ipady=5)

    label_sku.grid(row=1, column=0, padx=[0,10])
    label_nombre.grid(row=1, column=1, padx=[0,10])
    label_estatus.grid(row=1, column=2)
    label_telemark.grid(row=1, column=3, padx=[0,10])
    label_tijuana.grid(row=1, column=4, padx=[0,10])
    label_colroma.grid(row=1, column=5, padx=[0,10])
    label_villahermosa.grid(row=1, column=6, padx=[0,10])
    label_lapaz.grid(row=1, column=7, padx=[0,10])
    label_sanluis.grid(row=1, column=8, padx=[0,10])
    label_hermosillo.grid(row=1, column=9)

    texto_sku.grid(row=2, column=0, padx=[0,10], pady=[0,10])
    texto_nombre.grid(row=2, column=1, padx=[0,10], pady=[0,10])
    texto_estatus.grid(row=2, column=2, pady=[0,10])
    texto_telemark.grid(row=2, column=3, padx=[0,10])
    texto_tijuana.grid(row=2, column=4, padx=[0,10])
    texto_colroma.grid(row=2, column=5, padx=[0,10])
    texto_villahermosa.grid(row=2, column=6, padx=[0,10])
    texto_lapaz.grid(row=2, column=7, padx=[0,10])
    texto_sanluis.grid(row=2, column=8, padx=[0,10])
    texto_hermosillo.grid(row=2, column=9)

    boton_cancelar.grid(row=3, column=0, ipadx=5, padx=[0, 5], pady=[5, 10], ipady=5)
    boton_confirmar.grid(row=3, column=1, ipadx=5, padx=[5, 0], pady=[5, 10], ipady=5)


    # ************************************************************************
    # CONFIGURACION DE WODGETS
    # ************************************************************************
    texto_codigo.configure(font=("arial", 8))
    texto_sku.configure(font=("arial", 8))
    texto_nombre.configure(font=("arial", 8))
    texto_estatus.configure(font=("arial", 8))
    texto_telemark.configure(font=("arial", 8))
    texto_tijuana.configure(font=("arial", 8))
    texto_colroma.configure(font=("arial", 8))
    texto_villahermosa.configure(font=("arial", 8))
    texto_lapaz.configure(font=("arial", 8))
    texto_sanluis.configure(font=("arial", 8))
    texto_hermosillo.configure(font=("arial", 8))

    #***********************************************************************
    # FIN DE ROOT
    #*********************************************************************** 
    root.config(menu=menubar)   
    root.mainloop()