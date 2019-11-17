#EJER9
import os
#declaracion de variables
area_lateral2,area_base2,area_total2,figura =0.0,0.0,0.0,""
verificador= False
#input
figura="prisma"
area_lateral2=float(os.sys.argv[1])
area_base2=float(os.sys.argv[2])
#processing
area_total2=(area_lateral2+(2*area_base2))
verificador=(area_total2>=200)
#output
print("###############")
print("#figura:",figura)
print("#area:",area_total2)
#condicional
if(verificador):
    print("el area del prisma es considerablemente grande")

#fin_if
