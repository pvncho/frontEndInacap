def Triangulos():
    lado1=input("ingrese lado 1")
    lado2=input("ingrese lado 2")
    lado3=input("ingrese lado 3")
    if lado1==lado2 and lado1==lado3:
        print("es equilatero")
    elif lado1==lado2 and lado1!=lado3:
        print("es isoceles")
    else:
        print("es escaleno")

Triangulos()