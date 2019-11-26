t = float(input("Ingrese la temperatura en grados celsius: "))

Temp_f = lambda t: t*1.8 + 32
Temp_k = lambda t: t + 273.15

if __name__ == '__main__':

    print('La temperatura en grados farenheit es: ', Temp_f(t))
    print('La temperatura en grados kelvin es: ', Temp_k(t))