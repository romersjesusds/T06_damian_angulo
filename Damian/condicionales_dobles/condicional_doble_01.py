import os
#declarar variables
cliente,cajero,botellas,pu="","",0.0,0.0
total_pagar=False

#input
cliente=os.sys.argv[1]
cajero=os.sys.argv[2]
botellas=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#processing
consumo_total=botellas*pu
igv=consumo_total*0.18
total_pagar=consumo_total+igv


#output
print("#############################################################")
print("#	BOLETA	   DE	   VENTA			    #")
print("#############################################################")
print("cliente:", cliente              , "cajero:", cajero)
print("#############################################################")
print("#")
print("#item:", botellas, "botellas de aceite")
print("#P.U.: s/.", pu, "c/u")
print("#consumo:", consumo_total)
print("#IGV: s/.", igv)
print("total a pagar: s/.", total_pagar)
print("#############################################################")


#condicional

if(total_pagar>300):
    print("felicitaciones, ud. ha ganado 30% de descuento en su proxima compra")
else:
    print("vuelva pronto")

#fin_if
