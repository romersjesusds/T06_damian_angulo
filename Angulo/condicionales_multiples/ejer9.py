#EJER9
import os
#declaracion de variables
area_lateral2,area_base2,area_total2,figura =0.0,0.0,0.0,""
#input
figura="prisma"
area_lateral2=float(os.sys.argv[1])
area_base2=float(os.sys.argv[2])
#processing
area_total2=(area_lateral2+(2*area_base2))
#output
print("###############")
print("#figura:",figura)
print("#area:",area_total2)
#condicional
if(area_total2<=200 and area_total2>0 ):
    print("prisma con superficie estrecha")
if(area_total2>200 and area_total2<=250):
    print("prisma con superficie medianamente extensa")
if(area_total2>250):
    print("prisma con superficie extensa")
#fin_if
