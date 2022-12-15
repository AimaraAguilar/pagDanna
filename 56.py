import random 
#56
num = random.randint(1,10)
correcto = Falso
while  corecto == Falso:
    adivina = int(input("Introduce un numero: "))
    if adivina == num:
        correcto = Verdadero