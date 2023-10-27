from os import system 
from metodo import Metodo

class Menu:
    def __init__(self):
        self.metodo = Metodo()

    
    def codigo_morse(self):
        system("cls")
        print("__________________________________________________")
        print("                                                  ")
        print("                  CODIGO MORSE                    ")
        print("__________________________________________________")
        print("                                                  ")
        print("         1: Texto a Morse                         ")
        print("         2: Morse a Texto                         ")
        print("__________________________________________________")
        print("                                                  ")
        opcion = int(input(" Elige una opcion: "))
        print("                                                  ")

        diccionario_morse = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            ' ': ' ',  # Espacio
        }


        if opcion == 1:
            mensaje = input(" Ingrese el mensaje en texto: ")
            codigo_morse = self.metodo.texto_a_codigo_morse(mensaje, diccionario_morse)
            print("__________________________________________________")
            print("                                                  ")
            print("     Mensaje en codigo Morse: ", codigo_morse)
            print("__________________________________________________")
            print("                                                  ")
            input("ENTER")

        elif opcion == 2:
            mensaje = input(" Ingrese el mensaje en codigo Morse (separa letras con espacio y palabra con '/'): ")
            codigo_traducido = self.metodo.morse_a_texto(mensaje, diccionario_morse)

            print("__________________________________________________")
            print("                                                  ")
            print("      Mensaje en texto: ", codigo_traducido)
            print("__________________________________________________")
            print("                                                  ")
            input("ENTER")

        else:
            print("__________________________________________________")
            print("                                                  ")
            print("                OPCION NO VALIDA                  ")
            print("__________________________________________________")
            

    def matriz(self):
        system("cls")
        print("__________________________________________________")
        print("                                                  ")
        print("                SELECCION MATRIZ                  ")
        print("__________________________________________________")
        print("                                                  ")

        matriz = self.metodo.crear_matriz()
        numeros_deshabilitados = 0
        while numeros_deshabilitados < 5:
            fila = int(input("Ingrese la fila (0-9): "))
            columna = int(input("Ingrese la columna (0,4): "))

            if 0 <= fila < 10 and 0 <= columna < 5:
                if self.metodo.deshabilitar_matriz(matriz, fila, columna):
                    numeros_deshabilitados += 1
                    print(f"Celda ({fila}, {columna}) deshabilitada.")
                    self.metodo.imprimir_matriz(matriz)

                else:
                    print("La celda ya esta deshabilitada. Elige otra.")

            else:
                print("Fila o columna fuera de rango. Intente nuevamente.")

        self.metodo.imprimir_matriz(matriz)
        input("ENTER")


    def mostrar_menu_principal(self):
        while True:
            system("cls")
            print("_______________________________________________________")
            print("                                                       ")
            print("                  OPCIONES                             ")
            print("_______________________________________________________")
            print("                                                       ")
            print("         1: Codigo Morse                               ")
            print("         2: Matriz                                     ")
            print("         0: Salir                                      ")
            print("_______________________________________________________")
            print("                                                       ")

            try:
                opcion = int(input("Digite la opcion: "))

                if opcion == 1:
                    self.codigo_morse()

                elif opcion == 2:
                    self.matriz()

                elif opcion == 0:
                    break

                else:
                    print("____________________________________________")
                    print("                                            ")
                    print("     ERROR - OPCION NO VALIDA               ")
                    print("____________________________________________")
                    print("                                            ")
                    input("ENTER")

            except ValueError:
                print("_________________________________________________")
                print("                                                 ")
                print("         ERROR - EL DATO DEBE DE SER ENTERO      ")
                print("_________________________________________________")
                print("                                                 ")
                input("ENTER")


if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu_principal()


    