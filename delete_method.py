import requests

BASE_URL = "https://reqres.in"
endpoint = "/api/users/2"

response = requests.delete(url=BASE_URL+endpoint)

print(response.status_code)
print(response.text)