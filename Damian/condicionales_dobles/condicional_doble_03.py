import os
#declarar las variables
cliente,florista,ramos_flores,pu="","",0.0,0.0
ramos_flores=False

#input
cliente=os.sys.argv[1]
florista=os.sys.argv[2]
ramos_flores=int(os.sys.argv[3])
pu=float(os.sys.argv[4])
#processing
consumo_total=ramos_flores*pu
igv=consumo_total*0.18
total_pagar=consumo_total+igv


#output
print("#############################################################")
print("#	FLORERIA - MI ROSA      ")
print("#############################################################")
print("cliente:", cliente               ,"florista:", florista)
print("#############################################################")
print("#")
print("#item:", ramos_flores, "ramos de flores")
print("#P.U.: s/.", pu)
print("#consumo: s/.", consumo_total)
print("#IGV: s/.", igv)
print("total a pagar: s/.", total_pagar)
print("#############################################################")

#condicional

if(ramos_flores>60):
    print("oferta: ud. ha ganado un ramo de flores")
else:
    print("siga intentando")

#fin_if
