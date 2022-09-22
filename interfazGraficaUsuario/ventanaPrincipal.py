# paquetes python
import tkinter as tk
# importaciones propias
from .ventanaImportarArchivo import importarArchivo
from .ventanaCentrosLogisticos import ventanaCentrosLogisticos
from .ventanaInventariogeneral import ventanaInventarioGeneral
from.ventanaExistencias import ventanaExistencias
from.ventanaActualizarEstatusShopping import actualizar_estatus_shopping


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
        actualizar = tk.Menu(menubar, tearoff=0)
        # importar.add_command(label="Existencias SAP", command=importarArchivo)
        actualizar.add_command(label="Centros logísticos", command=importarArchivo)          

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

        sub_estatus_shopping = tk.Menu(menubar, tearoff=0)
        sub_estatus_shopping.add_command(label="General", command=importarArchivo)
        sub_estatus_shopping.add_command(label="Por producto", command=actualizar_estatus_shopping)

        menubar.add_cascade(label="Actualizar", menu=actualizar)
        actualizar.add_cascade(label="Existencias SAP", menu=sub_inventario_general)
        actualizar.add_cascade(label="Inventario general",menu=sub_inventario_general)
        actualizar.add_cascade(label="Estatus shopping", menu=sub_estatus_shopping)

        consultar = tk.Menu(menubar, tearoff=0)
        consultar.add_command(label="Existencias SAP", command=ventanaExistencias)
        consultar.add_command(label="Estatus shopping")
        consultar.add_command(label="Centros logísticos", command=ventanaCentrosLogisticos)
        consultar.add_command(label="Inventario general", command=ventanaInventarioGeneral)
        menubar.add_cascade(label="Consultar", menu=consultar)

        root.config(menu=menubar)
        root.mainloop()
