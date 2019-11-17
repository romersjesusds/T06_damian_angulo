import os
#declarar las variables
cliente,vendedor,kg_papas,precio_kg="","",0.0,0.0
consumo_limite=False

#input
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
kg_papas=int(os.sys.argv[3])
precio_kg=float(os.sys.argv[4])

#processing
consumo_total=kg_papas*precio_kg
igv=consumo_total*0.18
total_pagar=consumo_total+igv
consumo_limite=(total_pagar>100)

#output
print("#############################################################")
print("#	BODEGA  -       MI FERNANDITO			    #")
print("#############################################################")
print("cliente:", cliente,    "     vendedor:", vendedor)
print("#############################################################")
print("#")
print("#item:", kg_papas, "kg de papas")
print("#Precio por kg: s/.", precio_kg)
print("#consumo: s/.", consumo_total)
print("#IGV: s/.", igv)
print("total a pagar: s/.", total_pagar)
print("#############################################################")

#condicional

if(total_pagar>100 and total_pagar<=200):
    print("llevese una gaseosa pepsi personal por solo 0.1 centimos")
if(total_pagar>200 and total_pagar<300):
    print("ud. ha ganado una gaseosa pepsi familiar")
if(total_pagar>=300):
    print("felicitaciones, se ha ganado un fuerte abrazo del vendedor")

#fin_if
