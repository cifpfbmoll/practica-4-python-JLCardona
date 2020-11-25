from os import system
system("cls")
num1 = float (input ("Dame el 1er número : "))
num2 = float (input ("Dame el 2o número : "))
num3 = float (input ("Dame el 3er número : "))
num4 = float (input ("Dame el 4o número : "))
num5 = float (input ("Dame el 5o número : "))
if (num1 > num2) and (num2 > num3) and (num3 > num4) and (num4 > num5) :
    print ("!Números DECRECIENTES¡")
elif(num1 < num2) and (num2 < num3) and (num3 < num4) and (num4 < num5) :
    print ("!Números CRECIENTES¡")
else:
    print ("!Números DESORDENADOS¡")