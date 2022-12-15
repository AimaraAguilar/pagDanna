re = int(input("¿Qué volumen quiere conocer de un cono o una piramide?, 1=cono 2=piramide "))
import math

if re == 2:
    print("coloque el ancho, largo y altura, para conocer el volumen de la piramide (en ese orden)")
    an = float(input())
    la = float(input())
    l = float(input())
    Vp = (an*la*l)/3
    print ("El volumen de su piramide es: ")
    print (round(Vp, 2))

elif re == 1:
    print("coloque el radio y altura (en ese orden)")
    ra = float(input())
    h = float(input())
    rra = ra**2
    Vc = (math.pi*rra*h)/3
    print ("El volumen de su cono es: ")
    print (round (Vc, 2))
else:
    print ("Dulce o truco")
    

 
   


       




