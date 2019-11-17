#EJER6
import os
#declaracion de variables
radio,pi,area,figura =0.0,3.14159,0.0,""
#input
figura="circulo"
radio=float(os.sys.argv[1])
#processing
area=pi*radio*radio
#output
print("###############")
print("#figura:",figura)
print("#area:",area)
#condicional
if(area<=100 and area>0 ):
    print("circulo pequeño")
if(area>100 and area<=150):
    print("circulo mediano")
if(area>150):
    print("circulo grande")
#fin_if
