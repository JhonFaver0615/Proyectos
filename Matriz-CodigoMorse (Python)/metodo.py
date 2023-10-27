
class Metodo:
    
    def __init__(self):
        self.mensaje_morse = []
        self.mensaje_texto = []
    

#MORSE 

    def texto_a_codigo_morse(self, mensaje, diccionario_morse):
        mensaje = mensaje.upper()
        
        for i in mensaje:
            if i in diccionario_morse:
                self.mensaje_morse.append(diccionario_morse[i])
        return ' '.join(self.mensaje_morse)
    

    

    def morse_a_texto(self, mensaje, diccionario_morse):
        mensaje = mensaje.split(' ')
        
        for codigo in mensaje:
            for i, mensaje_char in diccionario_morse.items():
                if codigo == mensaje_char:
                    self.mensaje_texto.append(i)
        return ''.join(self.mensaje_texto)


#Matriz 

    def crear_matriz(self):
        matriz = [[0 for x in range(5)] for y in range(10)]
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                matriz[i][j] = i * 5 + j

        return matriz
    
    def deshabilitar_matriz(self,matriz, fila, columna):
        if matriz[fila][columna] != -1:
            matriz[fila][columna] = -1
            return True 
        else:
            return False 
        
    def imprimir_matriz(self, matriz):
        for fila in matriz:
            for elemento in fila:
                if elemento == -1:
                    print("X", end=" ")
                else:
                    print(elemento, end=" ")
            print()