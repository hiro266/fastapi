import requests
import asyncio
import time

res = requests.get('http://localhost:8000/sample/', headers={"Authorization": "Bearer XXX"})
# res = requests.post('http://localhost:8000/items/', json={"name": "サッカーボール", "price": 1000, "description": "サッカーボールです"})

print(res.status_code)
print(res.text)
print(res.headers)
