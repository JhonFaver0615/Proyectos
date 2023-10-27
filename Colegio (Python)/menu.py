from os import system
from estudiante import Estudiante
from colegio import Colegio
from aula import Aula
from fecha import Fecha
from asistencia import Asistencia

class Menu:

	def __init__(self):
		self.colegio = Colegio()

	def listar_estudiantes(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                     LISTAR ESTUDIANTE                        ")
		print("______________________________________________________________")
		print("                                                              ")
		for estudiante in self.colegio.get_estudiantes():
			print("______________________________________________________________")
			print("                                                              ")
			print("Codigo: %s" % (estudiante.get_codigo()))
			print("Nombre: %s" % (estudiante.get_nombre()))
			print("Apellido: %s" % (estudiante.get_apellido()))
			print("______________________________________________________________")
			print("                                                              ")
		input("ENTER")

	def listar_aulas(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                      LISTAR LAS AULAS                        ")
		print("______________________________________________________________")
		print("                                                              ")
		for aula in self.colegio.get_aulas():
			print("______________________________________________________________")
			print("                                                              ")
			print("Codigo: %s" % (aula.codigo_aula))
			print("Nombre: %s" % (aula.nombre_aula))
			print("Capacidad del aula: %s" % (aula.capacidad_aula))
			print("______________________________________________________________")
			print("                                                              ")
		input("ENTER")

	def listar_asistencias(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                      LISTAR ASISTENCIAS                      ")
		print("______________________________________________________________")
		print("                                                              ")
		for asistencia in self.colegio.get_asistencias():
			print("______________________________________________________________")
			print("                                                              ")
			asistencia.visualizar_asistencia()
			print("______________________________________________________________")
			print("                                                              ")
		input("ENTER")

	def listar_asistencia_aula(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                    LISTAR ASISTENCIA AULA                    ")
		print("______________________________________________________________")
		print("                                                              ")

		codigo_aula = input("Ingrese el Codigo del Aula: ")
		pos_aula = self.colegio.buscar_aula(codigo_aula)

		if pos_aula != -1:
			for asistencia in self.colegio.get_asistencia_aula(codigo_aula):
				print("______________________________________________________________")
				print("                                                              ")
				asistencia.visualizar_asistencia()
				print("______________________________________________________________")
				print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("                    EL AULA NO EXISTE.                        ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

	def listar_asistencia_aula_estudiante(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("           LISTAR ASISTENCIA AL AULA DEL ESTUDIANTE           ")
		print("______________________________________________________________")
		print("                                                              ")

		codigo_estudiante = input("Ingrese el Codigo del Estudiante: ")
		pos_estudiante = self.colegio.buscar_estudiante(codigo_estudiante)

		if pos_estudiante != -1:
			for asistencia in self.colegio.get_asistencia_estudiante(codigo_estudiante):
				print("______________________________________________________________")
				print("                                                              ")
				asistencia.visualizar_asistencia_estudiante()
				print("______________________________________________________________")
				print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("                  EL ESTUDIANTE NO EXISTE.                    ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")



	def pedir_datos_crear_estudiante(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                       CREAR ESTUDIANTE                       ")
		print("______________________________________________________________")
		print("                                                              ")
		nombre = input("Ingrese el Nombre: ")
		apellido = input("Ingrese el Apellido: ")
		codigo = input("Ingrese el Codigo: ")

		estudiante = Estudiante(nombre, apellido, codigo)

		if self.colegio.adicionar_estudiante(estudiante):
			print("______________________________________________________________")
			print("                                                              ")
			print("        INFO - EL ESTUDIANTE SE AGREGO CORRECTAMENTE.         ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("          ERROR - EL ESTUDIANTE NO SE PUDO ADICIONAR.         ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")


	def crear_aula(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                         CREAR AULA                           ")
		print("______________________________________________________________")
		print("                                                              ")
		nombre_aula = input("Ingrese el Nombre del Aula: ")
		codigo_aula = input("Ingrese el Codigo del Aula: ")
		capacidad_aula = input("Ingrese la Capacidad del Aula: ")

		aula = Aula(nombre_aula, codigo_aula, capacidad_aula)

		if self.colegio.adicionar_aula(aula):
			print("______________________________________________________________")
			print("                                                              ")
			print("          INFO - EL AULA SE ADICIONO CORRECTAMENTE.           ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("          ERROR - EL AULA NO SE PUDO ADICIONAR.               ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")


	def crear_asistencia_aula(self):
		system("cls")
		print("______________________________________________________________")
		print("                                                              ")
		print("                  CREAR ASISTENCIA AL AULA                    ")
		print("______________________________________________________________")
		print("                                                              ")
		codigo_aula = input("Ingrese el Codigo del Aula: ")
		pos_aula = self.colegio.buscar_aula(codigo_aula)

		if pos_aula != -1:
			dia = int(input("Ingrese el Dia: "))
			mes = int(input("Ingrese el Mes: "))
			anio = int(input("Ingrese el Año: "))
			fecha = Fecha(anio, mes, dia)

			codigo_asistencia = int(input("Ingrese el Codigo de la Asistencia: "))

			asistencia_aula = Asistencia(fecha, self.colegio.get_aula(pos_aula), codigo_asistencia)

			while True:
				print("______________________________________________________________")
				print("                                                              ")
				print("                   ASISTENCIA ESTUDIANTE                      ")
				print("______________________________________________________________")
				print("                                                              ")
				print("        1: Ingresar la Asistencia del Estudiante              ")
				print("        2: Salir                                              ")
				print("______________________________________________________________")
				print("                                                              ")
				op = int(input("Ingrese la Opcion: "))
				print("______________________________________________________________")
				print("                                                              ")

				if op == 1:
					codigo_estudiante = input("Ingrese el Codigo del Estudiante: ") 
					pos_estudiante = self.colegio.buscar_estudiante(codigo_estudiante)

					if pos_estudiante != -1:
						asistencia_aula.adicionar_estudiante(self.colegio.get_estudiante(pos_estudiante))

					else:
						print("______________________________________________________________")
						print("                                                              ")
						print("               ERROR - EL ESTUDIANTE NO EXISTE.               ")
						print("______________________________________________________________")
						print("                                                              ")
						input("ENTER") 

				elif op == 2:
					break

				else:
					print("______________________________________________________________")
					print("                                                              ")
					print("                   ERROR - OPCION NO VALIDA.                  ")
					print("______________________________________________________________")
					print("                                                              ")
					input("ENTER")

			self.colegio.adicionar_asistencia(asistencia_aula)

		else:
			print("______________________________________________________________")
			print("                                                              ")
			print("                 ERROR - OPCION NO VALIDA.                    ")
			print("______________________________________________________________")
			print("                                                              ")
			input("ENTER")


	def mostrar_menu_principal(self):
		while True:
			system("cls") 
			print("______________________________________________________________")
			print("                                                              ")
			print("                           COLEGIO                            ")
			print("______________________________________________________________")
			print("                                                              ")
			print("         1: Crear Estudiante                                  ")
			print("         2: crear Aula                                        ")
			print("         3: Crear Asistencia                                  ")
			print("         4: Listar Estudiantes                                ")
			print("         5: Listar Aulas                                      ")
			print("         6: Listar Asistencias                                ")
			print("         7: Listar Asistencia por Aula                        ")
			print("         8: Listar Asistencia al Aula del Estudiante          ")
			print("         0: Salir                                             ")
			print("______________________________________________________________")
			print("                                                              ")
			

			try:

				op = int(input("Ingrese la Opcion: "))
				
				if op == 1:
					self.pedir_datos_crear_estudiante()

				elif op == 2:
					self.crear_aula()

				elif op == 3:
					self.crear_asistencia_aula()

				elif op == 4:
					self.listar_estudiantes()

				elif op == 5:
					self.listar_aulas()

				elif op == 6:
					self.listar_asistencias()

				elif op == 7:
					self.listar_asistencia_aula()


				elif op == 8:
					self.listar_asistencia_aula_estudiante()

				elif op == 0:
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
				print("              ERROR - EL DATO DEBE DE SER ENTERO.             ")
				print("______________________________________________________________")
				print("                                                              ")
				input("ENTER")

if __name__ == '__main__':
	menu = Menu()
	menu.mostrar_menu_principal()