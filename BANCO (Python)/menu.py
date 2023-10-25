from os import system
from datetime import datetime
from cuenta import Cuenta
from banco import Banco 



class Menu:

	# Se realiza el constructor. Inicializa los objetos de la clase.
	def __init__(self):  
		self.banco = Banco() 



	def pedir_datos_cuenta(self):

		try:
			system("cls")
			print("______________________________________________________________")
			print("                                                              ")
			print("                        CREAR CUENTA                          ")
			print("______________________________________________________________")
			print("                                                              ")

			id_titular = input("Ingrese el Numero de Documento: ")
			nombre_titular = input("Ingrese el Nombre del Titular: ")
			num_cuenta = self.banco.generar_numeros_cuentas()
			saldo = int(input("Ingrese el Saldo Inicial de la Cuenta: "))
			fecha = datetime.now()

			while True:

				print("______________________________________________________________")
				print("                                                              ")
				print("                        TIPO DE CUENTA                        ")
				print("______________________________________________________________")
				print("                                                              ")
				print("      1: Ahorro                                               ")
				print("      2: Corriente                                            ")
				print("______________________________________________________________")
				print("                                                              ")

				try:
					op_tipo_cuenta = int(input("Seleccione el Tipo de Cuenta: "))
					print("______________________________________________________________")
					print("                                                              ")

					if op_tipo_cuenta == 1:
						tipo_cuenta = "Ahorro"
						cupo = 0 
						break

					elif op_tipo_cuenta == 2:
						tipo_cuenta = "Corriente"

						try:
							cupo = float(input("Ingrese el Cupo Asignado a la Cuenta: "))
							break

						except ValueError:
							print("______________________________________________________________")
							print("                                                              ")
							print("           ERROR - EL CUPO DEBE SER NUMERICO.                 ")
							print("______________________________________________________________")
							print("                                                              ")
							input("ENTER")

					else:
						print("______________________________________________________________")
						print("                                                              ")
						print("               ERROR - OPCION NO VALIDA                       ")
						print("______________________________________________________________")
						print("                                                              ")
						input("ENTER")

				except ValueError:
					print("______________________________________________________________")
					print("                                                              ")
					print("              ERROR - EL DATO DEBE SER ENTERO.                ")
					print("______________________________________________________________")
					print("                                                              ")
					input("ENTER")
			

			cuenta = Cuenta(id_titular, nombre_titular, num_cuenta, saldo, fecha, tipo_cuenta, cupo)

			
			if self.banco.adicionar_cuenta(cuenta):
				print("______________________________________________________________")
				print("                                                              ")
				print("            INFO - CUENTA CREADA CORRECTAMENTE.               ")
				print("______________________________________________________________")
				print("                                                              ")
				print("Numero de Cuenta Asignado: ", num_cuenta)
				print("______________________________________________________________")
				print("                                                              ")
				input("ENTER")

			else:
				print("______________________________________________________________")
				print("                                                              ")
				print("               ERROR - LA CUENTA YA EXISTE.                   ")
				print("______________________________________________________________")
				print("                                                              ")
				input("ENTER")



		except ValueError:
			print("______________________________________________________________")
			print("                                                              ")
			print("             ERROR - EL NUMERO NO ESTA DEFINIDO.              ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")


				

	def pedir_datos_visualizar_cuenta(self):

		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                       VISUALIZAR CUENTA                      ")
		print("______________________________________________________________")
		print("                                                              ")
		num_cuenta = int(input("Ingrese el Numero de Cuenta: "))
		pos = self.banco.buscar_cuenta(num_cuenta)

		if pos != -1 and self.banco.tipo_cuenta(num_cuenta) == 'Ahorro':
			self.banco.visualizar_cuenta(num_cuenta)
			input()

		elif pos != -1 and self.banco.tipo_cuenta(num_cuenta) == 'Corriente':
			self.banco.visualizar_cuenta_corriente(num_cuenta)
			input()

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("           ERROR - EL NUMERO DE CUENTA NO EXISTE.             ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

	def pedir_datos_retiro_cuenta(self):

		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                       RETIRAR SALDO                          ")
		print("______________________________________________________________")
		print("                                                              ")
		num_cuenta = int(input("Ingrese el Numero de la Cuenta: "))

		pos = self.banco.buscar_cuenta(num_cuenta)

		if pos != -1 and self.banco.tipo_cuenta(num_cuenta) == 'Ahorro':

			monto = float(input("Ingrese el Monto a Retirar: "))
			
			if self.banco.retirar_monto_cuenta(num_cuenta, monto):
				print("______________________________________________________________")
				print("                                                              ")
				print("            INFO - SALDO RETIRADO CORRECTAMENTE.              ")
				print("______________________________________________________________")
				print("                                                              ")
				input("ENTER")

			else:
				print("______________________________________________________________")
				print("                                                              ")
				print("             ERROR - EL SALDO NO SE PUDO RETIRAR.             ")
				print("______________________________________________________________")
				print("                                                              ")
				input("ENTER")

		elif pos != -1 and self.banco.tipo_cuenta(num_cuenta) == 'Corriente':
			monto = float(input("Ingrese el Monto a Retirar:"))

			if self.banco.retirar_monto_corriente(num_cuenta, monto):
				print("______________________________________________________________")
				print("                                                              ")
				print("            INFO - SALDO RETIRADO CORRECTAMENTE.              ")
				print("______________________________________________________________")
				print("                                                              ")
				input("ENTER")

			else:
				print("______________________________________________________________")
				print("                                                              ")
				print("             ERROR - EL SALDO NO SE PUDO RETIRAR.             ")
				print("______________________________________________________________")
				print("                                                              ")
				input("ENTER")


		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("                ERROR - LA CUENTA NO EXISTE.                  ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

	def pedir_datos_deposito_cuenta(self):

		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                         DEPOSITOS                            ")
		print("______________________________________________________________")
		print("                                                              ")
		print("                                                              ")
		num_cuenta = int(input("Ingrese el Numero de Cuenta: "))

		pos = self.banco.buscar_cuenta(num_cuenta)

		if pos != -1 and self.banco.tipo_cuenta(num_cuenta) == 'Ahorro':

			monto = float(input("Ingrese el Monto del Deposito:"))

			if self.banco.depositar_monto_cuenta(num_cuenta, monto):
				print("______________________________________________________________")
				print("                                                              ")
				print("         INFO - EL DEPOSITO SE REALIZO CORRECTAMENTE.         ")
				print("______________________________________________________________")
				print("                                                              ")
				input("ENTER")

			else:
				print("______________________________________________________________")
				print("                                                              ")
				print("          ERROR - EL DEPOSITO NO SE PUDO REALIZAR.            ")
				print("______________________________________________________________")
				print("                                                              ")
				input("ENTER")

		elif pos != -1 and self.banco.tipo_cuenta(num_cuenta) == 'Corriente':
			monto = float(input("Ingrese el Monto del Deposito: "))

			if self.banco.depositar_monto_corriente(num_cuenta, monto):
				print("______________________________________________________________")
				print("                                                              ")
				print("         INFO - EL DEPOSITO SE REALIZO CORRECTAMENTE.         ")
				print("______________________________________________________________")
				print("                                                              ")
				input("ENTER")

			else:
				print("______________________________________________________________")
				print("                                                              ")
				print("          ERROR - EL DEPOSITO NO SE PUDO REALIZAR.            ")
				print("______________________________________________________________")
				print("                                                              ")
				input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("                ERROR - LA CUENTA NO EXISTE.                  ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

	def mostrar_saldo_cuenta(self):
		
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                       MOSTRAR SALDO                          ")
		print("______________________________________________________________")
		print("                                                              ")
		num_cuenta = int(input("Ingrese el Numero de la Cuenta: "))

		pos = self.banco.buscar_cuenta(num_cuenta)
		
	

		if pos != -1 and self.banco.tipo_cuenta(num_cuenta) == 'Corriente':
			print("______________________________________________________________")
			print("                                                              ")
			print("Saldo de la Cuenta: ", (self.banco.consultar_saldo_cuenta(num_cuenta)))
			print("Cupo Disponible: ",(self.banco.consultar_cupo_disponible(num_cuenta)))
			print("Total Disponible: ", (self.banco.consultar_total_disponible(num_cuenta)))
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

		elif pos != -1 and self.banco.tipo_cuenta(num_cuenta) == 'Ahorro':
			print("______________________________________________________________")
			print("                                                              ")
			print("Saldo de la Cuenta: ", (self.banco.consultar_saldo_cuenta(num_cuenta)))
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("            ERROR - EL NUMERO DE CUENTA NO EXISTE.            ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

	def pedir_datos_visualizar_cliente(self):

		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                       CONSULTAR CLIENTE                      ")
		print("______________________________________________________________")
		print("                                                              ")
		num_cuenta = int(input("Ingrese el Numero de la Cuenta: "))

		pos = self.banco.buscar_cuenta(num_cuenta)

		if pos != -1:
			print("______________________________________________________________")
			print("                                                              ")
			print("Titular de la Cuenta: ",(self.banco.visualizar_cliente(num_cuenta)))
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("              ERROR - LA CUENTA NO EXISTE.                    ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")




	def mostrar_menu_principal(self):

		while True:
			system("cls")
			print("______________________________________________________________")
			print("                                                              ")
			print("                            BANCO                             ")
			print("______________________________________________________________")
			print("                                                              ")
			print("        1: Crear Cuenta                                       ")
			print("        2: Visualizar Cuenta                                  ")
			print("        3: Retiro                                             ")
			print("        4: Deposito                                           ")
			print("        5: Consultar Saldo                                    ")
			print("        6: Consultar Cliente                                  ")
			print("        0: Salir                                              ")
			print("______________________________________________________________")
			print("                                                              ")

			try:
				opcion = int(input("Ingrese la Opcion: "))
				print("______________________________________________________________")
				print("                                                              ")

				if opcion == 1:
					self.pedir_datos_cuenta()

				elif opcion == 2:
					self.pedir_datos_visualizar_cuenta()

				elif opcion == 3:
					self.pedir_datos_retiro_cuenta()

				elif opcion == 4:
					self.pedir_datos_deposito_cuenta()

				elif opcion == 5:
					self.mostrar_saldo_cuenta()

				elif opcion == 6:
					self.pedir_datos_visualizar_cliente()

				elif opcion == 0:
					break

				else:
					print("______________________________________________________________")
					print("                                                              ")
					print("                 ERROR - OPCION NO VALIDA.                    ")
					print("______________________________________________________________")
					print("                                                              ")
					input("ENTER")

			except ValueError:
				print("______________________________________________________________")
				print("                                                              ")
				print("               ERROR- EL DATO DEBE SER ENTERO.                ")
				print("______________________________________________________________")
				print("                                                              ")
				input("ENTER")



if __name__ == '__main__':
	menu = Menu()
	menu.mostrar_menu_principal()

