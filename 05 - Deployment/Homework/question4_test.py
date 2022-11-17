import requests


port = 80
host = 'mlzoomcamp-homework.eba-pf85myp5.eu-west-1.elasticbeanstalk.com'

url = f"http://{host}:{port}/predict"

client = {"reports": 0, "share": 0.354, "expenditure": 3.5, "owner": "yes"}
response = requests.post(url, json=client).json()

print(response)
