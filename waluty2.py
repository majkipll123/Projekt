import requests

url = "https://api.apilayer.com/exchangerates_data/convert"

from_currency = input("Enter the currency you want to convert from: ")
to_currency = input("Enter the currency you want to convert to: ")
amount = float(input("Enter the amount you want to convert: "))

querystring = {"to":to_currency,"from":from_currency,"amount":str(amount)}

headers= {
  "apikey": "xoVqRitppuJgc9tx8Q45wayzXqWuAehN"
}

response = requests.request("GET", url, headers=headers, params=querystring)

status_code = response.status_code
result = response.json()

print("Conversion result: ", result["result"])
