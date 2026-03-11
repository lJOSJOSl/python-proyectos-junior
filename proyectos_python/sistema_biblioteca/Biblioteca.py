libros = []
usuarios = []

def agregar_libro(): #funcion para agregar un nuevo libro

    nombre = input("Nombre del libro: ")
    autor = input("Nombre del autor: ")

    libro = {
    "nombre" : nombre,
    "autor" : autor,
    "disponible" : True,
    "prestado_a": None
    }

    if any(l["nombre"] == nombre for l in libros):
        print("El libro ya existe")
        return

    libros.append(libro)
    print("Libro agregado")

def mostrar_libros(): #funcion
    print("\nBiblioteca:")

    if not libros:
        print("No hay libros registrados")
        return

    for libro in libros:
        estado = "Disponible" if libro ["disponible"] else f'Prestado a {libro["prestado_a"]}'
        print(f'{libro["nombre"]} - {libro["autor"]} - {estado}')

def agregar_usuario():

    print("\nValidar informacion con una identificacion oficial")
    nombre_u = input("Nombre de la persona: ")
    if any(u["nombre_u"] == nombre_u for u in usuarios):
        print("El usuario ya existe")
    else:
        while True:
            try:
                edad = int(input("Ingresa la edad de la persona: "))
                if edad <= 0:
                    print("La edad debe ser mayor a 0")
                else:
                    break
            except ValueError:
                print("Ingresa un numero valido")

        direccion = input("Ingresa el domicilio de la persona: ")

        usuario = {
        "nombre_u": nombre_u,
        "edad": edad,
        "direccion": direccion
        }

        usuarios.append(usuario)
        print("Usuario agregado")

def prestar_libro():
    nombre_libro = input("Nombre del libro a prestar: ")
    nombre_usuario = input("Nombre del usuario: ")
    libro = next((l for l in libros if l["nombre"] == nombre_libro and l["disponible"]), None)
    usuario = next((u for u in usuarios if u["nombre_u"] == nombre_usuario), None)
    if libro and usuario:
        libro["disponible"] = False
        libro["prestado_a"] = nombre_usuario
        print(f'El libro {libro["nombre"]} se presto a {usuario["nombre_u"]}')
    else:
        print("Libro no disponible o usuario no encontrado")

def devolver_libro():
    nombre_libro = input("Nommbre del libro a devolver: ")
    libro = next((l for l in libros if l["nombre"] == nombre_libro and not l["disponible"]), None)
    if libro:
        libro["disponible"] = True
        libro["prestado_a" = None
        print(f'El libro "{libro["nombre"]}" se devolvio')
    else:
        print("Libro no encontrado o ya disponible")

def eliminar_libro():

    nombre = input("libro a eliminar: ")

    for libro in libros:
        if libro["nombre"] == nombre:
            libros.remove(libro)
            print("Libro eliminado")
            return

    print("Libro no encontrado")

def salir():
    print("Cerrando programa")
    exit()

def main(): #crea el menu y ejecuta el programa principal
    opciones = {
        "1" : agregar_libro,
        "2" : mostrar_libros,
        "3" : agregar_usuario,
        "4" : prestar_libro,
        "5" : devolver_libro,
        "6" : eliminar_libro,
        "7" : salir
    }
    while True:
        print("\n--- Biblioteca ---")
        print("1. agregar libro")
        print("2. mostrar libros")
        print("3. agregar ususario")
        print("4. prestar libro")
        print("5. devolver libro")
        print("6. eliminar_libro")
        print("7. salir")
        opcion = input("Elige una opcion: ")
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("opcion invalida")

if __name__ == "__main__":
    main()