from os import system
system("cls")
importe = int (input ("Dame el importe : "))
if (importe % 500 == 0):
    billetes = importe / 500
    print ("El cajero devolverá " , billetes , " de 500 euros")
elif (importe % 200 == 0):
    billetes = importe / 200
    print ("El cajero devolverá " , billetes , " de 200 euros")
elif (importe % 100 == 0):
    billetes = importe / 100
    print ("El cajero devolverá " , billetes , " de 100 euros")
elif (importe % 50 == 0):
    billetes = importe / 50
    print ("El cajero devolverá " , billetes , " de 50 euros")
elif (importe % 20 == 0):
    billetes = importe / 20
    print ("El cajero devolverá " , billetes , " de 20 euros")
elif (importe % 10 == 0):
    billetes = importe / 10
    print ("El cajero devolverá " , billetes , " de 10 euros")
elif (importe % 5 == 0):
    billetes = importe / 5
    print ("El cajero devolverá " , billetes , " de 5 euros")