import requests
header = {
    'Accept': 'text/plain'
}

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/3", headers=header)

print(response.status_code)
print(response.json())