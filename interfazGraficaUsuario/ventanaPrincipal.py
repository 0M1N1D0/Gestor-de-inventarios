# paquetes python
import tkinter as tk
# importaciones propias
from .ventanaImportarArchivo import importarArchivo
from .ventanaCentrosLogisticos import ventanaCentrosLogisticos
from .ventanaInventariogeneral import ventanaInventarioGeneral
from .ventanaExistencias import ventanaExistencias
from .estatus_shopping.estatusShoppingMexico import actualizar_estatus_shopping_mexico
from .ventanaEstatusShopping import ventanaEstatusShopping
from .ventanaEstatusDP import estatusDP


def ventanaPrincipal():


    def importarCentroLog():
        importarArchivo('Paises')

    def importarArchivoArg():
        importarArchivo('Argentina')
    def importarArchivoBol():
        importarArchivo('Bolivia')
    def importarArchivoBra():
        importarArchivo('Brasil')
    def importarArchivoChi():
        importarArchivo('Chile')
    def importarArchivoCol():
        importarArchivo('Colombia')
    def importarArchivoCR():
        importarArchivo('Costa Rica')
    def importarArchivoDom():
        importarArchivo('Dominicana')
    def importarArchivoEcu():
        importarArchivo('Ecuador')
    def importarArchivoSal():
        importarArchivo('El Salvador')
    def importarArchivoEsp():
        importarArchivo('España')
    def importarArchivoGua():
        importarArchivo('Guatemala')
    def importarArchivoHon():
        importarArchivo('Honduras')
    def importarArchivoIta():
        importarArchivo('Italia')
    def importarArchivoMex():
        importarArchivo('México')
    def importarArchivoNic():
        importarArchivo('Nicaragua')
    def importarArchivoNig():
        importarArchivo('Nigeria')
    def importarArchivoPan():
        importarArchivo('Panamá')
    def importarArchivoPar():
        importarArchivo('Paraguay')
    def importarArchivoPer():
        importarArchivo('Perú')
    def importarArchivoRus():
        importarArchivo('Rusia')
    def importarArchivoUru():
        importarArchivo('Uruguay')
    def importarArchivoUSA():
        importarArchivo('USA')
    



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
    actualizar.add_command(label="Centros logísticos", command=importarCentroLog)          

    sub_inventario_general = tk.Menu(menubar, tearoff=0)
    sub_inventario_general.add_command(label='Argentina', command=importarArchivoArg)
    sub_inventario_general.add_command(label='Bolivia', command=importarArchivoBol)
    sub_inventario_general.add_command(label='Brasil', command=importarArchivoBra)
    sub_inventario_general.add_command(label='Chile', command=importarArchivoChi)
    sub_inventario_general.add_command(label='Colombia', command=importarArchivoCol)
    sub_inventario_general.add_command(label='Costa Rica', command=importarArchivoCR)
    sub_inventario_general.add_command(label='Dominicana', command=importarArchivoDom)
    sub_inventario_general.add_command(label='Ecuador', command=importarArchivoEcu)
    sub_inventario_general.add_command(label='El Salvador', command=importarArchivoSal)
    sub_inventario_general.add_command(label='España', command=importarArchivoEsp)
    sub_inventario_general.add_command(label='Guatemala', command=importarArchivoGua)
    sub_inventario_general.add_command(label='Honduras', command=importarArchivoHon)
    sub_inventario_general.add_command(label='Italia', command=importarArchivoIta)
    sub_inventario_general.add_command(label='México', command=importarArchivoMex)
    sub_inventario_general.add_command(label='Nicaragua', command=importarArchivoNic)
    sub_inventario_general.add_command(label='Nigeria', command=importarArchivoNig)
    sub_inventario_general.add_command(label='Panamá', command=importarArchivoPan)
    sub_inventario_general.add_command(label='Paraguay', command=importarArchivoPar)
    sub_inventario_general.add_command(label='Perú', command=importarArchivoPer)
    sub_inventario_general.add_command(label='Rusia', command=importarArchivoRus)
    sub_inventario_general.add_command(label='Uruguay', command=importarArchivoUru)
    sub_inventario_general.add_command(label='USA', command=importarArchivoUSA)


    sub_estatus_shopping_pais = tk.Menu(menubar, tearoff=0)
    sub_estatus_shopping_pais.add_command(label='Argentina')
    sub_estatus_shopping_pais.add_command(label='Bolivia')
    sub_estatus_shopping_pais.add_command(label='Brasil')
    sub_estatus_shopping_pais.add_command(label='Chile')
    sub_estatus_shopping_pais.add_command(label='Colombia')
    sub_estatus_shopping_pais.add_command(label='Costa Rica')
    sub_estatus_shopping_pais.add_command(label='Dominicana')
    sub_estatus_shopping_pais.add_command(label='Ecuador')
    sub_estatus_shopping_pais.add_command(label='El Salvador')
    sub_estatus_shopping_pais.add_command(label='España')
    sub_estatus_shopping_pais.add_command(label='Guatemala')
    sub_estatus_shopping_pais.add_command(label='Honduras')
    sub_estatus_shopping_pais.add_command(label='Italia')
    sub_estatus_shopping_pais.add_command(label='México', command=actualizar_estatus_shopping_mexico)
    sub_estatus_shopping_pais.add_command(label='Nicaragua')
    sub_estatus_shopping_pais.add_command(label='Nigeria')
    sub_estatus_shopping_pais.add_command(label='Panamá')
    sub_estatus_shopping_pais.add_command(label='Paraguay')
    sub_estatus_shopping_pais.add_command(label='Perú')
    sub_estatus_shopping_pais.add_command(label='Rusia')
    sub_estatus_shopping_pais.add_command(label='Uruguay')
    sub_estatus_shopping_pais.add_command(label='USA')

    sub_estatus_shopping = tk.Menu(menubar, tearoff=0)
    sub_estatus_shopping.add_cascade(label="General", menu=sub_inventario_general)
    sub_estatus_shopping.add_cascade(label="Por producto", menu=sub_estatus_shopping_pais)

    sub_estatus_dp = tk.Menu(menubar, tearoff=0)
    sub_estatus_dp.add_command(label="México", command=importarArchivoMex)

    menubar.add_cascade(label="Actualizar", menu=actualizar)
    actualizar.add_cascade(label="Existencias SAP", menu=sub_inventario_general)
    actualizar.add_cascade(label="Inventario general",menu=sub_inventario_general)
    actualizar.add_cascade(label="Estatus shopping", menu=sub_estatus_shopping)
    actualizar.add_cascade(label="Estatus DP", menu=sub_estatus_dp)

    consultar = tk.Menu(menubar, tearoff=0)
    consultar.add_command(label="Existencias SAP", command=ventanaExistencias)
    consultar.add_command(label="Estatus shopping", command=ventanaEstatusShopping)
    consultar.add_command(label="Centros logísticos", command=ventanaCentrosLogisticos)
    consultar.add_command(label="Inventario general", command=ventanaInventarioGeneral)
    consultar.add_command(label="Estatus DP", command=estatusDP)
    menubar.add_cascade(label="Consultar", menu=consultar)

    root.config(menu=menubar)
    root.mainloop()
