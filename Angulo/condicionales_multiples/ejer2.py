#EJER2
import os
#declaracion de variables
precio01,precio02,precio03,precio04 =0.0,0.0,0.0,0.0
#input
producto="arroz"
precio01=float(os.sys.argv[1])
precio02=float(os.sys.argv[2])
precio03=float(os.sys.argv[3])
precio04=float(os.sys.argv[4])
#processing
precio_promedio=float((precio01+precio02+precio03+precio04)/4)
#output
print("###############")
print("#producto:",producto)
print("precio promedio:",precio_promedio)
#condicional
if(precio_promedio<=2.00):
    print("arroz de calidad baja")
if(precio_promedio>2.00 and precio_promedio<=3.00):
    print("arroz de calidad media")
if(precio_promedio>3.00 and precio_promedio<=3.50):
    print("arroz de buena calidad")
#fin_if
