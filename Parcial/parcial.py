""" ###ACT 1###

from random import randint
from funciones import altura
from consumo_api import get_charter_by_id
from funciones import peso

id1 = randint(1,83),
personaje1 = get_charter_by_id(1)

id2 = randint(1,83),
personaje2 = get_charter_by_id(2)

##A##

if (altura(personaje1) > altura(personaje2)) :
   print ("El personaje mas alto es",personaje1["name"],"la altura es", altura(personaje1))


else:
    print ("El personaje mas alto es",personaje2["name"],"la altura es", altura(personaje2))

##B##

if (peso(personaje1)) > (peso(personaje2)):

   print ("El personaje mas pesado es",personaje1["name"],"el peso es", altura(personaje1))

else:
    print ("El personaje mas pesado es",personaje2["name"],"el peso es", altura(personaje2))

##D##

if (personaje1 == "Yoda" or personaje2 == "Grievous" or  personaje1 == "Grievous" or personaje2 == "Yoda") :
    print(personaje1)
    print(personaje2)



 ###ACT3###

from random import randint
lista = []

for i in range (0,78):
    num = randint(1,3000)
    lista.append(num)

lista.sort()

print ("El menor es ",lista[0])
print ("El mayor es ",lista[77])

print(lista)
for lista in range (0,500):
    if (lista % 2==0):
        print(lista) """

##Act2##

import json
import requests

def consultar_personajes(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        diccionario = json.loads(respuesta.text)
        return diccionario
    else:
        print('nope')


urlbase = consultar_personajes('https://swapi.dev/api/people/')


sw_data = []

while(urlbase['next'] is not None):
    for doc in urlbase['results']:
        sw_data.append(doc)
    urlbase = consultar_personajes(urlbase['next'])



def nombre (item):
    return (item['name'])

sw_data.sort(key=nombre)

for index, character in enumerate(sw_data):
    
    print(character['name'],character['homeworld'],character['species'])