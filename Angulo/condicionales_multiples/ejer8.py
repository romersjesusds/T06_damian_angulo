#EJER8
import os
#declaracion de variables
area_lateral1,area_base1,area_total1,figura =0.0,0.0,0.0,""
#input
figura="cilindro"
area_lateral1=float(os.sys.argv[1])
area_base1=float(os.sys.argv[2])
#processing
area_total1=(area_lateral1+(2*area_base1))
#output
print("###############")
print("#figura:",figura)
print("area:",area_total1)
#condicional
if(area_total1<=200 and area_total1>0 ):
    print("cilindro con superficie estrecha")
if(area_total1>200 and area_total1<=250):
    print("cilindro con superficie medianamente extensa")
if(area_total1>250):
    print("cilindro con superficie extensa")
#fin_if
