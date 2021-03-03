# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:39:50 2021

@author: jorge
"""

"""1. En una llantera se ha establecido una promoción de las llantas marca
Ponchadas, dicha promoción consiste en lo siguiente: Si se compran menos
de cinco llantas el precio es de $300 cada una, de $250 si se compran de
cinco a 10 y de $200 si se compran más de 10. Obtener la cantidad de dinero
que una persona tiene que pagar por cada una de las llantas que compra y la
que tiene que pagar por el total de la compra."""

llantas_a_comprar = int(input('Ingrese el número de llantas que va a comprar: '))
llantas_5 = 300
llantas_5_10 = 250
llantas_10 = 200

if llantas_a_comprar < 5:
    total = llantas_a_comprar * llantas_5
    print(f'El precio a pagar por cada una de las {llantas_a_comprar} llantas es: ${llantas_5}')
    print(f'El precio total por las {llantas_a_comprar} llantas es de: ${total}')
    
elif llantas_a_comprar >= 5 and llantas_a_comprar <= 10:
    total = llantas_a_comprar * llantas_5_10
    print(f'El precio a pagar por cada una de las {llantas_a_comprar} llantas es: ${llantas_5_10}')
    print(f'El precio total por las {llantas_a_comprar} llantas es de: ${total}')
    
elif llantas_a_comprar > 10:
    total = llantas_a_comprar * llantas_10
    print(f'El precio a pagar por cada una de las {llantas_a_comprar} llantas es: ${llantas_10}')
    print(f'El precio total por las {llantas_a_comprar} llantas es de: ${total}')



"""2. Hacer algoritmo que de el valor final por la compra de televisores. El
descuento lo hace basado en los dos numeros finales a la cédula, si
termina en 01 el descuento es del 10% y si termina en 25 el descuento es
del 20%, si termina en 44 el descuento es 35% y si es 57 el 50%."""

precio_total = int(input('Ingrese el precio total de los televisores: $'))
cedula = input('Ingrese los 2 últimos digitos de su cedula: ')

if cedula == '01':
    con_descuento = precio_total * 0.9
    print(f'El valor de la compra con el descuento por cédula es: ${con_descuento}')

elif cedula == '25':
    con_descuento = precio_total * 0.8
    print(f'El valor de la compra con el descuento por cédula es: ${con_descuento}')
    
elif cedula == '44':
    con_descuento = precio_total * 0.65
    print(f'El valor de la compra con el descuento por cédula es: ${con_descuento}')
    
elif cedula == '57':
    con_descuento = precio_total * 0.5
    print(f'El valor final de la compra con el descuento por cédula es: ${con_descuento}')


"""3. Una empresa de colchones ofrece descuento según la siguiente tabla
Numero de colchones
comprados
% Descuento
De 0 a menos de 3 0%
De 3 hasta menos de 6 20%
De 6 hasta menos de 8 25%
De 8 en adelante 30%
Determine cuanto pagará una persona que compre colchones"""

precio_total = int(input('Ingrese el precio total de los colchones: $'))
colchones_comprar = int(input('Ingrese el número de colchones que va a comprar: '))

if colchones_comprar < 3:
    print(f'El precio a pagar por los {colchones_comprar} colchones es de: ${precio_total}')

elif colchones_comprar >= 3 and colchones_comprar < 6:
    total_compra = precio_total * 0.8
    print(f'El precio a pagar por los {colchones_comprar} colchones es de: ${total_compra}')

elif colchones_comprar >= 6 and colchones_comprar < 8:
    total_compra = precio_total * 0.75
    print(f'El precio a pagar por los {colchones_comprar} colchones es de: ${total_compra}')

elif colchones_comprar >= 8:
    total_compra = precio_total * 0.7
    print(f'El precio a pagar por los {colchones_comprar} colchones es de: ${total_compra}')



"""4. Una universidad desea seleccionar una muestra de estudiantes para
realizar una encuesta. Si el número de estudiantes es menor que 20 se
tomará el 50%, si el salón tiene entre 20 y 30 estudiantes se tomará 60%,
si la cantidad es mayor a 30 tomará 70%. ¿Que cantidad de estudiantes
serán seleccionados para la encuesta?."""

numero_estudiantes = int(input('Ingrese el número de alumnos del salon: '))

if numero_estudiantes < 20:
    muestra = round(numero_estudiantes * 0.5)
    print(f'{muestra} estudiantes serán seleccionados para la encuesta')

elif numero_estudiantes >= 20 and numero_estudiantes <= 30:
    muestra = round(numero_estudiantes * 0.6)
    print(f'{muestra} estudiantes serán seleccionados para la encuesta')

elif numero_estudiantes > 30:
    muestra = round(numero_estudiantes * 0.7)
    print(f'{muestra} estudiantes serán seleccionados para la encuesta')









