#EJER8
import os
#declaracion de variables
area_lateral1,area_base1,area_total1,figura =0.0,0.0,0.0,""
verificador= False
#input
figura="cilindro"
area_lateral1=float(os.sys.argv[1])
area_base1=float(os.sys.argv[2])
#processing
area_total1=(area_lateral1+(2*area_base1))
verificador=(area_total1>=200)
#output
print("###############")
print("#figura:",figura)
print("area:",area_total1)
#condicional
if(verificador):
    print("la superficie del cilindro es considerablemente grande")
#fin_if
