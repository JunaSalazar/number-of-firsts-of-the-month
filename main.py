import io
import time
import re
import os, fnmatch
import sys
import locale
from datetime import datetime

list = []
nameCount = []
indiviualName = []
data = []

# Metodo donde se abre el archivo INI, se obtiene la informacion
# y se realiza el conteo para obtener los nombres y la cantidad de veces que estos se repiten
# almacenandolos en una lista, y ordenandolos de manera decendnente por el numero en la segunda columna utilizando
# la funcion LAMBDA.
def read_file():
    file1 = open("file.ini", 'r')
    lines = file1.readlines()

    list = []
    nameCount = []
    indiviualName = []
    data = []

    try:
        for line in reversed(lines):
            list = re.split(r"\t+", line)

        linea = list[0]
        linea = linea.replace("[", "")
        linea = linea.replace("]", "")
        names = linea.split(",")

        for name in names:
            if (not indiviualName):
                indiviualName.append(name)
                nameCount.append(1)
            elif (name in indiviualName):
                nameCount[indiviualName.index(name)] += 1
            else:
                indiviualName.append(name)
                nameCount.append(1)

        for name in indiviualName:
            data.append([name, nameCount[indiviualName.index(name)]])

        data = sorted(data, key=lambda data: data[1], reverse=True)
        return data
    except Exception as e:
        # Closing file
        print("Fallo: ", e)
        file1.close()

# Metodo para obtener el mes y el año actual, se escribe de la siguiente manera MESAÑO
def get_month_and_year():
    date_month = datetime.today().strftime('%b').upper()
    date_month = date_month.replace(".","")
    date_year = datetime.today().strftime('%Y')
    date = date_month+date_year
    return date

# Metodo para escribir archivo, si existe el archivo se re-escribe, si no existe se crea uno nuevo
def write_file(data):
    print("")

locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))
data = read_file()
write_file(data)
print(data)

