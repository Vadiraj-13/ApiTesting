import requests

url = 'https://gorest.co.in/public/v2/users'

parameters = {
    'page': 2,
    'per_page': 1
}

response = requests.get(url=url, params=parameters)
print(response.json())

assert response.status_code == 200
