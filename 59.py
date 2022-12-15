import random 
#59
colour = random.choice(["rojo","azul","verde","blanco","rosa"])
print ("Selccionar de rojo, azul, verde, blanco o rosa")
input ()
Intentadenuevo = verdadero
while Intentadenuevo == verdadero:
      sueleccion = input("introduce un color: ")
      sueleccion = sueleccion.lower()
      if color == sueleccion:
        print("Bien hecho")
        Intentadenuevo = Falso
      else:
        if colour == "rojo":
            print ("apuesto a que ahora mismo ves rojo")
        elif colour == "azul":
            print ("no sientas azul")
        elif colour == "verde":
            print ("apuesto a que ahora mismo ves verde con envidia")
        elif colour == "blanco":
            print ("eres blanco como una hoja, no lo adivinaste correctamente?")
        elif colour == "rosa":
            prin("que pena que no te sientas rosa, por haber perdido")
