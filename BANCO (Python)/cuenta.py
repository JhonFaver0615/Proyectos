class Cuenta:
	def __init__(self, id_titular, nombre_titular, num_cuenta, saldo, fecha, tipo_cuenta, cupo):

		self.__id_titular = id_titular
		self.__nombre_titular = nombre_titular
		self.__numero_cuenta = num_cuenta
		self.__saldo = saldo                           
		self.__fecha = fecha
		self.__tipo_cuenta = tipo_cuenta
		self.__cupo = cupo
		self.__cupo_original = cupo
	

	def get_num_cuenta(self): 
		return self.__numero_cuenta

	def visualizar(self):

		print("ID del Titular: ",self.__id_titular)
		print("Nombre del Titular: ",self.__nombre_titular)
		print("Numero de Cuenta: ",self.__numero_cuenta)
		print("Fecha Actual: ",self.__fecha)
		print("Tipo de Cuenta: ",self.__tipo_cuenta)
		print("Saldo de la Cuenta: ",self.__saldo)
	


	def visualizar_cuenta_corriente(self):

		print("ID del Titular: ",self.__id_titular)
		print("Nombre del Titular: ",self.__nombre_titular)
		print("Numero Cuenta: ",self.__numero_cuenta)
		print("Fecha Actual: ",self.__fecha)
		print("Tipo de Cuenta: ",self.__tipo_cuenta)
		print("Saldo de la Cuenta: ",self.__saldo)
		print("Cupo Disponible: ",self.__cupo)

		if self.__cupo >= 0 and self.__saldo < 0:
			
			print("Total Disponible:", self.__cupo)

		else:
			print("Total Disponible: ", self.__saldo + self.__cupo)


	def retirar(self, monto):

		if self.__saldo - monto > 0:
			self.__saldo -= monto
			return True
		else:
			return False

	def retirar_cuenta_corriente(self, monto):

		if (self.__saldo + self.__cupo) - monto > 0:
			self.__saldo -= monto
			if self.__saldo < 0:
				self.__cupo += self.__saldo
				return True 
		return False 
				

	def depositar(self, monto):

		if monto > 0:
			self.__saldo += monto
			return True
		return False

	def depositar_cuenta_corriente(self, monto):
		
		if monto > 0:

			if self.__saldo >= 0:
				self.__saldo += monto
				return True 
			else:
				self.__saldo += monto
				if self.__cupo < self.__cupo_original:
					deuda = self.__cupo_original - self.__cupo

					if monto < deuda: 
						self.__cupo += monto
						return True

					else:
						self.__cupo = self.__cupo_original 
				return True 
				

		return False 

	def get_saldo(self):
		return self.__saldo 

	def get_cupo_disponible(self):
		return self.__cupo
		
		
	def get_tipo_cuenta(self):
		return self.__tipo_cuenta 

	def get_nombre_titular(self):
		return self.__nombre_titular

	def get_id_titular(self):
		return self.__id_titular
