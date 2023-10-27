from os import system
from socio import Socio
from videoclub import VideoClub
from pelicula import Pelicula
from pedido import Pedido




class Menu: # La clase siempre se inicia en mayuscula, con el mismo nombre con que se guardo.

	def __init__(self): # El init es el constructor de la clase. El self es el que permite el trabajo de los objetos.
		self.videoclub = VideoClub()

	def adicionar_socio(self):
		system("cls") # Es la limpieza de la consola.
		print("______________________________________________________________")
		print("                                                              ")
		print("                      ADICIONAR SOCIO                         ")
		print("______________________________________________________________")
		print("                                                              ")	
		codigo = input("Ingrese su Numero de Documento: ") 
		nombre = input("Ingrese su Nombre Completo con Apellidos: ")
		telefono = input("Ingrese su Numero de Telefono de Celular: ")
		direccion = input("Ingrese su Direccion de Residencia: ")
		
		#Instancia de la clase.
		#socio -> objeto
		#Socio -> clase
		socio  = Socio(codigo, nombre, telefono, direccion)

		if self.videoclub.adicionar_socio(socio):
			print("______________________________________________________________")
			print("                                                              ")
			print("         INFO - EL SOCIO SE ADICIONO CORRECTAMENTE.           ")
			print("______________________________________________________________")
			print("                                                              ")	
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")	
			print("                 ERROR - EL SOCIO YA EXISTE.                  ")
			print("______________________________________________________________")
			print("                                                              ")	
			input("ENTER")	

	def listar_socios(self):

		system("cls") 
		print("______________________________________________________________")
		print("                                                              ")
		print("                      LISTAR SOCIOS                           ")
		print("______________________________________________________________")
		print("                                                              ")
		self.videoclub.listar_socios()
		input("ENTER")

	def modificar_socio(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                       MODIFICAR SOCIO                        ")
		print("______________________________________________________________")
		print("                                                              ")
		codigo = input("Ingrese el Codigo del Socio que Desea Buscar: ")

		if self.videoclub.modificar_socio(codigo): 
			print("______________________________________________________________")
			print("                                                              ")
			print("            INFO - LOS DATOS FUERON MODIFICADOS.              ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("           ERROR - LOS DATOS NO SE PUEDEN MODIFICAR.          ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")	

	def eliminar_socio(self): 
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                       ELIMINAR SOCIO                         ")
		print("______________________________________________________________")
		print("                                                              ")
		codigo = input("Ingrese el Codigo del Socio que Desea Buscar: ")

		if self.videoclub.eliminar_socio(codigo):
			print("______________________________________________________________")
			print("                                                              ")
			print("             INFO -LOS DATOS FUERON ELIMINADOS.               ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("           ERROR - LOS DATOS NO SE PUEDEN ELIMINAR.           ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")	

	def adicionar_pelicula(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                      ADICIONAR PELICULA                      ")
		print("______________________________________________________________")
		print("                                                              ")		
		codigo = input("Ingrese el Codigo de la Pelicula: ")
		titulo = input("Ingrese el Titulo de la Pelicula: ")
		genero = input("Ingrese el Genero de la Pelicula: ")
		nombre_socio = ("No Asignado o ya se Encuentra Disponible.")
		pelicula = Pelicula(codigo, titulo, genero, nombre_socio)

		if self.videoclub.adicionar_pelicula(pelicula):
			print("______________________________________________________________")
			print("                                                              ")
			print("      INFO - LA PELICULA FUE ADICIONADA CORRECTAMENTE.        ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("          INFO - LA PELICULA NO SE PUDO ADICIONAR.            ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")	

	def listar_peliculas(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                       LISTAR PELICULAS                       ")
		print("______________________________________________________________")
		print("                                                              ")
		self.videoclub.listar_pelicula()
		input("ENTER")

	def modificar_peliculas(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                    MODIFICAR PELICULAS                       ")
		print("______________________________________________________________")
		print("                                                              ")
		codigo = input("Ingrese el Codigo de la Pelicula que Desea Buscar: ")

		if self.videoclub.modificar_peliculas(codigo):
			print("______________________________________________________________")
			print("                                                              ")
			print("     INFO - LOS DATOS DE LA PELICULA FUERON MODIFICADOS.      ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("    ERROR - LOS DATOS DE LA PELICULA NO PUEDEN MODIFICAR.     ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")	

	def eliminar_peliculas(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                        ELIMINAR PELICULAS                    ")
		print("______________________________________________________________")
		print("                                                              ")
		codigo = input("Ingrese el Codigo de la Pelicula que Desea Buscar: ")

		if self.videoclub.eliminar_peliculas(codigo):
			print("______________________________________________________________")
			print("                                                              ")
			print("      INFO - LOS DATOS DE LA PELICULA FUERON ELIMINADOS.      ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("     ERROR - LOS DATOS DE LA PELICULA NO PUEDEN ELIMINAR.     ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")	

	def alquilar_pelicula(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                      ALQUILAR PELICULA                       ")
		print("______________________________________________________________")
		print("                                                              ")
		codigo_pelicula = input("Ingrese el Codigo de la Pelicula:")
		codigo_socio = input("Ingrese el Codigo del Socio:")

		if self.videoclub.alquilar_pelicula(codigo_pelicula, codigo_socio):
			print("______________________________________________________________")
			print("                                                              ")
			print("              INFO - LA PELICULA ESTA ALQUILADA.              ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("              INFO - LA PELICULA NO ESTA ALQUILADA.           ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

	def devolver_pelicula(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                      DEVOLVER PELICULA                       ")
		print("______________________________________________________________")
		print("                                                              ")
		codigo_pelicula = input("Ingrese el Codigo de la Pelicula:")
		codigo_socio = input("Ingrese el Codigo del Socio:")

		if self.videoclub.devolver_pelicula(codigo_pelicula, codigo_socio):
			print("______________________________________________________________")
			print("                                                              ")
			print("              INFO - LA PELICULA ESTA DISPONIBLE.             ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("              INFO - LA PELICULA NO ESTA DISPONIBLE.          ")
			print("______________________________________________________________")
			print("                                                              ")
			input()

	def listar_peliculas_alquiladas(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                LISTAR PELICULAS ALQUILADAS                   ")
		print("______________________________________________________________")
		print("                                                              ") 
		self.videoclub.listar_peliculas_alquiladas()
		input("ENTER")

	def listar_peliculas_disponibles(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                 LISTAR PELICULAS DISPONIBLES                 ")
		print("______________________________________________________________")
		print("                                                              ")
		self.videoclub.listar_peliculas_disponibles()
		input("ENTER")

	def realizar_pedido(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                      REALIZAR PEDIDO                         ")
		print("______________________________________________________________")
		print("                                                              ")
		codigo = input("Ingrese el Codigo del Pedido: ")
		nombre_socio = ("......")
		direccion = input("Ingrese su Direccion de Residencia: ") 
		forma_de_pago = input("Ingrese la Forma de Pago: ")
		descripcion = input("Ingrese el Pedido que Solicita: ")
		pelicula = (".......")
		valor = input("Valor del Pedido: ")
		pedido = Pedido(codigo, nombre_socio, direccion, forma_de_pago, descripcion, pelicula, valor)

		if self.videoclub.realizar_pedido(pedido):
			print("______________________________________________________________")
			print("                                                              ")
			print("          INFO - EL PEDIDO FUE REALIZADO CORRECTAMENTE.       ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("                ERROR - PEDIDO NO REALIZADO.                  ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

	def listar_pedidos(self): 
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                  LISTAR PEDIDOS REALIZADOS                   ")
		print("______________________________________________________________")
		print("                                                              ")
		self.videoclub.listar_pedidos()
		input("ENTER")

	def confirmar_pedido(self): 
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                      CONFIRMAR PEDIDO                        ")
		print("______________________________________________________________")
		print("                                                              ")
		codigo_pedido = input("Ingrese el Codigo del Pedido: ") 
		codigo_socio = input("Ingrese el Codigo del Socio: ")
		codigo_pelicula = input("Ingrese el Codigo de la Pelicula: ")



		if self.videoclub.confirmar_pedido(codigo_pedido, codigo_socio, codigo_pelicula):
			print("______________________________________________________________")
			print("                                                              ")
			print("                INFO - CONFIRMADA LA COMPRA.                  ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("                 ERROR - COMPRA NO CONFIRMADA.                ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")



	def mostrar_menu_principal(self):
		while True:
			system("cls")
			print("______________________________________________________________")
			print("                                                              ")
			print("                           VIDEOCLUB                          ")
			print("______________________________________________________________")
			print("                                                              ")
			print("                         Menu Principal                       ")
			print("______________________________________________________________")
			print("                                                              ")
			print("          1: Crear Socio                                      ")
			print("          2: Listar Socios                                    ")
			print("          3: Modificar Socio                                  ")
			print("          4: Eliminar Socio                                   ")
			print("          5: Crear Pelicula                                   ")
			print("          6: Listar Peliculas                                 ")
			print("          7: Modificar Peliculas                              ")
			print("          8: Eliminar Peliculas                               ")
			print("          9: Alquilar Pelicula                                ")
			print("          10: Devolver Pelicula                               ")
			print("          11: Listar Peliculas Alquiladas                     ")
			print("          12: Listar Peliculas Disponibles                    ")
			print("          13: Realizar Pedidos                                ")
			print("          14: Listar Pedidos                                  ")
			print("          15: Confirmar Pedido                                ")
			print("          16: Salir                                           ")
			print("______________________________________________________________")
			print("                                                              ")
			

			try:
				op = int(input("Ingrese la Opcion:"))

				if op == 1:
					#Se invoca el metodo. 
					self.adicionar_socio()

				elif op == 2:
					self.listar_socios()

				elif op == 3:
					self.modificar_socio()

				elif op == 4:
					self.eliminar_socio()	

				elif op == 5:
					self.adicionar_pelicula()

				elif op == 6:
					self.listar_peliculas()	

				elif op == 7:
					self.modificar_peliculas()	

				elif op == 8:
					self.eliminar_peliculas()

				elif op == 9:
					self.alquilar_pelicula()

				elif op == 10:
					self.devolver_pelicula()

				elif op == 11:
					self.listar_peliculas_alquiladas()

				elif op == 12:
					self.listar_peliculas_disponibles()	

				elif op == 13:
					self.realizar_pedido()

				elif op == 14:
					self.listar_pedidos()

				elif op == 15:
					self.confirmar_pedido()

				elif op == 16:
					break

				else:
					print("______________________________________________________________")
					print("                                                              ")
					print("                  ERROR - OPCION NO VALIDA.                   ")
					print("______________________________________________________________")
					print("                                                              ")
					input("ENTER")

			except ValueError:
				print("______________________________________________________________")
				print("                                                              ")
				print("            ERROR - EL DATO INGRESADO NO ES ENTERO.           ")
				print("______________________________________________________________")
				print("                                                              ")		
				input("ENTER") 	

if __name__ == '__main__':
	#instancia de clase Menu. 
	menu = Menu()
	menu.mostrar_menu_principal()	# Todo lo que tenga un punto es un archivo adicional.
