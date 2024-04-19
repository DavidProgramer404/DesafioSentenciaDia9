import sys

# Verificar si se proporciona el umbral como argumento
if len(sys.argv) != 2:
    print("Por favor, proporcione exactamente un umbral como argumento.")
    sys.exit(1)

# Intentar convertir el umbral a un entero
umbral_str = sys.argv[1]
if not umbral_str.isdigit():
    print("Por favor, proporcione un umbral válido como argumento.")
    sys.exit(1)


# Diccionario de ventas
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

# Filtrar los meses que superan el umbral especificado
meses_superiores = {mes: valor for mes, valor in ventas.items() if valor > int(umbral_str)}

print(meses_superiores)



"""
Codigo de Luis
import sys

def obtener_meses_mayor_a(umbral, ventas):
    meses_mayor_a = {}
    for mes, monto in ventas.items():
        if monto > umbral:
            meses_mayor_a[mes] = monto
    return meses_mayor_a

if __name__ == "__main__":
    ventas = {
        "Enero": 15000,
        "Febrero": 22000,
        "Marzo": 12000,
        "Abril": 17000,
        "Mayo": 81000,
        "Junio": 13000,
        "Julio": 21000,
        "Agosto": 41200,
        "Septiembre": 25000,
        "Octubre": 21500,
        "Noviembre": 91000,
        "Diciembre": 21000,
    }
    umbral = int(sys.argv[1])
    resultados = obtener_meses_mayor_a(umbral, ventas)
    print(resultados)

"""