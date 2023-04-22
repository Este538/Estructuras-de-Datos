
from Pila import Pila

class Palindromo:
        __pila = Pila()
        __palabraIngresada = Pila()
        __pilaRespaldo = Pila()
        
        #Verificar si la pila se escribe igual por delante y por atrás
        def es_palindromo(palabra):
                palabra = palabra.lower()
                return palabra == palabra[::-1]

        def verificarCadena(self, cadena):
            for k in cadena:
                   if k != " ":
                          self.__palabraIngresada.insertar(k)
                          self.__pila.insertar(k) 
            
            while not self.__pila.esta_vacia():
                   self.__pilaRespaldo.insertar(self.__pila.quitar())

            while not self.__palabraIngresada.esta_vacia() and not self.__pilaRespaldo.esta_vacia() and self.__palabraIngresada.cima() == self.__pilaRespaldo.cima():
                 self.__pilaRespaldo.quitar()
                 self.__palabraIngresada.quitar() 
            
            if self.__palabraIngresada.esta_vacia():
                   print("Es Palindromo")
            else:
                   print("No es Palindromo")


