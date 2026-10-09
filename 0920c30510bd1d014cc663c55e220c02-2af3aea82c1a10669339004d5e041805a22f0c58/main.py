carreras: tuple[str,...] = (
    "Ingenieria de software",
    "Ciberseguridad", 
    "Ingenieria en Ciencias de Datos",
)
personas: list[tuple[str, str, int, int]] = [
  #nombre, apellido, edad, carrera
]

estudiantes: list[dict[str, str | int ]] = [
    # Lista de diccionario con nombre, apellido, edad carrera
]
for _ in range(1):
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))
    carrera = int(
        input("Ingrese la carrera (0=Ingenieria de Software, 1=Ciencia de Datos, 2=Ciberseguridad):")
        )

    persona = (nombre, apellido, edad, carrera)
    personas.append(persona) 

    print("\n----- Lista de estudiantes -----\n")

for persona in personas:
    
    nombre_carrera = carreras[persona[3]]
    

    estudiante = {
        "nombre": persona[0],
        "apellido": persona [1],
        "edad": persona[2],
        "carrera": nombre_carrera
    }
    estudiantes.append(estudiante)

for estudiante in estudiantes:
    print(
        estudiante["nombre"],
        estudiante["apellido"],
        "tiene",
        estudiante["edad"],
        "años y estudia",
        estudiante["carrera"]
    )