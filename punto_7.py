# -*- coding: utf-8 -*-
"""Punto_7

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RyLPKr76XsXXICfinr2kBoVhA43Up0iB

# **Septimo Punto**

**Enunciado:** Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
"""

mult=1

for i in range(1, 10):
  print("------------------------------------------------")
  print("Tabla de multiplicar del " + str(i))
  for j in range (1, 11):
    mult=i*j
    print(str(i) + " x " + str(j) + " = " + str(mult))