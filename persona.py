class Persona:
    def __init__(self, nombre, apellidos, edad, sexo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        
    def __str__(self):
        '''
        Representación textual informal.
        '''
        return self.nombre + " " + self.apellidos

    def __repr__(self):
        '''
        Representación formal.
        '''
        return f"Persona({self.nombre!r}, {self.apellidos!r}, {self.edad!r}, {self.sexo!r})"
    
    def saludar(self):
        print("Hola, me llamo", self.nombre)
