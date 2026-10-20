def buscar_palabra():
    """Opción 3: Busca comentarios que contengan una palabra indicada."""
    if len(comentarios) == 0:
        print("No hay comentarios registrados para buscar.")
        return

    palabra = input("Ingrese la palabra que desea buscar: ").strip().lower()
    encontrados = False

    print(f'Resultados de búsqueda para: "{palabra}"-')
    for i in range(len(comentarios)):
        if palabra in comentarios[i].lower():
            print(f"Comentario [{i + 1}]: {comentarios[i]}")
            encontrados = True

    if not encontrados:
        print("No se encontraron comentarios que contengan esa palabra.")

def mostrar_cantidad_palabras():
    """Opción 4: Muestra la cantidad de palabras de cada comentario."""
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
    else:
        print("Cantidad de palabras por comentario")
        for i in range(len(comentarios)):
            palabras = comentarios[i].split()
            print(f"Comentario {i + 1}: {len(palabras)} palabras")

def contar_palabra_en_comentario():
    """Opción 5: Cuenta cuántas veces aparece una palabra en un comentario seleccionado."""
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
        return

    mostrar_comentarios()
    try:
        seleccion = int(input("Seleccione el número del comentario a analizar: "))
        if seleccion < 1 or seleccion > len(comentarios):
            print("Número de comentario inválido.")
            return
        
        comentario_elegido = comentarios[seleccion - 1]
        palabra = input("¿Qué palabra desea contar en este comentario? ").strip().lower()
        
        palabras_lista = comentario_elegido.lower().split()
        conteo = palabras_lista.count(palabra)
        
        print(f"La palabra '{palabra}' aparece {conteo} vez/veces en el comentario seleccionado.")
    except ValueError:
        print("Por favor, ingrese un número válido.")


def generar_resumen():
    """Opción 6: Genera un resumen almacenado en una tupla (caracteres, palabras, apariciones)."""
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
        return

    mostrar_comentarios()
    try:
        seleccion = int(input("Seleccione el número del comentario para el resumen: "))
        if seleccion < 1 or seleccion > len(comentarios):
            print("Número de comentario inválido.")
            return

        comentario_elegido = comentarios[seleccion - 1]
        palabra_buscada = input("Ingrese la palabra clave para contar sus apariciones en el resumen: ").strip().lower()

        num_caracteres = len(comentario_elegido)
        palabras_lista = comentario_elegido.split()
        num_palabras = len(palabras_lista)
        
        num_apariciones = comentario_elegido.lower().split().count(palabra_buscada)

        resumen = (num_caracteres, num_palabras, num_apariciones)

        print("Resumen del comentario")
        print(f"Tupla generada: {resumen}")
        print(f"Número de caracteres: {resumen[0]}")
        print(f"Número de palabras: {resumen[1]}")
        print(f"Apariciones de la palabra '{palabra_buscada}': {resumen[2]}")

    except ValueError:
        print("Por favor, ingrese un número válido.")

def menu_principal():
    """Función principal que despliega el menú de consola."""
    while True:
        print("Analizador de comentarios.")
        print("1. Registrar un comentario")
        print("2. Mostrar todos los comentarios")
        print("3. Buscar comentarios que contengan una palabra")
        print("4. Mostrar la cantidad de palabras de cada comentario")
        print("5. Contar cuántas veces aparece una palabra en un comentario")
        print("6. Mostrar resumen de un comentario (Tupla)")
        print("7. Salir")
        
        opcion = input("Elija una opción (1-7): ").strip()
        
        if opcion == "1":
            registrar_comentario()
        elif opcion == "2":
            mostrar_comentarios()
        elif opcion == "3":
            buscar_palabra()
        elif opcion == "4":
            mostrar_cantidad_palabras()
        elif opcion == "5":
            contar_palabra_en_comentario()
        elif opcion == "6":
            generar_resumen()
        elif opcion == "7":
            print("¡Saliendo del programa! ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija un número entre 1 y 7.")

menu_principal()
