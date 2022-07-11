import requests
import json
import os
from datetime import date

Hoy = date.today()
Anio = str(Hoy.year)
Mes = str(Hoy.month) # TODO: Ojo que el mes no completa con cero a izquierda cuando es de un solo dígito

UrlBase = 'https://api.mercadolibre.com/sites/MLA/'
UrlNombreApi = 'search'
UrlParametros = 'category=MLA1000'

Formato = 'json'
NomCarpeta = UrlNombreApi + Formato + Anio + Mes
print(NomCarpeta)

UrlCompleta = UrlBase + UrlNombreApi + '?' + UrlParametros
res = None

try:
  res = requests.get(UrlCompleta)
except Exception as e:
# TODO: En un caso real tendría que tomar alguna acción concreta en caso de error  
  print(e)

if res != None and res.status_code == 200:
  print(json.loads(res.text))

# Si no existe la carpeta, la creo
isExist = os.path.exists(NomCarpeta)
if not isExist:
  os.makedirs(NomCarpeta)

# Guardo el archivo como json
UnJson = res.json()
out_file = open(NomCarpeta + "/archivo.json", "w") 
json.dump(UnJson, out_file, indent = 6) 
out_file.close() 