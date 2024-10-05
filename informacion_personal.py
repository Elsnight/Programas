# Crear el diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Miguel CUenca",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder al valor asociado a la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor para la "profesion"
informacion_personal["profesion"] = "Desarrollador de software"

# Verificar si la clave "telefono" existe, y si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "983873954"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)

# Imprimir el diccionario resultante
print(informacion_personal)
