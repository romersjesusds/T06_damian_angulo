#EJER7
import os
#declaracion de variables
base,altura,area,figura =0.0,0.0,0.0,""
verificador= False
#input
figura="rectangulo"
base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])
#processing
area=base*altura
verificador=(area>=100)
#output
print("###############")
print("#figura:",figura)
print("#area:",area)
#condicional
if(verificador):
    print("rectangulo grande")
else:
    print("rectangulo pequeño")
#fin_if
