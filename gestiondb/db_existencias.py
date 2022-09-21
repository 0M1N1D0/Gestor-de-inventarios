import ntpath
import sqlite3
from tkinter import messagebox
import pandas as pd


def guardaExistencias(ruta):
    ruta_archivo = ruta
    nombre_archivo = ntpath.basename(ruta_archivo)
    nombre_archivo = nombre_archivo[:-5]

    # importar el archivo a pandas
    df = pd.read_excel(f"{ruta_archivo}")
    # print(df)

    # crea la conexion a sqlite
    conexion = sqlite3.connect("gestorInventariosdb.db")

    try:
        # el df de pandas se pasa a sqlite
        df.to_sql(name=nombre_archivo, con=conexion,
                  if_exists='replace', index=False)
        messagebox.showinfo(title="Importar archivo",
                            message="Archivo seleccionado actualizado correctamente en base de datos.")
    except:
        messagebox.showerror(title="Error de importación",
                             message="Ocurrió un error al importar el archivo seleccionado a la base de datos.")

    conexion.close()
