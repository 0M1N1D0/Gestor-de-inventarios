# paquetes python
import tkinter as tk
# importaciones propias
from .ventanaImportarArchivo import importarArchivo
from .ventanaCentrosLogisticos import ventanaCentrosLogisticos
from .ventanaInventariogeneral import ventanaInventarioGeneral
from.ventanaExistencias import ventanaExistencias


class VentanaPrincipal:

    def __init__(self):
        # raiz
        root = tk.Tk()
        # titulo
        root.title("Gestor de inventarios")
        # ********* confogurcion de ventana ***********
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

        # ***************** MENU BAR **************************
        menubar = tk.Menu(root)

        # tearoff=0 elimina linea superior
        importar = tk.Menu(menubar, tearoff=0)
        # importar.add_command(label="Existencias SAP", command=importarArchivo)
        importar.add_command(label="Estatus shopping")
        importar.add_command(label="Centros logísticos",
                             command=importarArchivo)

        sub_inventario_general = tk.Menu(menubar, tearoff=0)
        
        sub_inventario_general.add_command(
            label='Argentina', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Bolivia', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Brasil', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Chile', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Colombia', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Costa Rica', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Dominicana', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Ecuador', command=importarArchivo)
        sub_inventario_general.add_command(
            label='El Salvador', command=importarArchivo)
        sub_inventario_general.add_command(
            label='España', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Guatemala', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Honduras', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Italia', command=importarArchivo)
        sub_inventario_general.add_command(
            label='México', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Nicaragua', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Nigeria', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Panamá', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Paraguay', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Perú', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Rusia', command=importarArchivo)
        sub_inventario_general.add_command(
            label='Uruguay', command=importarArchivo)
        sub_inventario_general.add_command(
            label='USA', command=importarArchivo)

        menubar.add_cascade(label="Actualizar", menu=importar)
        importar.add_cascade(label="Existencias SAP", 
                             menu=sub_inventario_general)
        importar.add_cascade(label="Inventario general",
                             menu=sub_inventario_general)

        visualizacionAnalisis = tk.Menu(menubar, tearoff=0)
        visualizacionAnalisis.add_command(
            label="Existencias SAP", command=ventanaExistencias)
        visualizacionAnalisis.add_command(label="Estatus shopping")
        visualizacionAnalisis.add_command(
            label="Centros logísticos", command=ventanaCentrosLogisticos)
        visualizacionAnalisis.add_command(
            label="Inventario general", command=ventanaInventarioGeneral)
        menubar.add_cascade(label="Consultas", menu=visualizacionAnalisis)

        root.config(menu=menubar)
        root.mainloop()
