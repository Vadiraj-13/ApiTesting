import requests

url = 'https://gorest.co.in/public/v2/users'

head = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 0fcbe4ab7d2d42c92a8f2cf346d8fed8a96a08b9896defe5a7e609586afe3aa5'
}

body = {
    "name": "Ram Somayaji",
    "email": "ram1_charuchandra@kuhn.test",
    "gender": "male",
    "status": "inactive"
}

response = requests.post(url=url, headers=head, json=body)
assert response.status_code == 201

getUrl = url + "/" + str(response.json()['id'])

getHead = {
    'Authorization': 'Bearer 0fcbe4ab7d2d42c92a8f2cf346d8fed8a96a08b9896defe5a7e609586afe3aa5',
    'Accept': 'text/plain'
}
getResponse = requests.get(url=getUrl, headers=getHead)

assert getResponse.status_code == 200

print(getResponse.json())

