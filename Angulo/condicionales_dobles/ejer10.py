#EJER10
import os
#declaracion de variables
radio,pi,sup_esferica,figura =0.0,3.14159,0.0,""
verificador= False
#input
figura="esfera"
radio=float(os.sys.argv[1])
#processing
sup_esferica=4*pi*radio*radio
verificador=(sup_esferica<=200)
#output
print("###############")
print("#figura:",figura)
print("#area:",sup_esferica)
#condicional
if(verificador):
    print("esfera amplia")
else:
    print("esfera estrecha")
#fin_if
