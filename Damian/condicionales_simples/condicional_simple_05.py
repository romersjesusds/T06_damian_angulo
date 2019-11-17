import os
#declarar las variables
cliente,tienda,nro_chompas,pu="","",0.0,0.0
limite=False

#input
cliente=os.sys.argv[1]
tienda=os.sys.argv[2]
nro_chompas=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#processing
pago_chompas=nro_chompas*pu
igv=pago_chompas*0.18
total_pagar=pago_chompas+igv
limite=(nro_chompas>50)

#output
print("#############################################################")
print("#    Tienda -  ABRIGOS QUE ABRIGAN			    #")
print("#############################################################")
print("cliente:", cliente             ,"     tienda:", tienda)
print("#############################################################")
print("#")
print("#item:", nro_chompas, "chompas")
print("#P.U.: s/.", pu)
print("#pago por chompas: s/.", pago_chompas)
print("#IGV: s/.", igv)
print("total a pagar: s/.", total_pagar)
print("#############################################################")

#condicional
if(nro_chompas>50):
    print("ud. a superado el limite de adquisicion del producto")

#fin_if
