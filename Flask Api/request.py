import requests
from datainput import data_input

URL = 'http://127.0.0.1:5000/predict'
headers={"Content-Type": "application/json"}
data={"input":data_input}

r=requests.get(URl,headers=headers,json=data)

r.json()
