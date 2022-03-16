numeroNotas = int(input("ingrese el numero de notas a calcular\n"))
cont=1
notas=0
while cont <= numeroNotas:
    notas+=int(input(f"ingrese nota {cont}\n"))
    cont+=1
print(f"el promedio es {notas/numeroNotas}")


