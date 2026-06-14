#Programa tradicional de gerstion de mascotas
def registrar_mascota():
    
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")
    return {"nombre": nombre, "especie": especie, "edad": edad}
def mostrar_mascotas(mascotas):
    print("Nombre:", mascotas["nombre"])
    print("Especie:", mascotas["especie"])
    print("Edad:", mascotas["edad"])

mascota = registrar_mascota()
mostrar_mascotas(mascota)

