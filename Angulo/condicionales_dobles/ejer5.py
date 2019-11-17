#EJER5
import os
#declaracion de variables
diagonal_mayor,diagonal_menor,area,figura =0.0,0.0,0.0,""
verificador= False
#input
figura="rombo"
diagonal_mayor=float(os.sys.argv[1])
diagonal_menor=float(os.sys.argv[2])
#processing
area=((diagonal_mayor*diagonal_menor)/2)
verificador=(area>=100)
#output
print("###############")
print("#figura:",figura)
print("#area:",area)
#condicional
if(verificador):
    print("rombo grande")
else:
    print("rombo pequeño")
#fin_if
