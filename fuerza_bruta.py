from string import ascii_lowercase
import msvcrt 

def getpass(prompt="Password: "):
    print(prompt, end='', flush=True)
    password = ''
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r':
            print('')
            return password
        elif char == '\b':
            if password:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        else:
            password += char
            print('*', end='', flush=True)

def fuerza_bruta(contraseña):
    intentos = 0
    for letra in contraseña:
        for letra_abecedario in ascii_lowercase:
            intentos += 1
            if letra_abecedario == letra:
                break
    return intentos

if __name__ == "__main__":
    contraseña_oculta = getpass("Ingrese la contraseña oculta: ")
    print("La contraseña fue forzada en", fuerza_bruta(contraseña_oculta), "intentos")

