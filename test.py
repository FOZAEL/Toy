from urllib import response
import requests

BASE = "http://localhost:5000"

response = requests.get(BASE + "/hello/Fozael")

print(response.json())