class Pedido:
	def __init__(self, codigo, nombre_socio, direccion, forma_de_pago, descripcion, titulo, valor):

		self.codigo = codigo
		self.nombre_socio = nombre_socio
		self.direccion = direccion 
		self.forma_de_pago = forma_de_pago
		self.descripcion = descripcion 
		self.titulo = titulo 
		self.valor = valor
		self.compra = False

	def mostrar_pedido(self):
		print("Codigo: ",self.codigo)
		print("Nombre_socio: ",self.nombre_socio)
		print("Direccion: ",self.direccion)
		print("Forma_de_pago: ",self.forma_de_pago)
		print("Pedido: ",self.descripcion)
		print("Pelicula: ",self.titulo)
		print("Valor: ",self.valor)
		print("Compra: ",self.compra)


	
	#def mostrar_pedidos(self):


