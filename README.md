# Código para ordenar monedas
Este código se utiliza para ordenar una cantidad dada de dinero en monedas de diferentes denominaciones.

## Función ordenar_monedas(cantidad)
La función ordenar_monedas toma como argumento una cantidad de dinero y devuelve una lista con la cantidad de monedas necesarias para representar esa cantidad, ordenadas de mayor a menor denominación.

def ordenar_monedas(cantidad):
    monedas = [1000, 500, 200, 100, 50]
    cantidades = [0, 0, 0, 0, 0]
    for i, m in enumerate(monedas):
        if cantidad >= m:
            cantidades[i] = cantidad // m
            cantidad = cantidad % m
    return cantidades
La lista monedas contiene las denominaciones de las monedas, en orden de mayor a menor valor. La lista cantidades se utiliza para almacenar la cantidad de cada tipo de moneda necesaria para representar la cantidad dada.

El cuerpo de la función itera sobre la lista monedas y, para cada moneda, verifica si es posible representar la cantidad restante con monedas de esa denominación. Si es posible, se divide la cantidad restante por la denominación de la moneda y se guarda el resultado en cantidades[i]. La cantidad restante se actualiza como el módulo de la cantidad original y la denominación de la moneda.

Después de iterar sobre todas las denominaciones, la función devuelve la lista cantidades.

## Uso del código
El código incluye una sección que pide al usuario que introduzca la cantidad a ordenar y muestra el resultado de llamar a la función ordenar_monedas.

cantidad = int(input("Introduce la cantidad a ordenar: "))
resultado = ordenar_monedas(cantidad)
print("Monedas de 1000: ", resultado[0])
print("Monedas de 500: ", resultado[1])
print("Monedas de 200: ", resultado[2])
print("Monedas de 100: ", resultado[3])
print("Monedas de 50: ", resultado[4])
La cantidad a ordenar se pide al usuario como una entrada y se convierte a un número entero. Luego, se llama a la función ordenar_monedas con la cantidad introducida como argumento y se guarda el resultado en la variable resultado. Finalmente, se imprimen las cantidades de cada tipo de moneda en el resultado.
