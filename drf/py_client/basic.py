import requests

# endpoint = 'https://httpbin.org/status/200/'
endpoint = 'http://127.0.0.1:8000/api/'

get_respose = requests.get(endpoint)
print(get_respose.text)
