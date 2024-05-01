import json

import requests

base_url = 'https://reqres.in/api/users'

header = {
    'Content-Type': 'application/json'
}

json_file = open('./users.json')
json_payload = json.load(json_file)

response = requests.post(url=base_url, headers=header, data = json.dumps(json_payload))
assert response.status_code == 201
print(response.text)
