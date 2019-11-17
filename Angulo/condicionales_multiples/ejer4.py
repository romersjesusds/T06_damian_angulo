#EJER4
import os
#declaracion de variables
base_menor,base_mayor,altura,area,figura =0.0,0.0,0.0,0.0,""


#input
figura="trapecio"
base_menor=float(os.sys.argv[1])
base_mayor=float(os.sys.argv[2])
altura=float(os.sys.argv[3])
#processing
area=((base_mayor*base_menor*altura)/2)
#output
print("###############")
print("#figura:",figura)
print("area:",area)
#condicional
if(area<=100 and area>0 ):
    print("trapecio pequeño")
if(area>100 and area<=150):
    print("trapecio mediano")
if(area>150):
    print("trapecio grande")
#fin_if
