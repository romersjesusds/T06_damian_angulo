import os
#declarar las variables
velocidad_1,velocidad_2,distancia=0.0,0.0,0.0
tiempo_previsto=False

#input
velocidad_1=int(os.sys.argv[1])
velocidad_2=int(os.sys.argv[2])
distancia=int(os.sys.argv[3])

#processing
tiempo_encuentro=(distancia)/(velocidad_1+velocidad_2)
tiempo_previsto=(tiempo_encuentro>10)

#output
print("####################################################")
print("#    CALCULO DEL TIEMPO DE ENCUENTRO     #")
print("####################################################")
print("#")
print("#velocidad primer movil:", velocidad_1, "m/s")
print("#velocidad segundo movil:", velocidad_2, "m/s")
print("#distancia de separacion:", distancia, "metros")
print("#tiempo de encuentro:", tiempo_encuentro)
print("#")
print("#####################################################")

#condicional
#considerando que la distancia es al misma para todos los casos

if(tiempo_encuentro>10 and tiempo_encuentro<15):
    print("genial, eso si fue rapido")
if(tiempo_encuentro>=15 and tiempo_encuentro<25):
    print("eso estuvo un poco lento")
if(tiempo_encuentro>=25):
    print("demaciado lento")

#fin_if
