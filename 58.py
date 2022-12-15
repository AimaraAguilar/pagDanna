import random
#58
puntaje = 0
for i in range (1,6):
    num1  =  random.randint(1,50)
    num2  =  random.randint(1,50)
    correcto = num1 + num2
    print (num1, "+", num2, "= ")
    respuesta = int(input("tu respuesta: "))
    print()
    if respuesta == correcto:
        puntaje = puntaje + 1
print ("Tu puntaje", puntaje, "fuera de 5")
