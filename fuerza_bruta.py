from string import ascii_lowercase  # Importamos el alfabeto en minúsculas
import msvcrt  # Importamos la biblioteca msvcrt para leer caracteres sin necesidad de presionar Enter

def getpass(prompt="Password: "):
    """Función para obtener una contraseña oculta desde la entrada estándar."""
    print(prompt, end='', flush=True)  # Mostramos el prompt para ingresar la contraseña
    password = ''  # Inicializamos una cadena vacía para almacenar la contraseña
    while True:
        char = msvcrt.getch().decode('utf-8')  # Leemos un caracter sin mostrarlo en pantalla
        if char == '\r':  # Si se presiona Enter ('\r'), finalizamos la entrada de la contraseña
            print('')  # Imprimimos una nueva línea para mantener el formato
            return password  # Devolvemos la contraseña ingresada
        elif char == '\b':  # Si se presiona Retroceso ('\b')
            if password:  # Verificamos que haya caracteres en la contraseña
                password = password[:-1]  # Eliminamos el último caracter de la contraseña
                print('\b \b', end='', flush=True)  # Borramos el último caracter mostrado en pantalla
        else:
            password += char  # Añadimos el caracter a la contraseña
            print('*', end='', flush=True)  # Mostramos un asterisco en lugar del caracter para ocultar la contraseña

def fuerza_bruta(contraseña):
    """Función para simular un ataque de fuerza bruta a una contraseña."""
    intentos = 0  # Inicializamos el contador de intentos
    for letra in contraseña:  # Iteramos sobre cada letra de la contraseña
        for letra_abecedario in ascii_lowercase:  # Iteramos sobre cada letra del alfabeto en minúsculas
            intentos += 1  # Incrementamos el contador de intentos
            if letra_abecedario == letra:  # Si la letra del alfabeto coincide con una letra de la contraseña
                break  # Salimos del bucle interno
    return intentos  # Devolvemos el total de intentos realizados para forzar la contraseña

if __name__ == "__main__":
    contraseña_oculta = getpass("Ingrese la contraseña oculta: ")  # Solicitamos al usuario ingresar una contraseña oculta
    print("La contraseña fue forzada en", fuerza_bruta(contraseña_oculta), "intentos")  # Imprimimos el resultado del ataque de fuerza bruta



"""
from string import ascii_lowercase  # Importamos el alfabeto en minúsculas
from getpass import getpass  # Importamos la función getpass para leer la contraseña sin mostrarla en pantalla

def fuerza_bruta(contraseña):
    # Función para simular un ataque de fuerza bruta a una contraseña.
    intentos = 0  # Inicializamos el contador de intentos
    for letra in contraseña:  # Iteramos sobre cada letra de la contraseña
        for letra_abecedario in ascii_lowercase:  # Iteramos sobre cada letra del alfabeto en minúsculas
            intentos += 1  # Incrementamos el contador de intentos
            if letra_abecedario == letra:  # Si la letra del alfabeto coincide con una letra de la contraseña
                break  # Salimos del bucle interno
    return intentos  # Devolvemos el total de intentos realizados para forzar la contraseña

if __name__ == "__main__":
    contraseña_oculta = getpass("Ingrese la contraseña oculta: ")  # Solicitamos al usuario ingresar una contraseña oculta
    print("La contraseña fue forzada en", fuerza_bruta(contraseña_oculta), "intentos")  # Imprimimos el resultado del ataque de fuerza bruta


"""