# Reto número 8 repo
### Fecha:  04-10-2023
### Link notebook: https://colab.research.google.com/drive/1-UD-JkBPsWI-TXVp8vZ-jUWiJt-kswGH?usp=sharing
**1.** Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
* Para este problema primero definí mis variables n=1 ya que el listado debe comenzar desde 1 y, una lista vacía donde se van a ir incluyendo los cuadrados de los número.

Creé un for, el cuál funcionará dentro del rango de los números del 1 al 101 (para que se incluya el número 100). Dentro de este, se calcula el cuadrado del número y el resultado se añade a la lista. 

Cuando se hayan evaluado todos los números del rango, significa que el programa ya tendrá todos los cuadrados de los números desde 1 hasta 100 y el programa imprimirá la lista.

* Mirar archivo Punto_1.py
```pseudocode
cuadrado=1
Lista=[]

for i in range (1,101):
  cuadrado = i**2
  Lista.append(cuadrado)

print(Lista)
```
**2.** Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
* Para este problema primero creé una lista vacía donde se van a ir incluyendo los números impares (Lista_impares), y una lista vacía que tendrá los números pares (Lista_pares).

Creé un for, el cuál funcionará en el rango de números desde el 1 hasta el 1001 (para que se incluya el 1000). Dentro de este, hay un condicional if: i%2==0, que se usa para determinar si el número es par o impar, en caso de ser verdadera la condición el número se añadirá a la lista de pares, en el caso contrario, en la lista de impares. 

Cuando ya se hayan evaluado todos los números del rango del for, significa que el programa ya tendrá clasificado todos los números desde 1 hasta 1000 y el programa imprimirá la lista tanto de los número impares como los pares.
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
* Para este problema primero le solicité al ususario ingresar el número n, definí mis variables m=n, una lista donde se van a ir incluyendo los números pares.

Creé un for, el cuál funcionará durante el rango desde el numero n ingresado hasta el número 1, y cada valor que se evalúa se le irá restado una unidad(para hacerlo descendente comienzo desde n y le voy restando una unidad a este valor). Dentro de este, hay un condicional en el cual si i%2==0 significa que el número es par y por esta razón, se añadirá a la lista el elemento i. 

Cuando se hayan evaluado todos los números del rango del for, significa que el programa ya tendrá clasificado todos los números pares desde n hasta 2 y el programa imprimirá la lista de estos.
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
* Para este problema primero importé la función math para usar la operación de factorial, le solicité al ususario ingresar el numero entero n al cuál se le quiere calcular el factorial, y creé la variable factorial.

Creé un for, el cuál funcionará en el rango desde 1 hasta n+1 (para incluir n) y a el valor a evaluar se le irá sumando una unidad (para evaluarlos todos). Dentro de este, se realizan utiliza la función factorial para calcular el resultadp.

Cuando se hayan evaluado todos los números del rago del for, significa que ya se ha calculado el factorial, el programa imprimirá el resultado.
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
* Para este problema primero le solicité al ususario ingresar el numero entero n que será la potencia del número 2.

Creé un for, el cuál funcionará n-1 veces ya que la potencia de 2 a la cero es uno y de esta manera se puede calcular esta. Dentro del for se va realizando la operación de 2*2 para hallar la potencia final

Cuando se hayan evaluado n-1 veces el for, significa que ya se ha calculado la potencia, el programa imprimirá el resultado.
* Mirar archivo Punto_5.py
```pseudocode
n = int(input("Ingrese el número de la potencia: "))
potencia = 2

for i in range(n-1):
  potencia *= 2
  
print("El resultado es: " + str(potencia))
```
**6.** Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.
* Para este problema primero le solicité al ususario ingresar el numero natural n, un número real x, además, creé la variable operacion que tendrá el valor inicial de 1.

Creé un for, el cuál funcionará n-1 veces ya que la potencia de un número a la cero es uno y de esta manera se puede calcular esta. Dentro del for se va realizando la operación de multiplicar n veces el número por sí mismo.

Cuando se hayan evaluado n-1 veces el for, significa que ya se ha calculado la potencia, el programa imprimirá el resultado.
* Mirar archivo Punto_6.py
```pseudocode
n = int(input("Ingrese un número natural: "))
x = float(input("Ingrese un número real: "))
operacion = 1

for i in range(n-1):
  operacion *= x

print("El resultado es: " + str(operacion))
```
**7.** Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
* Para este problema primero creé la variable mult para poder imprimir más fácilmente las tablas.

Creé un for, el cuál funcionará en el rango desde 1 hasta 10 (para incluir la tabla del 9). Lo primero que se realiza es imprimir el valor i del for que se usa para saber la tabla de multiplicar a que número corresponde. Después, hay otro for que funciona en el rango desde 1 hasta 11 (para incluir en la tabla el x10) el cuál multiplicará en valor i por j (así funcionan las tablas de multiplicar ;) y este resultado se irá imprimiendo. 

Cuando se hayan evaluado todos los valores del primer for con todos los del segundo for, significa que ya se han calculado todas las tablas, el programa ya habrá imprimido todos los resultados.

Pdt: Si fuera más viejita, este programa me hubiera sacado muchas canas, a pesar de q se vea fácil...el proceso de descifrarlo no lo fue :)

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
