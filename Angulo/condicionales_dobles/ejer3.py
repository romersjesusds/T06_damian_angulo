#EJER3
import os
#declaracion de variables
figura,base,altura,area="",0.0,0.0,0.0
verificador= False
#input
figura="triangulo"
base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])
#processing
area=(base*altura)/2
verificador=(area>=100)
#output
print("###############")
print("#figura:",figura)
print("area:",area)
#condicional
if(verificador):
    print("triangulo grande")
else:
    print("triangulo pequeño")
#fin_if
