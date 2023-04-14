

import requests

url = "https://api.apilayer.com/exchangerates_data/symbols"

payload = {}
headers= {
  "apikey": "xoVqRitppuJgc9tx8Q45wayzXqWuAehN"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(result)