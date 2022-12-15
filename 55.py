import random 
#55
num1 = random.randint(1,5)
adivina = int(input("numero:"))
if adivina == num1:
    print("Well done")
elif adivina > num1:
    print ("Muy alto")
    adivina = int(input("Adivina de nuevo: "))
    if adivina == num1:
        print("CORRECTO")
    else:
        print("PERDISTE")
elif adivina < num1:
    print("Muy bajo")     
    adivina = int(input("Adivina de nuevo:"))
    if adivina == num1:
        print("CORRECTO")
    else:
        print("you lose")
