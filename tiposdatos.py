print("Clases V2 Nicolas")
# el constructor funcion
class Datos:
    print("")
    def __init__(self,estatura,peso):
        self.estatura = estatura
        self.peso = peso
    def mostrar_datos(self):
        print(f"Estatura : {self.estatura} mts, peso {self.peso} kg")
    
    # listas
    def mi_lista(self):
        mylista=["Ford","Chevrolet","Mustang"]
        print(mylista)
        for autos in mylista:
            print(autos)

    # Tuplas
    def mi_tupla(self):
        mitupla=("Gamesa","Marinela","Cuetara")
        print(mitupla)
        for cuki in mitupla:
            print(cuki)

    # Diccionario
    def mi_diccionario (self):
        midicc = {
            "Martin:" "19",
            "Anais:" "14",
            "Nicolas:" "16" 
            }
        print(midicc)
        for x in midicc:
            print(x)

    # Set
    def mi_set(self):
        miset = {"Pug","Bulldog","Pitbull"}
        print(miset)
        for dog in miset:
            print(dog)

# Creacion de objeto info
info=Datos(1.75,70.5)

# Utilizando el obj.
info.mostrar_datos()
print("")
print(" -lista- ")
print("Lista de marcas de Autos")
info.mi_lista()
print("")
print(" -Tupla- ")
print("lista de Galletas")
info.mi_tupla()
print("")
print(" -Diccionario- ")
print("Mis Hermanos")
info.mi_diccionario()
print("")
print(" -Set- ")
print("Raza de perros")
info.mi_set()
