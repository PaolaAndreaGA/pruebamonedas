def ordenar_monedas(cantidad):
    monedas = [1000, 500, 200, 100, 50]
    cantidades = [0, 0, 0, 0, 0]
    for i, m in enumerate(monedas):
        if cantidad >= m:
            cantidades[i] = cantidad // m
            cantidad = cantidad % m
    return cantidades

cantidad = int(input("Introduce la cantidad a ordenar: "))
resultado = ordenar_monedas(cantidad)
print("Monedas de 1000: ", resultado[0])
print("Monedas de 500: ", resultado[1])
print("Monedas de 200: ", resultado[2])
print("Monedas de 100: ", resultado[3])
print("Monedas de 50: ", resultado[4])
