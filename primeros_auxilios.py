


# Pregunta al usuario si la persona responde a estímulos
respuesta_1 = input("¿La persona responde a estímulos? (si/no): ").lower()

# Si la respuesta es sí, se valora la necesidad de llevarlo al hospital más cercano
if respuesta_1 == "si":
    print("Valorar la necesidad de llevarlo al hospital más cercano.")
# Si la respuesta es no, se procede con las siguientes acciones
else:
    print("Abrir la vía aérea.")
    # Pregunta al usuario si la persona respira
    respuesta_2 = input("¿La persona respira? (si/no): ").lower()
    if respuesta_2 == "si":
        print("Permitirle posición de suficiente ventilación.")
        print("Fin")
    else:
        print("Administrar 5 ventilaciones y llamar a ambulancia.")
        print("Signos de vida")
        # Pregunta al usuario si hay signos de vida
        respuesta_3 = input("¿Hay signos de vida? (si/no): ").lower()
        if respuesta_3 == "no":
            print("Administrar compresiones torácicas hasta que llegue ambulancia.")
        else:
            print("Reevaluar a la espera de la ambulancia.")
    
    while True:
        respuesta_4 = input("¿Llegó la ambulancia? (si/no): ").lower()
        if respuesta_4 == "si":
            print("La ambulancia a llegado - Fin")
            break
        elif respuesta_4 == "no":
            print("Signos de vida")
            respuesta_5 = input("¿Hay signos de vida? (si/no): ").lower()
            if respuesta_5 == "si":
                print("Reevaluar a la espera de la ambulancia.")
                continue
            elif respuesta_5 == "no":
                print("Administrar compresiones torácicas hasta que llegue ambulancia.")
                continue
        else:
            print("Respuesta inválida. Por favor, responde 'si' o 'no'.")




"""
def respuesta_emergencia():
    responde_estimulos = input("¿Responde a estímulos? (Sí/No): ").lower()
    
    if responde_estimulos == "no":
        print("No llevarlo al hospital próximo")
        print("Abrir vía aérea")
    
    respira = input("¿Respira? (Sí/No): ").lower()
    
    if respira == "no":
        print("Administrar 5 ventilaciones")
        print("Llamar a ambulancia")
        
        signos_vida = input("¿Hay signos de vida? (Sí/No): ").lower()
        
        if signos_vida == "no":
            print("Administrar compresiones torácicas")
            print("Reevaluar a la espera de la ambulancia")

respuesta_emergencia()

"""