#=============================================================
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo basededatos.py : trae el objeto Basededatos
#=============================================================
from aplicacion.repositorio.basededatos import BaseDeDatos

#============================================================
# Del diretorio aplicacion, el sudirectorio repositorio,
# el archivo s3.py : trae el objeto S3
#============================================================
from aplicacion.repositorio.s3 import S3

#============================================================
# Del diretorio aplicacion, el subdirectorio repositorio,
# el archivo sistemadearchivo.py : trae el archivo SistemaDeArchivos
#============================================================
from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos

#============================================================
# Del directorio de aplicacion, el subdirectorio negocios, 
# el archivo manejodeinscripciones.py : trae el objeto ManejoDeInscrinciones
#============================================================
from aplicacione.negocios,manejodeinscripciones import ManejoDeInscripciones

#==========================
# crear el objeto Usuario
#==========================
usuario = Usuario("Roberto","Jimenez",18)

#==========================
# crear el objeto s3
#==========================
repositorioS3 = S3("321321321","sdf324223","MiCubeta")

#=============================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#=============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

#===================================
# crear el objeto sistemadearchivos
#===================================
repositorioSistemaDeArchivos = SistemaDeArchivos("\home\users")

#=============================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#=============================================================
ManejoDeInscripciones.iscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n") 

#======================================
# crear el objeto basededatos 
#======================================
repositorioBaseDeDatos = BaseDeDatos ("localhost","admin","admin123")

#===============================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#===============================================================
ManejoDeInscripciones.incribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")


