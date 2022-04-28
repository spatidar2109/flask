import requests
import json

with open("example.json") as f:
    data = json.load(f)
    
r = requests.post('http://127.0.0.1:5000/calc', json = data)
print(r.status_code)
print(r.text)