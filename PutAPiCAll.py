import requests

header = {
    'Accept': 'text/plain'
}

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/13", headers=header)

print("Before Update")
print(response.json())

header_put = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

putPayload = {
    "id": 14,
    "title": "vadiraj",
    "dueDate": "2024-04-23T05:25:56.875Z",
    "completed": True
}

response_put = requests.put(
    'https://fakerestapi.azurewebsites.net/api/v1/Activities/14',
    headers=header_put,
    json=putPayload
)

print("After Update")
print(response_put.json())
