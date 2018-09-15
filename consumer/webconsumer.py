import requests
import json
import sys


#Puedo declarar parametros que voy a usar en el request
parameters = {"lat": 40.71, "lon": -74}

#Digo cual es la URL de la cual voy a traer info y le paso los parametros
#response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)

if len(sys.argv)!=1:
    response = requests.get("http://localhost:5000/", sys.argv[1])
else:
    response = requests.get("http://localhost:5000/")

#Imprimo el string que me traigo
print(response.content)
#Lo convierto en un objeto JSON
#responseJson = response.json()

#Imprimo de ese objeto JSON el "atributo" en el campo message
#print (responseJson["message"])
