#EJER2
import os
#declaracion de variables
precio01,precio02,precio03,precio04 =0.0,0.0,0.0,0.0
verificador= False
#input
producto="arroz"
precio01=float(os.sys.argv[1])
precio02=float(os.sys.argv[2])
precio03=float(os.sys.argv[3])
precio04=float(os.sys.argv[4])
#processing
precio_promedio=float((precio01+precio02+precio03+precio04)/4)
verificador=(precio_promedio<=3.5)
#output
print("###############")
print("#producto:",producto)
print("precio promedio:",precio_promedio)
#condicional
if(verificador):
    print("el precio del arroz el aceptable para el comprador")
#fin_if
