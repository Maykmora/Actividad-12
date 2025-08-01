estudiantes={}

try:
    n=int(input("Ingrese la cantidad de estudiantes que desea registrar: "))
    for i in range(n):
        nombre=input("Ingrese el nombre del estudiante:")
        cantidad=int(input("Ingrese la cantidad de notas para agregar: "))
        for j in range(cantidad):
            nota=int(input(f"Ingrese la nota No.{i+1} del estudiante: "))
    estudiantes[nombre]={"notas":nota}

except Exception as e:
    print("Ocurrio un erro inesperado")

finally:
    print(estudiantes)