import requests
import json

BASE_URL = "https://reqres.in"
endpoint = "/api/users"

file = open('data.json','r')
body = json.loads(file.read())

response = requests.post(url=BASE_URL+endpoint,json=body)

print(response.status_code)
resp = json.loads(response.text)
print(resp)
print(type(resp))
