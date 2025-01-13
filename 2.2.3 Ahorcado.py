'''''

import random
lista= ['perro', 'gato', 'avestruz','campana','brindis','dividir','ceder','doctor','carta','fingir','desierto','tulipan','abeja', 'tumba', 'edificio', 'novedoso', 'abril','azul','aguacate','blanco','banana', 'bolivia','lujo','lija','circo','cocina','maceta','charco','chile','coche','chino']

palabra_aleatoria = random.choice(lista)
palabra_mostrada=[]
intentos=7
letras_adivinadas=0
letras_antes_adivinadas=0
letras_dichas=set()

#Creamos la lista de guiones, según la longitud de la palabra
for i in range(len(palabra_aleatoria)):
    palabra_mostrada.append ("_")
print("La palabra es:",palabra_mostrada )

#Pedimos letra y comprobamos si la letra está en la palabra
def adivina_letra (letra):
    global intentos
    global letras_adivinadas
    acerto_letra= False
  
    for count, value in enumerate(palabra_aleatoria):
        if letra== value: #Aquí revisamos toda la palabra, letra a letra y sustituimos en letra mostrada si es que ha acertado
            palabra_mostrada[count]=letra
            letras_adivinadas = letras_adivinadas +1
            acerto_letra=True
            letras_dichas.add(letra)
    if acerto_letra : #Aquí verificamos si en todo el recorrido el for ha acertado alguna letra
        print("¡Has acertado una letra, tu progreso es:",palabra_mostrada)
    else:
        print ("No, esa no está:", palabra_mostrada)
        intentos -=1

while intentos>0 and(letras_adivinadas !=len(palabra_aleatoria)):
    letra=input ('Dime una letra a ver si está en la palabra')
    adivina_letra(letra)
    for count, value in enumerate(palabra_mostrada):
        if letras_adivinadas ==len(palabra_aleatoria):
            print("¡Enhorabuena, has ganado!, te quedaban ", intentos, " intentos, la palabra es:",palabra_mostrada)
            break
            
if intentos==0:
    print ("Has perdido, se han acabado los intentos, la respuesta era:",palabra_aleatoria)

'''''
import random
lista= ['perro', 'gato', 'avestruz','campana','brindis','dividir','ceder','doctor','carta','fingir','desierto','tulipan','abeja', 'tumba', 'edificio', 'novedoso', 'abril','azul','aguacate','blanco','banana', 'bolivia','lujo','lija','circo','cocina','maceta','charco','chile','coche','chino']

palabra_aleatoria = random.choice(lista)
palabra_mostrada=[]
intentos=7
letras_adivinadas=0
letras_antes_adivinadas=0
letras_dichas=set()

#Creamos la lista de guiones, según la longitud de la palabra
for i in range(len(palabra_aleatoria)):
    palabra_mostrada.append ("_")
print("La palabra es:",palabra_mostrada )

#Pedimos letra y comprobamos si la letra está en la palabra
def adivina_letra (letra):
    global intentos
    global letras_adivinadas
    acerto_letra= False

#Comprobamos si la letra ya la había dicho antes
    if letra in letras_dichas:
        return print("Esta letra :", letra, "ya la has dicho, introduce otra letra")

    letras_dichas.add(letra)
    
    for count, value in enumerate(palabra_aleatoria):
        if letra== value: #Aquí revisamos toda la palabra, letra a letra y sustituimos en letra mostrada si es que ha acertado
            palabra_mostrada[count]=letra
            letras_adivinadas = letras_adivinadas +1
            acerto_letra=True
            letras_dichas.add(letra)
    if acerto_letra : #Aquí verificamos si en todo el recorrido el for ha acertado alguna letra
        print("¡Has acertado una letra, tu progreso es:",palabra_mostrada)
    else:
        print ("No, esa no está:", palabra_mostrada)
        intentos -=1

while intentos>0 and(letras_adivinadas !=len(palabra_aleatoria)):
    letra=input ('Dime una letra a ver si está en la palabra')
    adivina_letra(letra)
    for count, value in enumerate(palabra_mostrada):
        if letras_adivinadas ==len(palabra_aleatoria):
            print("¡Enhorabuena, has ganado!, te quedaban ", intentos, " intentos, la palabra es:",palabra_mostrada)
            break
            
if intentos==0:
    print ("Has perdido, se han acabado los intentos, la respuesta era:",palabra_aleatoria)








