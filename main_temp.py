from temp import convert_temp

t = float(input("Ingrese la temperatura en grados celsius: "))
temp = convert_temp(t)

if __name__ == '__main__':
    conv_c_f = temp.conv_celsius_farenheit()
    conv_c_k = temp.conv_celsius_kelvin()
    print('La temperatura en grados farenheit: ', conv_c_f)
    print('La temperatura en grados kelvin: ', conv_c_k)

