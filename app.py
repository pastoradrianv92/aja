import math
'''

a = input('Nombre')
b = input('Color')
msg = f'El color favorito de {a} es el {b}'
msg2=msg.upper()
c='Python' in a
print(msg2)
print(c)

'''

'''
a = 3.14
a=math.floor(a)
b=math.ceil(a)
print(a)
print(b)
'''

'''temperature=input('Es un dia soleado?: ')
if temperature == 'Si':
    print('Que tenga un dia brillante')
else : print('Abriguese bien y tome un chocolate caliente')'''

'''price = input('Precio')
good_credit = False
price = float(price)
if good_credit==True:

    new_price = price - price/10
    print('Down payment is 10% so the final payment is '+ str(new_price))
else:
    new_price = price - price / 20
    print('Down payment is 20% so the final payment is '+ str(new_price))'''


'''nombre = input('Introduzca nombre y apellido: ')
if len(nombre)<3:
    print('Por favor introduzca un nombre mayor a tres caracteres')
elif len(nombre)>20:
    print('El nombre no puede excederse de 10 caracteres')
else:
    print(f'Un gusto en saludarte {nombre}')'''

'''i=1
while i<6:
    print('*' * i)
    i=i+1'''

#Adivinar un numero (3 oportunidades)
'''i = 1
j = 0
while i < 4:
    a=input(f'Ingrese el numero')
    if int(a) == 7:
        print('Correcto')
        break
    else:
        if i == 3 and not int(a) == 7:
            print(f'Gracias por intentar, suerte para la proxima')
        else:
             b = 3-i
             print(f'Vuelva a intentar, le quedan {b} intentos')
        i = i+1'''


#El automovil
'''
a = ''
i = 0
while a.lower()!='finish':
    b = a
    a = input('> ').lower()
    if a == b and a == 'start':
        print('Yep, you already started. . .')
    elif a == b and a == 'stop' and i!=0:
        print('Yep, you already stopped remember?')
    else:
        if a == 'help':
            print(f'start-Start the car')
            print(f'stop-Stop the car')
            print(f'finish- Finish simulation')
        elif a == 'stop':
                if i == 0:
                    print('You didnt even started the car')
                else:
                    print('car stopped')
        elif a == 'start':
            i = i+1
            print(f'Car started, Ready to go')
        elif a == 'finish':
            break
        else:
            print('What?')
print('Thank you for playing')
'''
'''
for i in 'Liz Karolina':
    print(i)'''
'''for i in range(0,30,5):
    print(i)'''

#Calculo de costo total de shopping cart
'''prices = [10, 20, 30, 40, 50]
j = 0
for i in prices:
   j = j + i
print(f'{j}')'''

#Ejercicio de la F (LO LOGRE!)
'''
list = [5, 2, 5, 2, 2]
for i in list:
    j = 0
    while j < i+1:
        if i != j:
            print('*', end='')
        j = j + 1

    else:print('\n')
'''
#EJERCICIO DE LA F DE UNA MEJOR MANERA
'''
list = [5, 2, 5, 2, 2]
for i in list:
    salida = ''
    for j in range(i):
        salida = salida+'x'
    print(salida)
'''

#Hallar el numero mas alto de una lista
'''
lista = [12, 34, 67, 54, 32, 9, 56]
numero_grande = lista[0]
for i in lista:
    if i > numero_grande:
        numero_grande = i
print(numero_grande)
'''
'''
matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])

'''
'''
lista = [1, 4, 8, 2, 6, 8, 3, 7, 6]
lista2 = lista.copy()
lista.append(10)
lista.sort()
lista.reverse()
print(lista)
print(lista2)
'''
#ELIMINAR REPETIDOS (FORMA 1)
'''
lista = [2, 2, 4, 6, 3, 4, 6, 1, 2]
b = lista.copy()
b.reverse()
for i in b:
    a = b.count(i)
    while a != 1:
        b.remove(i)
        a = b.count(i)
b.reverse()
print(b)
'''

#ELIMINAR REPETIDOS 2
'''
lista = [2, 2, 4, 6, 3, 4, 6, 1, 2]
unicos = []
for i in lista:
    if i not in unicos:
        unicos.append(i)
print(unicos)
'''

'''
lista = [0, 1, 2, 3, 4, 5]
u, v, w, x, y, z = lista
print(x)
'''


'''
usuario = {
    'Nombre': 'Pastor Adrian',
    'Edad': 27,
    'Telefono': 1234
}

print(usuario['Edad'])
'''


