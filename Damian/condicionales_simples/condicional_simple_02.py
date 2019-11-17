import os
#declararar la variable
cliente,cajero,pares_zapatos,pares_zapatillas,pares_tacones,precio_par_zapatos,precio_par_zapatillas,precio_par_tacones="","",0.0,0.0,0.0,0.0,0.0,0.0
comprador_compulsivo=False

#input
cliente=os.sys.argv[1]
cajero=os.sys.argv[2]
pares_zapatos=int(os.sys.argv[3])
pares_zapatillas=int(os.sys.argv[4])
pares_tacones=int(os.sys.argv[5])
precio_par_zapatos=float(os.sys.argv[6])
precio_par_zapatillas=float(os.sys.argv[7])
precio_par_tacones=float(os.sys.argv[8])

#processing
consumo_zapatos=pares_zapatos*precio_par_zapatos
consumo_zapatillas=pares_zapatillas*precio_par_zapatillas
consumo_tacones=pares_tacones*precio_par_tacones
consumo_total=consumo_zapatos+consumo_zapatillas+consumo_tacones
IGV=consumo_total*0.18
total_pagar=consumo_total+IGV
comprador_compulsivo=(total_pagar>1000)

#output
print("#############################################################")
print("   ZAPATERIA - DAMIAN      ")
print("#############################################################")
print("cliente:", cliente               ,"cajero:", cajero)
print("#############################################################")
print("producto	        cantidad	     P.U.	             total")
print("#zapatos:",      pares_zapatos   ,precio_par_zapatos ,consumo_zapatos)
print("#zapatillas:",   pares_zapatillas ,precio_par_zapatillas ,consumo_zapatillas)
print("#tacones:",      pares_tacones    ,precio_par_tacones    ,consumo_tacones)
print("#############################################################")
print("#consumo:", consumo_total)
print("#IGV:", IGV)
print("total a pagar:", total_pagar)
print("#############################################################")

#condicional

if(total_pagar>1000):
    print("ud. es un comprador compulsivo")

#fin_if
