#inicializamos las variables
sum = 0
n = int(input())
num = []

#Corremos el proceso
for i in range(n):
    num.append(i)
    sum = sum + num[i]

#Desplegamos los resultados
print(num)
print(sum)
