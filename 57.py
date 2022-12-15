import random
#57
num = random.randint(1,10)
correcto = Falso
while correcto == Falso:
    adivina = int(input("Introduce un numero: "))
 if adivina == num:
        correcto = verdadero 
 elif adivina > num:
    print ("muy alto")
 else:
    print ("muy bajo")