import os
#declarar las variables
velocidad_1,velocidad_2,distancia=0.0,0.0,0.0
tiempo_previsto=False

#input
velocidad_1=int(os.sys.argv[1])
velocidad_2=int(os.sys.argv[2])
distancia=int(os.sys.argv[3])

#processig
tiempo_alcance=(distancia)/(velocidad_2-velocidad_1)
tiempo_previsto=(tiempo_alcance>15)
#output
print("####################################################")
print("#    CALCULO DEL TIEMPO DE ALCANCE     #")
print("####################################################")
print("#")
print("#velocidad primer movil:", velocidad_1, "m/s")
print("#velocidad segundo movil:", velocidad_2, "m/s")
print("#distancia de separacion:", distancia, "metros")
print("#tiempo de alcance:", tiempo_alcance, "segundos")
print("#")
print("#####################################################")

#condicional
if(tiempo_alcance>15):
    print("felicidades, a cimplido el tiempo previsto")

#fin_if
