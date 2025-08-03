estudiantes={}
try:
    n=int(input("Ingrese la cantidad de estudiantes que desea registrar: "))
    for i in range(n):
        nombre=input(f"\nIngrese el nombre del estudiante #{i+1}:")
        cantidad=int(input("Ingrese la cantidad de notas para agregar: "))
        notas = []
        for j in range(cantidad):
            nota=int(input(f"Ingrese la nota No.{j+1} del estudiante: "))
            notas.append(nota)
        estudiantes[nombre]={"notas":notas}

    print("\n--NOTAS--")
    for nombre,datos in estudiantes.items():
        print(f"Estudiante: {nombre}")
        for i, nota in enumerate(datos["notas"]):
            print(f"Nota #{i+1}: {nota}")
        promedio=sum(datos["notas"])/len(datos["notas"])
        print(f"El promedio de {nombre} es: {promedio}")

except Exception as e:
    print("Ocurrio un erro inesperado")

finally:
    print(estudiantes)