# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "BRIAN-FERNANDEZ"
__date__ = "$19/10/2015 05:27:40 PM$"

puntero=0
final=9
vec = [3,8,11,22,38,49,50,56,62,70]
encontro = False

numero = int(input("Favor ingresar un numero: "))

while ( not(encontro) and puntero <= final):
    
    mitad =  int( (puntero + final) / 2)
    
    if(numero == vec[mitad] ):
        encontro = True
    
    elif(numero < vec [mitad] ):
        final = mitad  - 1
    else:
        puntero = mitad + 1
        
        
if (encontro):
    print("El dato se encuentra y esta en la posicion: " + str(mitad + 1))
else:
    print("El dato no se encuentra")
