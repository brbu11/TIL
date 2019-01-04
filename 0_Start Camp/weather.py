 import requests
 url = 'https://api.darksky.net/forecast/67a4709ee0b80f25d8ef923a6bba5e6e/37.5013697,127.0380784'

res = requests.get(url)
 data = res.json()

 print(data['currently']['summary'])

{'key' : 'value'}

from darksky import forecast
multicampus = forecast('67a4709ee0b80f25d8ef923a6bba5e6e',37.5013697,127.0380784)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])
