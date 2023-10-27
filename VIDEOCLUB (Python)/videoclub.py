from socio import Socio
from pelicula import Pelicula
from pedido import Pedido


#Definimos la clase
class VideoClub:

	#Consructor de clase.
	def __init__(self):
		#atributo tipo lista.
		self.socios = []
		self.peliculas = []
		self.pedidos = []

	def buscar_socio(self, codigo):
		for i in range(len(self.socios)):
			if self.socios[i].codigo == codigo: # Compara todos los codigos almacenados con el nuevo codigo ingresado.
				return i

		return -1 # Si la condicion anterior no se cumple retorna un menos uno.		

	def adicionar_socio(self, socio):
		if self.buscar_socio(socio.codigo) == -1:
			self.socios.append(socio)
			return True
		return False	

	def listar_socios(self): 
		for i in self.socios: 
			print("*******************")
			i.mostrar_socio()

	def modificar_socio(self, codigo): 
		pos_socio = self.buscar_socio(codigo)
		if pos_socio != -1:
			if self.socios[pos_socio].codigo == codigo:
				print("********************")
				print("  OPCIONES PARA MODIFICAR ")
				print("********************")

				try:
					print("************************")
					print("1 = Modificar nombre")
					print("2 = Modificar Telefono")
					print("3 = modificar direccion")
					print("*************************")

					op = int(input("Seleccione la opcion a modificar: "))

					if op == 1:
						nombre = input("Digite el nuevo nombre del socio: ")
						self.socios[pos_socio].nombre = nombre
						return True 

					elif op == 2:
						telefono = input("Digite el nuevo telefono del socio: ")
						self.socios[pos_socio].telefono = telefono
						return True 

					elif op == 3:
						direccion = input("Digite la nueva direccion del socio: ")
						self.socios[pos_socio].direccion = direccion
						return True 

					else: 
						return False 



				except ValueError:
					print("*****************")
					print("Error - el dato debe de ser entero.")
					print("*****************")
					input()			

			else:
				return False

		else:
			return False			


	def eliminar_socio(self, codigo): 
		pos_socio = self.buscar_socio(codigo)
		if pos_socio != -1:
			del(self.socios[pos_socio])
			return True
		return False	
		
	def adicionar_pelicula(self, pelicula):
		if self.buscar_pelicula(pelicula.codigo) == -1:
			self.peliculas.append(pelicula)
			return True
		return False 
		
	def buscar_pelicula(self, codigo):
		for i in range (len(self.peliculas)):
			if self.peliculas[i].codigo == codigo:
				return i
		return -1 	

	def listar_pelicula(self):
		for pelicula in self.peliculas:
			print("********************")
			pelicula.mostrar_pelicula()	

	def modificar_peliculas(self, codigo):
		pos_pelicula = self.buscar_pelicula(codigo)
		if pos_pelicula != -1:
			if self.peliculas[pos_pelicula].codigo == codigo:
				print("**************************")
				print("   OPCIONES PARA MODIFICAR ")
				print("**************************")

				try:
					print("**************************")
					print("1 = Modificar titulo")
					print("2 = Modificar genero")
					print("**************************")

					op = int(input("Seleccione la opcion a modificar: "))

					if op == 1:
						titulo = input("Digite el nuevo titulo de la pelicula: ")
						self.peliculas[pos_pelicula].titulo = titulo
						return True

					elif op == 2:
						genero = input("Digite el nuevo genero de la pelicula: ")
						self.peliculas[pos_pelicula].genero = genero	
						return True

					else:
						return False


				except ValueError:
					print("*****************")
					print("Error - el dato debe de ser entero.")
					print("*****************")
					input()	
			else:
				return False

		else:
			return False

	def eliminar_peliculas(self, codigo):
		pos_pelicula = self.buscar_pelicula(codigo)
		if pos_pelicula != -1:
			del(self.peliculas[pos_pelicula])
			return True
		return False
		
	def alquilar_pelicula(self, codigo_pelicula, codigo_socio):
		pos_pelicula = self.buscar_pelicula(codigo_pelicula)
		pos_socio = self.buscar_socio(codigo_socio)
		if pos_pelicula != -1 and pos_socio != -1:
			if self.peliculas[pos_pelicula].codigo == codigo_pelicula:
				if self.socios[pos_socio].codigo == codigo_socio:
					self.peliculas[pos_pelicula].alquilada = True
					self.peliculas[pos_pelicula].nombre_socio = self.socios[pos_socio].nombre
					return True
				else:
					return False

			else:
				return False

		else:
			return False	


	def devolver_pelicula(self, codigo_pelicula, codigo_socio):
		pos_pelicula = self.buscar_pelicula(codigo_pelicula)
		pos_socio = self.buscar_socio(codigo_socio)
		if pos_pelicula != -1 and pos_socio != -1:
			if self.peliculas[pos_pelicula].codigo == codigo_pelicula:
				if self.socios[pos_socio].codigo == codigo_socio:
					self.peliculas[pos_pelicula].alquilada = False
					return True

				else:
					return False
			else:
				return False
		else:
			return False	



	def listar_peliculas_alquiladas(self):
		for pelicula in self.peliculas:
			print("********************")
			pelicula.mostrar_peliculas_alquiladas()

	def listar_peliculas_disponibles(self):
		for pelicula in self.peliculas:
			print("********************")
			pelicula.mostrar_peliculas_disponibles()

	def realizar_pedido(self, pedido):
		if self.buscar_pedido(pedido.codigo) == -1:
			self.pedidos.append(pedido)
			return True
		return False

	def buscar_pedido(self, codigo):
		for i in range(len(self.pedidos)):
			if self.pedidos[i].codigo == codigo: 
				return i 
		return -1

	def listar_pedidos(self):
		for pedido in self.pedidos:
			print("*************************")
			pedido.mostrar_pedido()

	def confirmar_pedido(self, codigo_pedido, codigo_socio, codigo_pelicula):
		pos_pedido = self.buscar_pedido(codigo_pedido)
		pos_socio = self.buscar_socio(codigo_socio)
		pos_pelicula = self.buscar_pelicula(codigo_pelicula)
		if pos_pedido != -1 and pos_socio != -1 and pos_pelicula != -1:
			if self.pedidos[pos_pedido].codigo == codigo_pedido:
				if self.socios[pos_socio].codigo == codigo_socio:
					if self.peliculas[pos_pelicula].codigo == codigo_pelicula:
						self.pedidos[pos_pedido].compra = True
						self.pedidos[pos_pedido].nombre_socio = self.socios[pos_socio].nombre
						self.pedidos[pos_pedido].titulo = self.peliculas[pos_pelicula].titulo
						return True
					else:
						return False

				else:
					return False

			else:
				return False	
		else:
			return False
