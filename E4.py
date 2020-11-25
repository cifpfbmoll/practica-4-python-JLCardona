from os import system
system("cls")
num1 = float (input ("Dame el 1er número : "))
num2 = float (input ("Dame el 2o número : "))
num3 = float (input ("Dame el 3er número : "))
num4 = float (input ("Dame el 4o número : "))
if (num1 % num4 == 0):
    print ("El " , num4 , " es divisor de " , num1)
if (num2 % num4 == 0):
    print ("El " , num4 , " es divisor de " , num2)
if (num3 % num4 == 0):
    print ("El " , num4 , " es divisor de " , num3)