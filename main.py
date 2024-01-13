#En py los objetos se crean usando clases 
#Los objetos nos ofrecen una "plantilla" para crear cosas

class Person: 
    def __init__(self,name,last_name,gender):
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.full_name = f"{name} {last_name}"


#Metodo --> "acciones" que puede hacer nuestro objeto
    def saluda(self): 
        print(f"Hola, me llamo: {self.full_name}, soy programador crack")

    def cambiar_nombre(self,new_name):
        self.name = new_name
        self.full_name = f"{new_name} {self.last_name}"

    def __repr__(self): 
        return f"name: {self.name}, last_name: {self.last_name}"
        
    def serialize(self):
        return{
            "name": self.name,
            "last_name": self.last_name,
        }

#Herencia --> se hereda el constructor y los metodos de un objeto ya creado
    
def impuestos(salary):
    return salary/2

class Empleado(Person):
    def __init__(self, name, last_name, gender, department, salary):
        super().__init__(name, last_name, gender)
        self.department = department
        self.salary = salary
    def saluda(self):
        print(f"gano {self.salary}")

    def calcular_impuestos(self):
        print(f"debo pagar: {impuestos(self.salary)} en impuestos")

empleado_uno = Empleado("Pedro", "Gomez", "Masculino", "Control de calidad", 30000)
empleado_uno.saluda()
empleado_uno.calcular_impuestos()

empleado_dos = Empleado("Valery", "Jimenez", "Femenino", "CEO", 80000000)
empleado_dos.saluda()
empleado_dos.calcular_impuestos()
    



        