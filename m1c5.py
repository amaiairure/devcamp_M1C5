#Ejercicio 1
notas = ['Do', 'Re', 'Mi']

for nota in notas:
  print(nota)

#Ejercicio 2
num_1=2
num_2=4
num_3=6

suma=num_1+num_2+num_3
print("La suma es: ",suma)

#Ejercicio 3
suma = lambda x, y: x + y

num_1 = 2
num_2 = 4

resultado = suma(num_1, num_2)
print("La suma es:", resultado)

#Ejercicio 4
lista_nombre = ["Jessica", "Paul", "George", "Henry", "Adán"]
nombre = "Enrique"
if nombre in lista_nombre:
    print(nombre)
else:
    print("El nombre no esta en la lista")