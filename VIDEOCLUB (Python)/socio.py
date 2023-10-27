# Se difine la clase.

class Socio:

	#Constructor de clase.
	def __init__(self, codigo, nombre, telefono, direccion):
		#Atributos de la clase
		#self.nombre_atributo = parametro.
		self.codigo = codigo
		self.nombre = nombre
		self.telefono = telefono
		self.direccion = direccion

	def mostrar_socio(self):
		print("Codigo: ",self.codigo)
		print("Nombre completo: ",self.nombre)
		print("Telefono: ",self.telefono)	
		print("Direccion: ",self.direccion)

		