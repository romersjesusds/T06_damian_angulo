#EJER1
import os
#declaracion de variables
nota01,nota02,nota03,nota04,curso=0.0,0.0,0.0,0.0,""
verificador= False
#input
curso=os.sys.argv[1]
nota01=float(os.sys.argv[2])
nota02=float(os.sys.argv[3])
nota03=float(os.sys.argv[4])
nota04=float(os.sys.argv[5])
#processing
promedio=float((nota01+nota02+nota03+nota04)/4)
verificador=(promedio>=11)
#output
print("###############")
print("#curso:",curso)
print("promedio:",promedio)
#condicional
if(verificador):
    print("Si estas aprobado")

#fin_if
