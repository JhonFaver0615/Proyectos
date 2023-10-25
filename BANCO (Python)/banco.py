import random
from cuenta import Cuenta

class Banco:

	def __init__(self):  
		self.__cuentas = []
		self.__numeros_cuentas = []

	def generar_numeros_cuentas(self):
		while True:
			numero = random.randint(1, 9)
			if numero not in self.__numeros_cuentas:
				self.__numeros_cuentas.append(numero)
				break
		return numero
	
	def buscar_cuenta(self, num_cuenta):
		for i in range(len(self.__cuentas)):
			if self.__cuentas[i].get_num_cuenta() == num_cuenta:
				return i
		return -1

	def buscar_id_titular(self, id_titular):
		for i in range(len(self.__cuentas)):
			if self.__cuentas[i].get_id_titular() == id_titular:
				return i 
		return -1 




	def adicionar_cuenta(self, cuenta):
		pos = self.buscar_cuenta(cuenta.get_num_cuenta())
		pos_1 = self.buscar_id_titular(cuenta.get_id_titular())
		if pos == -1 and pos_1 == -1:
			self.__cuentas.append(cuenta)
			return True
		return False

	def visualizar_cuenta(self, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			if self.__cuentas[pos].visualizar():
				return True
		return False

	def visualizar_cuenta_corriente(self, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1: 
			if self.__cuentas[pos].visualizar_cuenta_corriente():
				return True
		return False 

	def retirar_monto_cuenta(self, num_cuenta, monto):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			if self.__cuentas[pos].retirar(monto):
				return True
		return False

	def retirar_monto_corriente(self, num_cuenta, monto):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			if self.__cuentas[pos].retirar_cuenta_corriente(monto):
				return True
		return False

	def depositar_monto_cuenta(self, monto, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			self.__cuentas[pos].depositar(monto)
			return True
		return False

	def depositar_monto_corriente(self, num_cuenta, monto):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1: 
			self.__cuentas[pos].depositar_cuenta_corriente(monto)
			return True
		return False


	def consultar_saldo_cuenta(self, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			valor = self.__cuentas[pos].get_saldo()
			return valor

	def consultar_total_disponible(self, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			saldo_disponible = self.__cuentas[pos].get_saldo()
			cupo_disponible = self.__cuentas[pos].get_cupo_disponible()
			if cupo_disponible >= 0 and saldo_disponible < 0:
				total_disponible = cupo_disponible
				return total_disponible

			else:
				total_disponible = saldo_disponible + cupo_disponible
				return total_disponible
	

	def consultar_cupo_disponible(self, num_cuenta): 
		pos = self.buscar_cuenta(num_cuenta)

		if pos != -1: 
			cupo_disponible = self.__cuentas[pos].get_cupo_disponible()
			if cupo_disponible != -1:
				return cupo_disponible 
			else:
				return -1

	def visualizar_cliente(self, num_cuenta): 
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1: 
			titular = self.__cuentas[pos].get_nombre_titular()
			return titular 



	def tipo_cuenta(self, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			tipo_cuenta = self.__cuentas[pos].get_tipo_cuenta()
			return tipo_cuenta



	
			











