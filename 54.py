import random
#54
mone = random.choice(  [ "h", "t"] )
adivina = input ("Ingrese (h)eads o (t)ails: ")
if adivina == mone:
    print("GANASTE")
else:
    print("MALA SUERTE, NIMODILLO")
if mone == "h":
    print ("Fue heads")
else:
    print ("Fue tails")       
