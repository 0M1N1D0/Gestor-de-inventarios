import tkinter as tk
import ntpath  # determina el nombre del archivo de la ruta especificada
from tkinter import filedialog

from gestiondb.db_centrosLogisticos import guardarCentrosLogisticos
from gestiondb.db_inventarioGeneral import guardaInventarioGeneral
from gestiondb.db_existencias import guardaExistencias


def importarArchivo():
    
    # ************************************************************************
    # FUNCIONES
    # ************************************************************************
    
    # funcion que abre ventana para seleccionar archivo a importar
    def buscarArchivo():
        archivo = filedialog.askopenfilename(
            title="Seleciona archivo", initialdir="/")

        # si archivo tiene contenido, muestra el messagebox, cambia de color el label respuesta
        # y guarda la ruta en la variable ruta
        if archivo:
            # messagebox.showinfo(title="Imprtar archivo", message="Archivo seleccionado correctamente.")
            respuesta = "Sí"
            labelRespuesta.config(fg="blue")
            labelRespuesta.config(text=respuesta)
            nonlocal rutaArchivo
            rutaArchivo = archivo
            determinarNombreArchivo(rutaArchivo)

    # dependiendo del nombre del archivo, pasa la ruta al archivo
    # db correspondiente para su ingreso

    def determinarNombreArchivo(ruta):
        nonlocal nombreArchivo
        nombreArchivo = ntpath.basename(ruta)

    def guardarEnDB():
        if nombreArchivo == "centrosLogisticos.xlsx":
            guardarCentrosLogisticos(rutaArchivo)
            ventana.destroy()
        elif nombreArchivo.startswith("inventarioGeneral"):
            guardaInventarioGeneral(rutaArchivo)
            ventana.destroy()
        elif nombreArchivo.startswith("existencias"):
            guardaExistencias(rutaArchivo)
            ventana.destroy()
        elif nombreArchivo.startswith("estatusShopping"):
            guardaExistencias(rutaArchivo)
            ventana.destroy()


    # ************************************************************************
    # CREACION DE ROOT
    # ************************************************************************
    ventana = tk.Tk()
    # variable global que se mostrará en el label
    respuesta = "No"
    rutaArchivo: str
    nombreArchivo: str
    ventana.title("Importar")
    # ventana.geometry("260x135")
    ventana.iconbitmap("interfazGraficaUsuario\icono2.ico")
    ventana.resizable(False, False)
    ventana.focus_force()

    labelFrame = tk.LabelFrame(ventana)
    labelFrame.grid(padx=[15, 15], pady=[10, 0], columnspan=2)

    # ************************************************************************
    # MENU BAR
    # ************************************************************************
    menubar = tk.Menu(ventana)

    archivo = tk.Menu(menubar, tearoff=0)
    archivo.add_command(label="Cerrar", command=ventana.destroy)
    menubar.add_cascade(label="Archivo", menu=archivo)

    ayuda = tk.Menu(menubar, tearoff=0)
    ayuda.add_command(label="Manual de usuario")
    menubar.add_cascade(label="Ayuda", menu=ayuda)
    
    # ************************************************************************
    # CREACION DE WIDGETS
    # ************************************************************************
    labelSeleccion = tk.Label(labelFrame, text="Archivo a importar:")
    botonBuscar = tk.Button(labelFrame, text="Buscar",
                            width="10", command=buscarArchivo)
    labelMostrarRuta = tk.Label(labelFrame, text="Archivo seleccionado:")
    labelRespuesta = tk.Label(labelFrame, text=respuesta)
    botonCancelar = tk.Button(ventana, text="Cancelar",
                              width="10", command=ventana.destroy)
    botonGuardar = tk.Button(ventana, text="Guardar",
                             width="10", command=guardarEnDB)
    
    # ************************************************************************
    # POSICIONAMIENTO DE WIDGETS
    # ************************************************************************
    labelSeleccion.grid(row=0, column=0, padx=15, sticky="e")
    botonBuscar.grid(row=0, column=1, padx=[0, 10], pady=10)
    labelMostrarRuta.grid(row=1, column=0, padx=15, pady=[0, 10], sticky="e")
    labelRespuesta.grid(row=1, column=1, sticky="w", pady=[0, 10])
    botonCancelar.grid(row=3, column=0, padx=15, pady=[10, 15], sticky="e")
    botonGuardar.grid(row=3, column=1, pady=[10, 15], sticky="w")
    
    # ************************************************************************
    # CONFIGURACIONES DE WIDGETS
    # ************************************************************************
    labelRespuesta.config(fg="red")
    
    # ************************************************************************
    # FIN DE ROOT
    # ************************************************************************
    ventana.config(menu=menubar)
    ventana.mainloop()
