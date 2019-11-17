import os
#declarar las variables
cliente,empresa_azucarera,quintales_azucar,precio_quintal="","",0.0,0.0
comerciante=False

#input
cliente=os.sys.argv[1]
empresa_azucarera=os.sys.argv[2]
quintales_azucar=int(os.sys.argv[3])
precio_quintal=float(os.sys.argv[4])

#processing
total=quintales_azucar*precio_quintal
igv=total*0.18
total_pagar=total+igv

#output
print("#############################################################")
print("#           AZUCAR       POMALCA		           #")
print("#############################################################")
print("cliente:", cliente          ,"empresa azucarera:", empresa_azucarera)
print("#############################################################")
print("#")
print("#item:", quintales_azucar, "quintales de azucar")
print("#P.U.:", precio_quintal)
print("#total:", total)
print("#IGV:", igv)
print("total a pagar:", total_pagar)
print("#############################################################")

#condicional

if(total_pagar>100 and total_pagar<300):
    print("gracias amigo(a) comerciante por preferirnos")
if(total_pagar>=300 and total_pagar<500):
    print("ha ganado medio quintal de azucar")
if(total_pagar>=500):
    print("ha ganado un quintal de azucar")

#fin_if
