import requests

url = "https://postman-echo.com/get"
querystring = {"test": "123"}
headers: dict = {}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
