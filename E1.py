from os import system
system("cls")
num1 = float (input ("Dame el 1er número : "))
num2 = float (input ("Dame el 2o número : "))
num3 = float (input ("Dame el 3er número : "))
num4 = float (input ("Dame el 4o número : "))
num5 = float (input ("Dame el 5o número : "))
máx = mín = num1
if (num2 > máx):
    máx = num2
else:
    if (num2 < mín):
        mín = num2
if (num3 > máx):
    máx = num3
else:
    if (num3 < mín):
        mín = num3
if (num4 > máx):
    máx = num4
else:
    if (num4 < mín):
        mín = num4
if (num5 > máx):
    máx = num5
else:
    if (num5 < máx):
        máx = num5

print (máx, " es el mayor y " , mín , " es el menor")