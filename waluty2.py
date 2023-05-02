import requests

url = "https://api.apilayer.com/exchangerates_data/convert"

from_currency = input("Enter the currency you want to convert from: ")
to_currency = input("Enter the currency you want to convert to: ")
amount = float(input("Enter the amount you want to convert: "))

class zapytanie():
    def __init__(self, from_currency, to_currency, amount):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount

    querystring = {"to":to_currency,"from":from_currency,"amount":str(amount)}

    headers= {
        "apikey": "xoVqRitppuJgc9tx8Q45wayzXqWuAehN"
     }

    response = requests.request("GET", url, headers=headers, params=querystring)

    status_code = response.status_code
    result = response.json()
    print(result["result"])
    print("Conversion result: ", result["result"])
