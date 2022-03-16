numeroNotas = int(input("ingrese el numero de notas a calcular\n"))
cont=1
notas=0
while cont <= numeroNotas:
    notas+=int(input(f"ingrese nota {cont}\n"))
    cont+=1
print(f"el promedio es {notas/numeroNotas}")


def Triangulos():
    lado1=input("ingrese lado 1")
    lado2=input("ingrese lado 2")
    lado3=input("ingrese lado 3")
    if lado1==lado2 and lado1==lado3:
        print("es equilatero")
    if lado1==lado2 and lado1!=lado3:
        print("es isoceles")
    else:
        print("es escaleno")

Triangulos()
