import csv
def abrirArchivo():
    with open("datos.csv", "r") as archivo:
        datos = csv.DictReader(archivo)
        return list(datos)

def mayoresDeEdad(datos):
    mayores = []
    for i in datos:
        if int(i["Edad"]) >= 18:
            mayores.append(i)
    return mayores

def menoresDeEdad(datos):
    menores = []
    for i in datos:
        if int(i["Edad"]) < 18:
            menores.append(i)
    return menores

def mostrar(lista):
    for i in lista:
        print(i)

datos = abrirArchivo()
menores = menoresDeEdad(datos)
print("MENORES : ")
mostrar(menores)
print(" ")
mayores = mayoresDeEdad(datos)
print("MAYORES : ")
mostrar(mayores)