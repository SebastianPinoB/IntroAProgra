import csv
import json

#intento de eliminacion de branch

def abrirArchivo():
    with open("listado.csv", "r", encoding="utf-8") as archivo:
        datos = csv.DictReader(archivo)
        return list(datos)

def mostrar(diccionario):
    for i in diccionario:
        print(i)

def verificarGanadores(lista):
    ganadores = []
    for i in lista:
        if i["run"][-4:-2] == "92" or i["run"][-4:-2] == "95" or i["run"][-4:-2] == "84":
            ganadores.append(i)
    return ganadores

def archivoGanadores(ganadores):
    with open("ganadores.json","w") as archivo:
        json.dump(ganadores ,archivo, indent=1)

lista = abrirArchivo()
ganadores = verificarGanadores(lista)
archivoGanadores(ganadores)
