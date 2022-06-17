from urllib import response
import requests


response = requests.get("http://localhost:5000" + "/hello/Fozael")

print(response.json()['massage'])