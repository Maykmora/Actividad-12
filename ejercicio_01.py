estudiantes={}
notas=[]
try:
    n=int(input("Ingrese la cantidad de estudiantes que desea registrar: "))
    for i in range(n):
        nombre=input(f"Ingrese el nombre del estudiante #{i+1}:")
        cantidad=int(input("Ingrese la cantidad de notas para agregar: "))
        for j in range(cantidad):
            nota=int(input(f"Ingrese la nota No.{j+1} del estudiante: "))
            notas.append(nota)
    estudiantes[nombre]={"notas":[nota]}

    print("\n--NOTAS--")
    for

except Exception as e:
    print("Ocurrio un erro inesperado")

finally:
    print(estudiantes)