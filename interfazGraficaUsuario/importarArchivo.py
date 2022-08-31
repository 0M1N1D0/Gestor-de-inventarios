import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def importarArchivo():

    # funcion que abre ventana para seleccionar archivo a importar
    def buscarArchivo():
        archivo= filedialog.askopenfilename(title="Seleciona archivo", initialdir="/")
        
        # si archivo tiene contenido, muestra el messagebox, cambia de color el label respuesta
        # y guarda la ruta en la variable ruta
        if archivo: 
            messagebox.showinfo(title="Imprtar archivo", message="Archivo seleccionado correctamente.")
            respuesta = "Sí"
            labelRespuesta.config(fg="blue")
            labelRespuesta.config(text=respuesta)
            ruta = archivo
            print("buscarArchivo ruta", ruta)


    # raiz
    ventana = tk.Tk() 
    #variable global que se mostrará en el label
    respuesta = "No"
    



    # ************* Configuración de ventana ***************
    ventana.title("Importar")
    ventana.geometry("240x125")
    ventana.iconbitmap("interfazGraficaUsuario\icono2.ico")
    ventana.resizable(False, False)
    ventana.focus_force()

    # labelSeleccionaArchivo = tk.Label(ventana, text="Selecciona el arhivo:")
    # labelSeleccionaArchivo.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    labelSeleccion = tk.Label(ventana, text="Archivo a importar:")  
    labelSeleccion.grid(row=0, column=0, padx=15)

    botonBuscar = tk.Button(ventana, text="Buscar", width="10", command=buscarArchivo)
    botonBuscar.grid(row=0, column=1, pady=10)

    labelMostrarRuta = tk.Label(ventana, text="Archivo seleccionado:")
    labelMostrarRuta.grid(row=1, column=0, padx=15, sticky="e")

    labelRespuesta = tk.Label(ventana, text=respuesta)
    labelRespuesta.grid(row=1, column=1, sticky="w")
    labelRespuesta.config(fg="red")

    botonCancelar = tk.Button(ventana, text="Cancelar", width="10", command=ventana.destroy)
    botonCancelar.grid(row=3, column=0, padx=15, pady=10, sticky="e")

    botonAceptar = tk.Button(ventana, text="Guardar", width="10")
    botonAceptar.grid(row=3, column=1, pady=10, sticky="w")


    ventana.mainloop()