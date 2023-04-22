class Pila:
    #constructor
    def __init__(self):
        self.elementos = []

    #insertar un elemento
    def insertar (self, dato):
        self.elementos.append(dato)
    
    #Está vacía
    def esta_vacia (self):
        return len(self.elementos) == 0

    #Sacar un elemento
    def quitar(self):
        if self.esta_vacia():
            print(" La lista está vacía ")
            return None
        return self.elementos.pop()
    
    #limpiar la pila
    def limpiar(self):
        del self.elementos[:]

    #Cima de la pila
    def cima(self):
        if self.esta_vacia():
            print(" La lista está vacía ")
            return None
        else:
            return self.elementos[-1]
    
    #Tamaño de los elementos
    def tamanho(self):
        return len(self.elementos)

    #Mostrar elementos
    def mostrar(self):
        print(" Los elementos de la pila son: ")
        print(self.elementos)

        

