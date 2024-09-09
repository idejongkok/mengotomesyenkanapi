import requests
import json

BASE_URL = "https://reqres.in"
endpoint = "/api/users/2"

body = {
    "name": "sentot",
    "job": "ketua RT"
}

response = requests.put(url=BASE_URL+endpoint,json=body)

print(response.status_code)
resp = json.loads(response.text)
print(resp)
print(type(resp))
