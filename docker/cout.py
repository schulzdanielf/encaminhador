import sys
import requests

print("Python : ",sys.argv[1])

url = 'http://localhost:8889/incidente/'
myobj = {'action':sys.argv[1], 'equipe':'2', 'hostname':'evento'}

x = requests.post(url, data = myobj)
