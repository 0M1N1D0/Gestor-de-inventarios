
import sqlite3
import tkinter as tk
from tkinter import messagebox
import pandas as pd

def actualizar_estatus_shopping_mexico():

    # ************************************************************************
    # FUNCIONES
    # ************************************************************************

    # obtiene código y crea df. Valida info y manda llamar a funcion para mostrar info
    def obtener_producto():
        codigo = texto_codigo.get(1.0, "end-1c")

        # verifica que sea un numero entero
        try:
            codigo = int(codigo)
        except ValueError:
            messagebox.showwarning(message="Campo sin información.\nO carácteres incorrectos.")
            messagebox.showwarning(message="El código ingresado debe ser en formato CORBIZ (a 7 dígitos).\nEjemplo: 2603201")
            texto_codigo.delete("1.0", "end")
            root.focus_force()
        else:
            df_producto = df[df['SKU'] == codigo]

            '''
            validar cantidad total de campos vacíos, decuelve un int:
            total_vacios = df_producto.isnull().sum().sum()
            valida si el dataframe está vacío, devuelve un boolean:
            df_producto.empty
            '''

            if df_producto.empty:
                messagebox.showerror(message="El código ingresado no se encuentra en la base de datos.")
                messagebox.showwarning(message="El código ingresado debe ser en formato CORBIZ (a 7 dígitos).\nEjemplo: 2603201")
                texto_codigo.delete("1.0", "end")
                root.focus_force()

            
            mostrar_producto(df_producto)    

 
        
    def mostrar_producto(df_producto):
        index = df_producto.index
        texto_sku.insert(tk.INSERT, df_producto.loc[index[0], "SKU"])
        texto_nombre.insert(tk.INSERT, df_producto.loc[index[0], "Nombre del producto"])
        texto_estatus.insert(tk.INSERT, df_producto.loc[index[0], "Estatus principal"])
        texto_telemark.insert(tk.INSERT, df_producto.loc[index[0], "TELEMARK"])
        texto_tijuana.insert(tk.INSERT, df_producto.loc[index[0], "TIJUANA"])
        texto_colroma.insert(tk.INSERT, df_producto.loc[index[0], "COLROMA"])
        texto_villahermosa.insert(tk.INSERT, df_producto.loc[index[0], "VILLAHER"])
        texto_lapaz.insert(tk.INSERT, df_producto.loc[index[0], "LAPAZ"])
        texto_sanluis.insert(tk.INSERT, df_producto.loc[index[0], "SAN LUIS"])
        texto_hermosillo.insert(tk.INSERT, df_producto.loc[index[0], "HERMO"])


    def limpiar_campos():
        texto_sku.delete("1.0", "end")
        texto_nombre.delete("1.0", "end")
        texto_estatus.delete("1.0", "end")
        texto_telemark.delete("1.0", "end")
        texto_tijuana.delete("1.0", "end")
        texto_colroma.delete("1.0", "end")
        texto_villahermosa.delete("1.0", "end")
        texto_lapaz.delete("1.0", "end")
        texto_sanluis.delete("1.0", "end")
        texto_hermosillo.delete("1.0", "end")

        obtener_producto()


    def actualiza_datos():
        # obtiene los datos del Text Widget
        sku = texto_sku.get("1.0", "end")
        estatus_principal = texto_estatus.get("1.0", "end")
        estatus_telemark = texto_telemark.get("1.0", "end")
        estatus_tijuana = texto_tijuana.get("1.0", "end")
        estatus_colroma = texto_colroma.get("1.0", "end")
        estatus_villahermosa = texto_villahermosa.get("1.0", "end")
        estatus_lapaz = texto_lapaz.get("1.0", "end")
        estatus_sanluis = texto_sanluis.get("1.0", "end")
        estatus_hermosillo = texto_hermosillo.get("1.0", "end")

        # Obtiene el index del dato 
        index = df[df['SKU'] == int(sku)].index

        # actualiza los datos: 
        # el [:-1] es porque tkinter lo devuelve con un '\n' al final, y :-1 corta eso
        df.at[index[0], 'Estatus principal'] = estatus_principal[:-1] 
        df.at[index[0], 'TELEMARK'] = estatus_telemark[:-1] 
        df.at[index[0], 'TIJUANA'] = estatus_tijuana[:-1] 
        df.at[index[0], 'COLROMA'] = estatus_colroma[:-1] 
        df.at[index[0], 'VILLAHER'] = estatus_villahermosa[:-1] 
        df.at[index[0], 'LAPAZ'] = estatus_lapaz[:-1] 
        df.at[index[0], 'SAN LUIS'] = estatus_sanluis[:-1] 
        df.at[index[0], 'HERMO'] = estatus_hermosillo[:-1] 
   
        #print(df.at[index[0], 'Estatus principal'])

        try:
            df.to_sql(name='estatusShoppingMexico', con=conexion, if_exists='replace', index=False)
        except:
            messagebox.showerror(title="Error de importación",
                             message="Ocurrió un error al importar el archivo seleccionado a la base de datos.")
        else: 
            messagebox.showinfo(title="Actualizar estatus", message="Estatus actualizado(s) correctamente en base de datos.")
            root.focus_force()
        


    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return("break")


    def presionado(event):
        limpiar_campos()


    # ************************************************************************
    # CONEXION A DB Y CREACION DE DATAFRAME
    # ************************************************************************
    conexion = sqlite3.connect("gestorInventariosdb.db")
    df = pd.read_sql_query("SELECT * FROM estatusShoppingMexico", con=conexion)


    #***********************************************************************
    # CREACION DE ROOT
    #***********************************************************************
    root = tk.Tk()
    root.title("Estatus shopping por producto - México")
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
                -sub_frame4
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
    sub_frame4 = tk.Frame(label_frame)
    
    # ************************************************************************
    # POSICIONAMIENTO DE FRAMES
    # ************************************************************************
    frame1.grid(sticky="wn")
    frame2.grid(sticky="s")
    label_frame.grid()
    sub_frame1.grid(padx=10, sticky="w")
    sub_frame2.grid(padx=10, pady=[0,10])
    sub_frame3.grid()
    sub_frame4.grid(sticky="w")

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
    boton_buscar = tk.Button(frame1, text="Buscar", width=10, command=limpiar_campos)
    
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
    texto_nombre = tk.Text(sub_frame1, height=1, width=50, bd=2)
    texto_estatus = tk.Text(sub_frame1, height=1, width=15, bd=2)
    texto_telemark = tk.Text(sub_frame2, height=1, width=15, bd=2)
    texto_tijuana = tk.Text(sub_frame2, height=1, width=15, bd=2)
    texto_colroma = tk.Text(sub_frame2, height=1, width=15, bd=2)
    texto_villahermosa = tk.Text(sub_frame2, height=1, width=15, bd=2)
    texto_lapaz = tk.Text(sub_frame2, height=1, width=15, bd=2)
    texto_sanluis = tk.Text(sub_frame2, height=1, width=15, bd=2)
    texto_hermosillo = tk.Text(sub_frame2, height=1, width=15, bd=2)

    boton_cancelar = tk.Button(sub_frame3, width=10, text="Cancelar", command=root.destroy)
    boton_confirmar = tk.Button(sub_frame3, width=10, text="Confirmar", command=actualiza_datos)


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

    label_aviso = tk.Label(sub_frame4, text="En caso de confirmar actualización, recuerda actualizar el DRIVE.")
    label_aviso.grid(row=4, column=0)



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

    label_aviso.config(fg="blue")


    # ************************************************************************
    # COMPORTAMIENTOS
    # ************************************************************************
    texto_codigo.focus()
    texto_codigo.bind("<Tab>", focus_next_widget)
    boton_buscar.bind("<Return>", presionado)
    texto_sku.bind("<Tab>", focus_next_widget)
    texto_nombre.bind("<Tab>", focus_next_widget)
    texto_estatus.bind("<Tab>", focus_next_widget)
    texto_telemark.bind("<Tab>", focus_next_widget)
    texto_tijuana.bind("<Tab>", focus_next_widget)
    texto_colroma.bind("<Tab>", focus_next_widget)
    texto_villahermosa.bind("<Tab>", focus_next_widget)
    texto_lapaz.bind("<Tab>", focus_next_widget)
    texto_sanluis.bind("<Tab>", focus_next_widget)
    texto_hermosillo.bind("<Tab>", focus_next_widget)

    #***********************************************************************
    # FIN DE ROOT
    #*********************************************************************** 
    root.config(menu=menubar)   
    root.mainloop()