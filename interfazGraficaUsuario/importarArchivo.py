import tkinter as tk
from tkinter.ttk import Separator

def importarArchivo():

    ventana = tk.Tk() 

    # ************* Configuración de ventana ***************
    ventana.title("Importar archivo")
    ventana.geometry("280x125")
    ventana.iconbitmap("interfazGraficaUsuario\icono2.ico")
    ventana.resizable(False, False)
    ventana.focus_force()

    # labelSeleccionaArchivo = tk.Label(ventana, text="Selecciona el arhivo:")
    # labelSeleccionaArchivo.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    botonBuscar = tk.Button(ventana, text="Buscar archivo", width="35")
    botonBuscar.grid(row=0, columnspan=2, padx=15, pady=10, sticky="w")

    labelMostrarRuta = tk.Label(ventana, text="Ruta seleccionada: ")
    labelMostrarRuta.grid(row=1, column=0, padx=15, sticky="w")

    botonCancelar = tk.Button(ventana, text="Cancelar", width="15")
    botonCancelar.grid(row=3, column=0, padx=15, pady=10, sticky="w")

    botonAceptar = tk.Button(ventana, text="Aceptar", width="15")
    botonAceptar.grid(row=3, column=1, pady=10, sticky="w")


    ventana.mainloop()