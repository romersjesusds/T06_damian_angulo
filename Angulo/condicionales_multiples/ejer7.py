#EJER7
import os
#declaracion de variables
base,altura,area,figura =0.0,0.0,0.0,""
#input
figura="rectangulo"
base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])
#processing
area=base*altura
#output
print("###############")
print("#figura:",figura)
print("#area:",area)
#condicional
if(area<=100 and area>0 ):
    print("reectangulo pequeño")
if(area>100 and area<=150):
    print("rectangulo mediano")
if(area>150):
    print("rectangulo grande")
#fin_if
