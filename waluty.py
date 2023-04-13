from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import os

class Rates:
    def __init__(self, path):
        self.rates = {}
        if path.startswith("http"):
            # Pobierz kursy z API NBP
            response = requests.get(path, headers={"Accept": "application/xml"})
            if response.status_code == 200:
                root = ET.fromstring(response.content)
            else:
                print("Nie udało się pobrać danych z API NBP. Pobieram z pliku...")
                file_path = os.path.join(os.getcwd(), "a.xml")
                with open(file_path, "r") as f:
                    soup = BeautifulSoup(f, "xml")
                    root = soup.find("ExchangeRatesTable")
        else:
            # Otwórz lokalny plik z kursami
            with open(path, "r") as f:
                soup = BeautifulSoup(f, "xml")
                root = soup.find("ExchangeRatesTable")
        for child in root.iter("Rate"):
            currency = child.find("Code").text
            rate = child.find("Mid").text
            if rate is not None:
                self.rates[currency] = float(rate)

    def list_rates(self):
        print("List of available exchange rates:")
        for currency, rate in self.rates.items():
            print(f"{currency}: {rate}")

    def convert(self, from_currency, to_currency, amount, show_all=False):
        if show_all:
            self.list_rates()
            return None
        initial_amount = amount
        if from_currency != "PLN":
            if from_currency in self.rates:
                amount = amount / self.rates[from_currency]
            else:
                raise KeyError(f"{from_currency} not found in exchange rates")
        if to_currency in self.rates:
            # convert to target currency
            amount = amount * self.rates[to_currency]
        else:
            raise KeyError(f"{to_currency} not found in exchange rates")
        return amount

# przykładowe wywołanie z użyciem API NBP
rates = Rates("http://api.nbp.pl/api/exchangerates/tables/A/today/")
def main():
    rates.list_rates()
    from_currency = input("Enter currency to convert from (or type 'all' to see all rates): ")
    if from_currency == "all":
        rates.convert(None, None, None, show_all=True)
        return
    to_currency = input("Enter currency to convert to (or type 'all' to see all rates): ")
    if to_currency == "all":
        rates.convert(None, None, None, show_all=True)
        return
    try:
        amount = float(input("Enterter amount to convert: "))
    except ValueError:
        print("Invalid input. Amount must be a number.")
        return
    try:
        converted_amount = rates.convert(from_currency, to_currency, amount)
        print(f"Converted amount: {converted_amount}")
    except KeyError as e:
        print(str(e))

if __name__ == '__main__':
    main()
