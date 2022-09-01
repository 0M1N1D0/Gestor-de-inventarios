import sqlite3
from tkinter import messagebox
import pandas as pd


def guardarCentrosLogisticos(ruta):

    rutaArchivo = ruta

    # importar el archivo a pandas
    df = pd.read_excel(f"{rutaArchivo}")
    # print(df)

    # crea la conexion a sqlite
    conexion = sqlite3.connect("gestorInventariosdb.db")

    try:
        # el df de pandas se pasa a sqlite 
        df.to_sql(name="centrosLogisticos", con=conexion, if_exists='replace', index=False)
        messagebox.showinfo(title="Importar archivo", message="Archivo seleccionado actualizado correctamente en base de datos.")
    except:
        messagebox.showerror(title="Error de importación", message="Ocurrió un error al importar el archivo seleccionado a la base de datos.")


    conexion.close()

    # def importCentrosLogisticos(rutaArchivo):
    #     print(rutaArchivo)  