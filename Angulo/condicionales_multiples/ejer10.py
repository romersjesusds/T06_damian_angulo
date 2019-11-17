#EJER10
import os
#declaracion de variables
radio,pi,sup_esferica,figura =0.0,3.14159,0.0,""
#input
figura="esfera"
radio=float(os.sys.argv[1])
#processing
sup_esferica=4*pi*radio*radio
#output
print("###############")
print("#figura:",figura)
print("area:",sup_esferica)
#condicional
if(sup_esferica<=200 and sup_esferica>0 ):
    print("esfera con superficie estrecha")
if(sup_esferica>200 and sup_esferica<=250):
    print("esfera con superficie medianamente extensa")
if(sup_esferica>250):
    print("esfera con superficie extensa")
#fin_if
