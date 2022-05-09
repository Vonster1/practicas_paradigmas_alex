from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#=============================
# Clase storemanager
# NO TIENE VARIABLES
#=============================
class ManejoDeIscripciones
#=============================================================
# Decorador staticmethod
# El objeto solo tiene la funcion inscribirUsiario
# ENVULVE LA FUNCION SIN LLAMAR VARIABLES LOCALES
# el objeto ManejoDeIsacripciones es la interface intercambiable
#=============================================================
	@staticmethod
	def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
	print("----> Guardando usuario...\n")
	repositorioDeUsuarios.abrir()
	repositorioDeUsuarios.guardar(usuario)
	repositorioDeUsuarios.cerrar()
	
