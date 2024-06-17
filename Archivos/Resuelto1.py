import csv


with open("datos.csv", "r") as archivo:
    datos = csv.DictReader(archivo)
    mayores = []
    menores = []

    for i in datos:
        if int(i["Edad"]) >= 18:
            mayores.append(i)
        else:
            menores.append(i)

    print("Mayores")
    for i in mayores:
        print(i)

    print("Menores")
    for i in menores:
        print(i)
