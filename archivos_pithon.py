# Crear y abrir el archivo en modo de escritura
with open("my_notes.txt", "w") as file:
    # Escribir tres líneas de notas personales
    file.write("Primera nota: Aprender Python es divertido eduardo.\n")
    file.write("Segunda nota: Me encanta automatizar tareas.\n")
    file.write("Tercera nota: ¡Los archivos de texto son útiles!\n")

# Abrir el archivo en modo de lectura
with open("my_notes.txt", "r") as file:
    # Leer el archivo línea por línea
    for linea in file:
        # Mostrar cada línea en la consola
        print(linea.strip())  # .strip() elimina los saltos de línea adicionales
