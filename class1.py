#Inicio de la clase
class Hola:
    Nombre = ' '
    Apellido = ' '

    def __init__(self, nombre, apellido):
        self.Nombre = nombre
        self.Apellido = apellido
    
    def saludar(self):
        return "Hola " + self.Nombre + " "+ self.Apellido