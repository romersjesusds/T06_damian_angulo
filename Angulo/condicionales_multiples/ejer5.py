#EJER5
import os
#declaracion de variables
diagonal_mayor,diagonal_menor,area,figura =0.0,0.0,0.0,""
#input
figura="rombo"
diagonal_mayor=float(os.sys.argv[1])
diagonal_menor=float(os.sys.argv[2])
#processing
area=((diagonal_mayor*diagonal_menor)/2)
#output
print("###############")
print("#figura:",figura)
print("#area:",area)
#condicional
if(area<=100 and area>0 ):
    print("rombo pequeño")
if(area>100 and area<=150):
    print("rombo mediano")
if(area>150):
    print("rombo grande")
#fin_if
