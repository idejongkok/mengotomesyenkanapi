import requests
import json
from jsonschema import validate, ValidationError

# method get
BASE_URL = "https://reqres.in"

def test_get_user():
    response = requests.get(BASE_URL+'/api/users/2')

    print(response.status_code)
    
    assert response.status_code == 200
    
def test_create_user():
    file = open('data.json','r')
    body = json.loads(file.read())
    
    schema = {
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "job": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "createdAt": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "job",
    "id",
    "createdAt"
  ]
}

    response = requests.post(url=BASE_URL+'/api/users',json=body)
    resp = json.loads(response.text)
    
    assert response.status_code == 201
    assert resp['name'] == 'sentot'
    assert resp['job'] == 'ketua RT'
    
    try:
        validate(instance=response.json(), schema=schema)
        
    except ValidationError as e:
        assert False, f" JSON Schema error: {e}"
    