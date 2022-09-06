import tkinter as tk
import ntpath # determina el nombre del archivo de la ruta especificada
from tkinter import filedialog
from turtle import width

from gestiondb.db_centrosLogisticos import guardarCentrosLogisticos
from gestiondb.db_inventarioGeneral import guardaInventarioGeneral
from gestiondb.db_existencias import guardaExistencias


def importarArchivo():

    # funcion que abre ventana para seleccionar archivo a importar
    def buscarArchivo():
        archivo= filedialog.askopenfilename(title="Seleciona archivo", initialdir="/")
        
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
        #print("ruta", ruta)
        nonlocal nombreArchivo
        nombreArchivo = ntpath.basename(ruta)
        #print("nombreArchivo", nombreArchivo)


    def guardarEnDB():
        if nombreArchivo == "centrosLogisticos.xlsx":
            guardarCentrosLogisticos(rutaArchivo)
            ventana.destroy()
        elif nombreArchivo == "inventarioGeneral.xlsx":
            guardaInventarioGeneral(rutaArchivo)
            ventana.destroy()
        elif nombreArchivo == "existencias.xlsx":
            guardaExistencias(rutaArchivo)
            ventana.destroy()


    # dependiendo del nombre del arhicvo
    # def determinaDB():
    #     print("determinaRutaDB ", archivo)


    # raiz
    ventana = tk.Tk() 
    #variable global que se mostrará en el label
    respuesta = "No"
    rutaArchivo: str
    nombreArchivo: str
 


    # ************* Configuración de ventana ***************
    ventana.title("Importar")
    # ventana.geometry("260x135")
    ventana.iconbitmap("interfazGraficaUsuario\icono2.ico")
    ventana.resizable(False, False)
    ventana.focus_force()

    labelFrame = tk.LabelFrame(ventana)
    labelFrame.grid(padx=[15,15], pady=[10,0], columnspan=2)

    # *********** menu bar **********************
    menubar = tk.Menu(ventana)

    archivo = tk.Menu(menubar, tearoff=0)
    archivo.add_command(label="Cerrar", command=ventana.destroy)
    menubar.add_cascade(label="Archivo", menu=archivo)

    ayuda = tk.Menu(menubar, tearoff=0)
    ayuda.add_command(label="Manual de usuario")
    menubar.add_cascade(label="Ayuda", menu=ayuda)
    # ********************************************

    # labelSeleccionaArchivo = tk.Label(ventana, text="Selecciona el arhivo:")
    # labelSeleccionaArchivo.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    labelSeleccion = tk.Label(labelFrame, text="Archivo a importar:")  
    labelSeleccion.grid(row=0, column=0, padx=15, sticky="e")

    botonBuscar = tk.Button(labelFrame, text="Buscar", width="10", command=buscarArchivo)
    botonBuscar.grid(row=0, column=1, padx=[0,10], pady=10)

    labelMostrarRuta = tk.Label(labelFrame, text="Archivo seleccionado:")
    labelMostrarRuta.grid(row=1, column=0, padx=15, pady=[0,10], sticky="e")

    labelRespuesta = tk.Label(labelFrame, text=respuesta)
    labelRespuesta.grid(row=1, column=1, sticky="w", pady=[0,10])
    labelRespuesta.config(fg="red")

    botonCancelar = tk.Button(ventana, text="Cancelar", width="10", command=ventana.destroy)
    botonCancelar.grid(row=3, column=0, padx=15, pady=[10, 15], sticky="e")

    botonGuardar = tk.Button(ventana, text="Guardar", width="10", command=guardarEnDB)
    botonGuardar.grid(row=3, column=1, pady=[10, 15], sticky="w")

    ventana.config(menu=menubar)
    ventana.mainloop()