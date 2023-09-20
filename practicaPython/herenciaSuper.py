class Persona():
    
    def __init__(self, nombre, edad, Lugar_residencia):
        
        self.nombre=nombre
        self.edad=edad
        self.Lugar_residencia=Lugar_residencia
        
    def  descripcion(self):
        
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.Lugar_residencia)   
        
        
class Empleado(Persona):
    
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, Lugar_residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, Lugar_residencia_empleado)
        
        self.salario=salario
        self.antiguedad=antiguedad
        
    def descripcion(self):
        super().descripcion()
        
        print("Salario: ",self.salario,"Antigüedad: ", self.antiguedad)    
        
        
Antonio=Empleado(1600, 20, "Antonio", 55, "Venezuela")

Antonio.descripcion()  
#print(isinstance(Antonio, Empleado))     el metodo "isinstance" lo utilizamos para saber con que objeto esta instanciado        