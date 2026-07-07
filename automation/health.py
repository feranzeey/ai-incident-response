import requests

response = requests.get("http://localhost:5000")

print("Status Code:", response.status_code)

print("Response:")

print(response.text)