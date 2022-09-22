def monedas(dinero: int):

  lista = [1000,500,200,100,50]
  for i in lista:
    if (dinero >= i):
      queda = int(dinero // i)
      print("monedas de "+str(i)+ " son: " +str(queda))
      dinero = int(dinero % i)

dinero = int(input("Ingrese valor: "))
print(monedas(dinero))