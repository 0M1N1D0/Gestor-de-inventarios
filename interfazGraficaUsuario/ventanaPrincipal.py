# paquetes python
import tkinter as tk
#importaciones propias
from .importarArchivo import importarArchivo
from .ventanaCentrosLogisticos import ventanaCentrosLogisticos

class VentanaPrincipal:

    def __init__(self):
        # raiz
        root = tk.Tk()
        # titulo
        root.title("Gestor de inventarios")
        #********* confogurcion de ventana *********** 
        # y posicionamiento en el centro
        anchoVentana = 500
        altoVentana = 25

        # obteniendo largo y ansho de pantalla
        anchoPantalla = root.winfo_screenwidth()
        # altoPantalla = root.winfo_screenheight()

        # encontrando el punto medio del ancho de la pantalla 
        centroEjeX = int(anchoPantalla / 2 - anchoVentana / 2)
        ejeY = 50

        # centrando la pantalla en el eje x
        root.geometry(f'{anchoVentana}x{altoVentana}+{centroEjeX}+{ejeY}')
        # prohíbe el cambio de tamaño
        root.resizable(False, False)
        # ******************************************************

        # icono
        root.iconbitmap("interfazGraficaUsuario\icono2.ico")

        # ***************** menu bar **************************
        menubar = tk.Menu(root)

        importar = tk.Menu(menubar, tearoff=0) # tearoff=0 elimina linea superior
        importar.add_command(label="Existencias SAP")
        importar.add_command(label="Estatus shopping")
        importar.add_command(label="Centros logísticos", command=importarArchivo)
        menubar.add_cascade(label="Actualizar", menu=importar)

        visualizacionAnalisis = tk.Menu(menubar, tearoff=0)
        visualizacionAnalisis.add_command(label="Existencias SAP")
        visualizacionAnalisis.add_command(label="Estatus shopping")
        visualizacionAnalisis.add_command(label="Centros logísticos", command=ventanaCentrosLogisticos)
        menubar.add_cascade(label="Visualización y análisis", menu=visualizacionAnalisis)

        root.config(menu=menubar)
        root.mainloop()