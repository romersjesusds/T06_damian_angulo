#EJER4
import os
#declaracion de variables
base_menor,base_mayor,altura,area,figura =0.0,0.0,0.0,0.0,""
verificador= False
#input
figura="trapecio"
base_menor=float(os.sys.argv[1])
base_mayor=float(os.sys.argv[2])
altura=float(os.sys.argv[3])
#processing
area=((base_mayor*base_menor*altura)/2)
verificador=(area>=100)
#output
print("###############")
print("#figura:",figura)
print("#area:",area)
#condicional
if(verificador):
    print("trapecio grande")
else:
    print("trapecio pequeño")
#fin_if
