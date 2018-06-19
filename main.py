from Usuarios import *

listaUsuarios = []

def datosUsuarios():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    correo = input("Ingrese su correo electrónico: ")
    id = input("Ingrese su cédula: ")
    contrasena = input("Ingrese una contraseña: ")
    tipoUsuario = tipoUsuarioUI()

    agregarUsuarios(nombre,edad,correo,id,contrasena,tipoUsuario)


def tipoUsuarioUI():
    






def agregarUsuarios(nombre,edad,correo,id,contrasena,tipoUsuario):
    nuevoUsuario = Usuarios(nombre,edad,correo,id,contrasena,tipoUsuario)
    listaUsuarios.append(nuevoUsuario)
    main()

def datosUsuariosRegistrados():
    id = input("Ingrese su cédula: ")
    contrasena = input("Ingrese la contraseña: ")
    validarUsuarios(id,contrasena)

def validarUsuarios(id,contrasena):
    for i in listaUsuarios:
        if i [Usuarios.getId()] == id:
            if i [Usuarios.getContrasena()] == contrasena:



def main():
    print("\n**********************************************************************\n")
    print("***************Bienvenido al menú del sistema electoral***************")
    print("\n**********************************************************************\n")
    print("Escoja una opción:\n"
          "1) Registrarse\n"
          "2) Iniciar Seción\n"
          "3) Salir")
    opcion = input(str("¿Qué desea realizar? "))


    if opcion == "1":
        datosUsuarios()
    elif opcion == "2":
        pass
    elif opcion == "3":
        print("\n¡Gracias!")
    else:
        print("\nOpción inválida, intente de nuevo\n")
        main()



main()