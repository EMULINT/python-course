import math

a = float(input('Ingrese el valor de a: '))
b = float(input('Ingrese el valor de b: '))
c = float(input('Ingrese el valor de c: '))

determinante = b*b - 4*(a*c)

if determinante < 0:
    print("x1 y x2 son valores imaginarios")
if  determinante == 0.0:
    x = -b/(2*a)
    print("La ecuación solo tiene una solución x = ", x)
    
if determinante > 0:
    raiz = math.sqrt(determinante)
    x1 = (-b + raiz)/(2*a)
    x2 = (-b - raiz)/(2*a)
    print("La ecuación tiede dos soluciones x1= ",x1," x2= ",x2)

