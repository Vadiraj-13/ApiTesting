import requests

header = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

requests_payload = {
    "id": 20,
    "title": "prashanth api testing course",
    "dueDate": "2024-04-23T04:49:02.549Z",
    "completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=header,
                         json=requests_payload)

print(response.status_code)
data = response.json()
print(data['id'])

assert response.status_code == 200
assert data['id'] == 20
