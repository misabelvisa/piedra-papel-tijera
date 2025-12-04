import random

puntos_usuario = 0
puntos_maquina = 0

opciones = ["piedra", "papel", "tijera"]

while True:
    eleccion_usuario = input("Elige piedra, papel, tijera... o Q para salir: ").lower()
    if eleccion_usuario == "q":
        break

    if eleccion_usuario not in opciones:
        continue

    random_numero = random.randint(0,2)
    eleccion_maquina = opciones[random_numero]
    print("La máquina ha elegido " + eleccion_maquina + ".")
    if eleccion_usuario == "piedra" and eleccion_maquina == "tijera":
        puntos_usuario +=1
        print("Tu ganas!\nPuntos usuario:", puntos_usuario,"  Puntos máquina:", puntos_maquina)
    
        
    elif eleccion_usuario == "papel" and eleccion_maquina == "piedra":
        puntos_usuario +=1
        print("Tu ganas!\nPuntos usuario:", puntos_usuario,"  Puntos máquina:", puntos_maquina)
    elif eleccion_usuario == "tijera" and eleccion_maquina == "papel":
        puntos_usuario +=1
        print("Tu ganas!\nPuntos usuario:", puntos_usuario,"  Puntos máquina:", puntos_maquina)
    elif eleccion_usuario == eleccion_maquina:
        print("Empate :)")
    else:
        puntos_maquina +=1
        print("La máquina gana!\nPuntos usuario:", puntos_usuario,"  Puntos máquina:", puntos_maquina)

print("Hasta la próxima.")