#EJERCICIO NOMBRAR LOS NUMEROS------------------------------------------------------------------------------------------------
'''
Phone = input('Telefono')
respuesta = ''
digitos = {
    '0': 'Cero',
    '1': 'Uno',
    '2': 'Dos',
    '3': 'Tres',
    '4': 'Cuatro',
    '5': 'Cinco',
    '6': 'Seis',
    '7': 'Siete',
    '8': 'Ocho',
    '9': 'Nueve',
    '10': 'Diez'
}
for i in Phone:
   respuesta = respuesta + f'{digitos.get(i)} '
print(respuesta)'''

#CONVERTIDOR DE EMOJIS  -------------------------   codigos en la pagina https://unicode.org/emoji/charts/full-emoji-list.html
'''
a = input('> ')
b = a.split()
respuesta = ''
emojis = {
    ':)': '\U0001F600',
    ':(': '\U0001F615',
    ':O': '\U0001F632',
    'shit': '\U0001F4A9'
}
for i in b:
    if i in emojis:
        respuesta = respuesta + emojis[i] + ' '
    else:
        respuesta = respuesta + f'{i} '
print(respuesta)
'''
#CONVERTIDOR DE EMOJIS  -------------------------   POR MEDIO DEL COMANDO .get

'''
a = input('> ')
b = a.split()
respuesta = ''
emojis = {
    ':)': '\U0001F600',
    ':(': '\U0001F615',
    ':O': '\U0001F632',
    'shit': '\U0001F4A9'
}
for i in b:
    respuesta += emojis.get(i, i)+' '
print(respuesta)

'''
'''
def square(numero):
    return numero*numero

print(square(3))
'''

#CONVERTIDOR DE EMOJIS COMO UNA FUNCION
'''
def convertidor_emojis(a):
    b = a.split()
    respuesta = ''
    emojis = {
        ':)': '\U0001F600',
        ':(': '\U0001F615',
        ':O': '\U0001F632',
        'shit': '\U0001F4A9'
    }
    for i in b:
        if i in emojis:
            respuesta = respuesta + emojis[i] + ' '
        else:
            respuesta = respuesta + f'{i} '
    return respuesta
'''
#CONVERTIR EMOJIS COMO MENSAJE -------------------------------------------------------------------------------------------------
'''
mensaje = input('> ')
mensaje_emoji = convertidor_emojis(mensaje)
print(mensaje_emoji)
'''

#INTRODUCCION A LAS CLASES-----------------------------------------------------------------------------------------------------------------
'''
class Punto:
    def draw(self):
        print('draw')
    def hello(self):
        print('hello')

punto1 = Punto()
punto1.x = 10
punto1.y = 20
print(punto1.y)
punto1.draw()

'''


'''
class Person:

    def Talk(self):
        print('Talk?')


Pastor = Person()
Pastor.Talk()
'''


'''
class Person:

    def __init__(self, name):
         self.name = name

    def Talk(self):
        print(f'Hola soy {self.name}')

Pastor = Person('Pastor Adrian')
print(Pastor.name)
Pastor.Talk()
'''

#FUNCIONES PARA VARIAS CLASES--------------------------------------------------------------------------------------
'''
class Mammal:
    def talk(self):
        print('talking')

class Dog(Mammal):
    pass

class Cat(Mammal):
    pass


dog1 = Dog()
dog1.talk()

'''
'''
import convertidor

dolar = convertidor.dolar_euro(30)
print(dolar)
'''

'''
lista = [1, 3, 4,2, 7, 5,32, 78, 96, 45,34, 98, 65]
import utils
maxi = utils.maximo(lista)
print(maxi)
'''
#PAQUETES, MODULOS --------------------------------------------------------------------------------------------------------------
'''
import ecommerce.shipping
ecommerce.shipping.calc_shipping()
'''

#GENERAR AL AZAR------------------------------------------------------------------------------------------------------------
'''
import random
for i in range(3):
    print(random.randint(1,5))

lista = ['Pastor','Peter','Isabel','Linnet']
print(random.choice(lista))
'''
#EJERCICIO DEL DADO------------------------------------------------------------------------------------------------------------
'''
import random
class Dado:
    def lanzar(self):
        dado = (1, 2, 3, 4, 5, 6)
        print(f'({random.choice(dado)},{random.choice(dado)})')

dado1 = Dado()

dado1.lanzar()
'''
#EJERCICIO DEL DADO VERSION 2 CON CLASES Y SIN PRINT EN LA FUNCION------------------------------------------------------------------------------
'''
import random
class Dado:
    def lanzar(self):
        primero = random.randint(1,6)
        segundo = random.randint(1,6)
        return primero, segundo
dado = Dado()
print(dado.lanzar())
'''

#PRACTICANDO DIRECTORIOS


'''from pathlib import Path

camino = Path('ecommerce')
print(camino.exists())'''

'''
from pathlib import Path

camino = Path()

for archivo in camino.glob('*'):
    print(archivo)
'''

