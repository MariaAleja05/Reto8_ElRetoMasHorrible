# Reto número 8 repo
### Fecha:  04-10-2023
### Link notebook:
**1.** Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
* EXPLICACIÓN
* Mirar archivo Punto_1.py
```pseudocode
cuadrado=1
Lista=[]

for i in range (1,101):
  cuadrado = i**2
  Lista.append(cuadrado)
  i += 1

print(Lista)
```
**2.** Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
* EXPLICACIÓN
* Mirar archivo Punto_2.py
```pseudocode
Lista_impares=[]
Lista_pares=[]

for i in range (1,1001):
  if i%2==0:
    Lista_pares.append(i)
  else:
    Lista_impares.append(i)

print("Los números impares: " + str(Lista_impares))
print("Los números pares: " + str(Lista_pares))
```
**3.** Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
* EXPLICACIÓN
* Mirar archivo Punto_3.py
```pseudocode
n = int(input("Ingrese un número mayor o igual a 2: "))
lista = []

for i in range(n, 1, -1):
  if i%2==0:
    lista.append(i)

print("Los números pares desde n hasta 2 son: " + str(lista))
```
**4.** Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
* EXPLICACIÓN
* Mirar archivo Punto_4.py
```pseudocode
import math as m
n = int(input("Ingrese un número natural: "))
factorial = 0

for i in range(1, n+1, +1):
  factorial = m.factorial(i)
  print("El factorial de " + str(i) + " es: " + str(factorial))
```
**5.** Calcular el valor de 2 elevado a la potencia n usando ciclos for.
* EXPLICACIÓN
* Mirar archivo Punto_5.py
```pseudocode
n = int(input("Ingrese el número de la potencia: "))
potencia = 2

for i in range(n-1):
  potencia *= 2
  
print("El resultado es: " + str(potencia))
```
**6.** Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.
* EXPLICACIÓN
* Mirar archivo Punto_6.py
```pseudocode
n = int(input("Ingrese un número natural: "))
x = float(input("Ingrese un número real: "))
operacion = x

for i in range(n-1):
  operacion = operacion*x
  
print("El resultado es: " + str(operacion))
```
**7.** Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
* EXPLICACIÓN
* Mirar archivo Punto_7.py
```pseudocode
mult=1

for i in range(1, 10):
  print("------------------------------------------------")
  print("Tabla de multiplicar del " + str(i))
  for j in range (1, 11):
    mult=i*j
    print(str(i) + " x " + str(j) + " = " + str(mult))
```
**8.** Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
* EXPLICACIÓN
* Mirar archivo Punto_8.py
```pseudocode

```
**9.** Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
* EXPLICACIÓN
* Mirar archivo Punto_9.py
```pseudocode

```
**10.** Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
* EXPLICACIÓN
* Mirar archivo Punto_10.py
```pseudocode

```
