#EJER6
import os
#declaracion de variables
radio,pi,area,figura =0.0,3.14159,0.0,""
verificador= False
#input
figura="circulo"
radio=float(os.sys.argv[1])
#processing
area=pi*radio*radio
verificador=(area>=100)
#output
print("###############")
print("#figura:",figura)
print("#area:",area)
#condicional
if(verificador):
    print("circulo grande")
else:
    print("circulo pequeño")
#fin_if
