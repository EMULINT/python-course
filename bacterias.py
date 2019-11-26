import math

#Población de una colonia de bacterias
'''
Se calcula el número de día en que la población 
de una colonia de bacterias se duplica
'''
nd = 1 #Numero de dias
M0 = 10 #Población inicial
Mmax = int(input("Dame la población máxima: \n"))

while M0 <=Mmax:
    M0 = 2*M0
    if M0<= Mmax: #Checa si todavía no llega al máximo
        nd += 2 # Se incrementa el numero de días en 2

print("El número de días es ", nd)
print("La población de bacterias es ", M0)



