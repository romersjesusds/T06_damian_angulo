#EJER3
import os
#declaracion de variables
figura,base,altura,area="",0.0,0.0,0.0
#input
figura="triangulo"
base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])
#processing
area=(base*altura)/2
#output
print("###############")
print("#figura:",figura)
print("area del triangulo:",area)
#condicional
if(area<=100 and area>0):
    print("triangulo pequeño")
if(area>100 and area<=150):
    print("triangulo mediano")
if(area>150):
    print("triangulo grande")
#fin_if
