import os
#declarar las variables
velocidad_1,velocidad_2,distancia=0.0,0.0,0.0
tiempo_encuentro=False

#input
velocidad_1=int(os.sys.argv[1])
velocidad_2=int(os.sys.argv[2])
distancia=int(os.sys.argv[3])

#processing
tiempo_encuentro=(distancia)/(velocidad_1+velocidad_2)
tiempo_exacto=(tiempo_encuentro==10)

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

if(tiempo_encuentro==10):
    print("que buen calculo!")
else:
    print("que mal calculo, aprenda mas")

#fin_if
