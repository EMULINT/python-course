import math
# Determinación de un numero primo
print("Número a evaluar?")
n = int(input())
divisor = 2 # se iniciara con 2 hasta llegar a la raíz de un numero
          # A menos que se encuentre antes el numero exacto

while(divisor <= math.sqrt(n)):
    cociente = n/divisor #Verificar con cada divisor posible
    if n == cociente*divisor:
        divisor = n+1
    else:
        divisor = divisor + 1 #Tal vez sea primo
                              #Verifica el siguiente

if divisor >= n:
    print("No es primo")
else:
    print("Si es primo") #Se corrieron los posibles divisores