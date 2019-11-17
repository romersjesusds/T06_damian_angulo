import os
#declarar las variables
usuario,operadora_internet,gigas_usadas,costo_giga="","",0.0,0.0
gigas_limite=False

#input
usuario=os.sys.argv[1]
operadora_internet=os.sys.argv[2]
gigas_usadas=int(os.sys.argv[3])
costo_giga=float(os.sys.argv[4])
total=gigas_usadas*costo_giga
igv=total*0.18
total_pagar=total+igv
gigas_limite=(gigas_usadas>50)

#output
print("#############################################################")
print("#	BITEL- TELEFONIA DE TODOS			                   #")
print("#############################################################")
print("cliente:", usuario,             "operadora:", operadora_internet)
print("#############################################################")
print("#")
print("#gigas usadas:", gigas_usadas)
print("#costo por giga:", costo_giga)
print("#total:", total)
print("#IGV:", igv)
print("total a pagar:", total_pagar)
print("#############################################################")

#condicional

if(gigas_usadas>50 and gigas_usadas<100):
    print("usted usa moderadamente el internet")
if(gigas_usadas>=100 and gigas_usadas<300):
    print("modere su uso de internet")
if(gigas_usadas>=300):
    print("le exegimos moderar su uso de internet")

#fin_if
