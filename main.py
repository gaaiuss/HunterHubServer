# Tutorial https://www.youtube.com/watch?v=Qd8JT0bnJGs
import requests

url = 'http://localhost:8000/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.text)
