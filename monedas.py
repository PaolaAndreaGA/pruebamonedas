
# # Requerimiento: Desarrolle un algoritmo que devuelva un valor ingresado en la cantidad posible de monedas, siendo los valores de las monedas: 1000, 500, 200, 100, 50

# # Ejemplo: valor ingresado 1250
# Respuesta: 1000 * 1 | 200 * 1 | 50 * 1

def monedas(varoinit: int):
    if (varoinit > 0):
        dinero = int(varoinit // 1000)
        queda1000= int(varoinit % 1000)
        print(f"monedas de 1000 : {dinero}")

    if (queda1000 > 0):
        dinero = queda1000 // 500
        queda500 = queda1000 % 500
        print(f"monedas de 500 : {dinero}")

    if (queda500 > 0):
        dinero = queda500 // 200
        queda200 = queda500 % 200
        print(f"monedas de 200 : {dinero}")
    if (queda200 > 0):
        dinero = queda200 // 100
        queda100 = queda200 % 100
        print(f"monedas de 100 : {dinero}")
    if (queda100 > 0):
        dinero = queda100 // 50
        print(f"monedas de 50 : {dinero}")

varoinit = int(input("Ingrese valor: "))
print(monedas(varoinit))
