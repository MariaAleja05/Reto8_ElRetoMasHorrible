# -*- coding: utf-8 -*-
"""Punto_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RyLPKr76XsXXICfinr2kBoVhA43Up0iB

##**Punto 1**

**Enunciado:** Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
"""

cuadrado=1
Lista=[]

for i in range (1,101):
  cuadrado = i**2
  Lista.append(cuadrado)

print(Lista)