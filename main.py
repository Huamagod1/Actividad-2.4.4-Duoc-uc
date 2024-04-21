import os  
os.system("cls")

#Actividad 2.4.4. Ejercicio de los boletos.
#Prueba para ver como se comporta el modo remoto

#Ejercicio de los Buses

#1ero Partir preguntando 
#Pedir el precio de cada pasaje
#Si se ingresa un valor que no es un numero te indica que neesitas proporcionar un valor numerico valido
totalIngresos=0

while True:
 try:
       cantidad = int(input("Ingrese cantidad de pasajes que necesita\n"))

       for contador in range(cantidad):
        while True:
          try:
             precio = int(input(f"Favor indicar el precio del pasaje n° {contador+1} \n"))
             totalIngresos = totalIngresos + precio
             break
          except:
            print("Precio no existe")
       break
 except:
            print("Opcion no valida")

print(f"El Valor total a pagar por la cantidad de pasajes {cantidad} es de: {totalIngresos}")