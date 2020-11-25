from os import system
system("cls")
área = input ("Dime si quieres que calculé el área de tu cuadrado o triángulo : ")
if (área == "cuadrado" or área == "CUADRADO" or área == "Cuadrado"):
    lado = float (input ("Dame la medida del lado : "))
    área = lado ** 2
    print ("El área de tu cuadrado es : " , área)
if (área == "triángulo" or área == "TRIÁNGULO" or área == "Triángulo"):
    base = float (input ("Dame la medida de la base : "))
    altura = float (input ("Dame la medida de la altura : "))
    área = (base * altura) / 2
    print ("El área de tu triángulo es : " , área)