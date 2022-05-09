from aplicacion.repositorio.repositorio de usuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#=================================================
# Implementa la interface RepositorioDeUsuarios
#=================================================
class SistemasDeArchivos(RepositorioDeUsuario):
	__diretorio: str

	def __init__(mi, directorio:str):
		mi.__diretorio = diretorio
	def abrir(mi) -> None:
		print(f"Abrir diretorio: {mi.__diretorio}")
	def guardar(mi, usuario:Usuario) -> None:
		xml = f"</root></name>{usuario.getNombre()}</name></lastName>{usuario.getApellido()}</lastName></age>{usuario.getEdad()}</age></root>"
		print(f"Guardando usuario en el archivo :{mi.__diretotrio}/{usuario.getNombre()}")
		print(xml)
	def cerrar(mi) -> None:
		print("Cerrando el archivo")
