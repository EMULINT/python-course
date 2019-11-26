class convert_temp:
    Temp_c = 0.0
    
    def __init__(self, temp_c):
        self.Temp_c = temp_c
        
    def conv_celsius_farenheit(self):
        return self.Temp_c*1.8 + 32

    def conv_celsius_kelvin(self):
        return self.Temp_c + 273.15

   






