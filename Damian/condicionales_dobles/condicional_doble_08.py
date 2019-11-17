import os
#declarar las variables
usuario,operadora_internet,gigas_usadas,costo_giga="","",0.0,0.0
gigas_usadas=False

#input
usuario=os.sys.argv[1]
operadora_internet=os.sys.argv[2]
gigas_usadas=int(os.sys.argv[3])
costo_giga=float(os.sys.argv[4])

#processing
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

if(gigas_usadas>50):
    print("advertencia: exeso consumo de datos, tenga mas cuidado")
else:
    print("gracias por consumir datos moderadamente")

#fin_if
