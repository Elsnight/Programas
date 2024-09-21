lista_compras = []
valor_descuento = 10

def crear_lista_compras():
    
    while True:
        nombre = input("Ingresa el nombre del producto (solo letras): ")
        if nombre.isalpha():
            precio = float(input(f"Ingresa el precio de {nombre}: "))
            lista_compras.append([nombre, precio])
        else:
            print("Error: El nombre del producto debe contener solo letras. Inténtalo nuevamente.")
        continuar = input("¿Deseas agregar otro producto a la lista de compras? (s/n): ")
        if continuar.lower() != "s":
            break
    return lista_compras

def mostrar_lista_compras(lista_compras):
    print("Lista de compras:")
    for i, (producto, precio) in enumerate(lista_compras, 1):
        print(f"{i}. {producto}: {precio}")

def calcular_descuento(total,valor_descuento):
    descuento = (total * valor_descuento)/100
    return descuento

def generar_factura(lista_compras):
    total = sum(precio for producto, precio in lista_compras)
    descuento = calcular_descuento(total,valor_descuento)
    total_final = total - descuento
    print("\n========== FACTURA ==========")
    print("==============================")
    mostrar_lista_compras(lista_compras)
    print(f"Total: {total:.2f}")
    print(f"Descuento: {descuento:.2f}")
    print(f"Total a pagar: $ {total_final:.2f}")

generar_factura(crear_lista_compras())
