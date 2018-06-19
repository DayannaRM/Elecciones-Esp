class Usuarios:
    def __init__(self,nombreCompleto,edad,correo,iD,contrasena,tipoUsuario):
        self.__nombre = nombreCompleto
        self.__edad = edad
        self.__correo = correo
        self.__id = iD
        self.__contrasena = contrasena
        self.__tipoUsuario = tipoUsuario

    def getId(self):
        return self.__id
    def getContrasena(self):
        return self.__contrasena
    def getTipoUsuario(self):
        return self.__tipoUsuario