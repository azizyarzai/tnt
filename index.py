import requests
import json

res = requests.get("http://localhost:8000/api/students/")
data = json.loads(res.content)
for st in data:
    print(st['name'])
