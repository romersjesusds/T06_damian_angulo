import os
#declarar las variables
cliente,spa,servicio1,servicio2,costo_servicio1,costo_servicio2="","","","",0.0,0.0
total_pagar=False

#input
cliente=os.sys.argv[1]
spa=os.sys.argv[2]
servicio1=os.sys.argv[3]
servicio2=os.sys.argv[4]
costo_servicio1=int(os.sys.argv[5])
costo_servicio2=int(os.sys.argv[6])

#processing
costo=costo_servicio1+costo_servicio2
igv=costo*0.18
total_pagar=costo+igv
pago_limite=(total_pagar>60)

#output
print("#############################################################")
print("#  SPA - MI ANGELA			                               #")
print("#############################################################")
print("cliente:", cliente,               "spa:", spa)
print("#############################################################")
print("#")
print("#servicio 1:",servicio1)
print("#servicio 2", servicio2)
print("#precio servicio 1:", costo_servicio1)
print("precio servicio 2:", costo_servicio2)
print("#costo:", costo)
print("#IGV:", igv)
print("total a pagar:", total_pagar)
print("#############################################################")

#condicional

if(total_pagar>60):
    print("ha ganado un corte de cabello gratis")
else:
    print("vuelva pronto")

#fin_if
