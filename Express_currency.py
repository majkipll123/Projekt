import kivy

kivy.require("1.10.1")
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder

from kivy.properties import  ObjectProperty, StringProperty
from kivy.core.window import Window
from kivy_garden.mapview import  MapMarker
from kivy.utils import platform
import requests


#lagn false = en
#lang true = pl
Lang = False

class Kalkulator(Screen):
    acc = ObjectProperty(None)
    balance = StringProperty('')

    

    def __init__(self, **kwargs):
        
        super(Kalkulator, self).__init__(**kwargs)
        
        self.url= "https://api.apilayer.com/exchangerates_data/symbols"
        self.payload = {}
        self.headers= {
            "apikey": "xoVqRitppuJgc9tx8Q45wayzXqWuAehN"
        }    
        if Lang:
            self.ids.spinner_id.text = "Wybierz walute z której chcesz przeliczyć"
            self.ids.spinner_id2.text = "Wybierz walute na jaką chcesz przeliczyć"
        else:
            self.ids.spinner_id.text = "Choose currency you want to convert from"
            self.ids.spinner_id2.text = "Choose currency you want to convert to"
        
    
    def zamien_miejscami(self, a, b):
        self.ids.spinner_id.text = b
        self.ids.spinner_id2.text = a
    def change_lang(self):
        #"<Screen name='Kalkulator'>"
        if Lang:     
            
            self.ids.lb3.text = "Tranzakcja z:"+" "+self.acc.from_currency+" "+"na"+" "+self.acc.to_currency
            
            self.ids.lb1.text = "Kalkulator walut"
            self.ids.tp.hint_text = "Wpisz kwotę"
            self.ids.btn1.text = "Przelicz"
            self.ids.btn2.text = "Zmień waluty miejscami"
            """
            tu trzeba bedzie pokombinowac z globana wartoscia i jakins boolem i dobra funckja ale 
            bedzie sie to dało zrobic na luzie lub nie na luzie
            self.ids.spinner_id.text = "Wybierz walute z której chcesz przeliczyć"
            self.ids.spinner_id2.text = "Wybierz walute na jaką chcesz przeliczyć"
            """
           
        else:
            self.ids.lb1.text = "Currency converter"
            self.ids.tp.hint_text = "Enter amount"
            self.ids.btn1.text = "Convert"
            self.ids.btn2.text = "Swap currencies"
            """
            self.ids.spinner_id.text = "Choose currency you want to convert from"
            self.ids.spinner_id2.text = "Choose currency you want to convert to"
            """
            try:
                self.ids.lb3.text = "Transaction from:"+" "+self.acc.from_currency+" "+"to"+" "+self.acc.to_currency
            except:
                pass




    def update_from_currency(self,value,value2):
    

        self.from_currency = value 
        self.to_currency = value2
        
        self.acc = Przelicznik("Main", 0,value,value2)
        
        #self.response = requests.request("GET", self.url, headers=self.headers, data = self.payload)
        #self.symbols = self.response.symbols
    
        

    # Set label positions
        self.ids.lb1.pos_hint = {'center_x': 1, 'center_y': 0.8}

    
        self.ids.lb2.pos_hint = {'center_x': 1, 'center_y': 0.6}

        

        self.ids.lb3.pos_hint = {'center_x': 1, 'center_y': 0.5}
        
        self.ids.tp.pos_hint = {'center_x': 0.5, 'center_y': 0.35}
        self.ids.spinner_id.text
        self.ids.btn1.pos_hint = {'center_x': 0.5, 'center_y': 0.2}




    


    def update_balance(self):
        self.balance = str(self.acc.getBalance())


class Przelicznik():
    def __init__(self, name, balance, from_currency,to_currency):
        
        self.name = name
        self.__balance__ = balance
        print(self.__balance__)
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = balance

    def update_from_currency(self, value): 
            print(value)

    def getBalance(self):
        
        return (self.__balance__)

    def setText(self, text):
        self.__balance__ = self.from_currency

    def setBalance(self, abcd):
        url = "https://api.apilayer.com/exchangerates_data/convert"


        querystring = {"to":str(self.to_currency[:3]),"from":str(self.from_currency[:3]),"amount":str(abcd)}

        headers= {
        "apikey": "xoVqRitppuJgc9tx8Q45wayzXqWuAehN"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        status_code = response.status_code
        result = response.json()
        result2 = "{:.2f}".format(result["result"])

        
        try:  
            self.__balance__ = result2+" "+self.to_currency
            
        except:
            if Lang:
                self.__balance__ = "Error: połączenie niestabilne"
            else:  
                self.__balance__ = "Error: connection unstable"


class Custom(Screen):
    acc = ObjectProperty(None)
    balance = StringProperty('')

    
 
    def __init__(self, **kwargs):
        
        super(Custom, self).__init__(**kwargs)

        self.url= "https://api.apilayer.com/exchangerates_data/symbols"
        self.payload = {}
        self.headers= {
            "apikey": "xoVqRitppuJgc9tx8Q45wayzXqWuAehN"
        }    
        self.ids.lc1.pos_hint = {'center_x': 0.5, 'center_y': 0.8}
        self.ids.lc2.pos_hint = {'center_x': 0.5, 'center_y': 0.9}

        

        self.ids.tc.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.ids.custom_id.pos_hint = {'center_x': 0.5, 'center_y': 0.35}
        
        self.ids.btnc.pos_hint = {'center_x': 0.5, 'center_y': 0.2}
        if Lang:     
            self.ids.lc1.text = "Kalkulator walut własnych"
            self.ids.tc.hint_text = "Wartość"
            self.ids.custom_id.hint_text = "Ustaw swój kurs"
            self.ids.btnc.text = "Przelicz"
        else:
            self.ids.lc1.text = "Custom currency converter"
            self.ids.tc.hint_text = "Amount"
            self.ids.custom_id.hint_text = "Set your own rate"
            self.ids.btnc.text = "Convert"
    
        
    def update_balance2(self,value):

        self.kurs = value 
        self.acc = Przelicznik_custom("Main", 0,value)
        
    def change_lang(self):
        
        if Lang:     
            self.ids.lc1.text = "Kalkulator walut własnych"
            self.ids.tc.hint_text = "Wartość"
            self.ids.custom_id.hint_text = "Ustaw swój kurs"
            self.ids.btnc.text = "Przelicz"
        else:
            self.ids.lc1.text = "Custom currency converter"
            self.ids.tc.hint_text = "Amount"
            self.ids.custom_id.hint_text = "Set your own rate"
            self.ids.btnc.text = "Convert"
    
    def update_balance(self):
        self.balance = str(self.acc.getBalance())


class Przelicznik_custom():
    def __init__(self, name, balance, kurs):
        
        self.name = name
        self.__balance__ = balance
        print(self.__balance__)
        self.kurs = kurs
        self.amount = balance
    """
    def update_from_currency(self, value): 
            print(value)
    """
    def getBalance(self):
        
        return (self.__balance__)

    def setText(self, text):
        self.__balance__ = self.kurs

    def setBalance(self, abcd):
    
        result2=str(float(self.kurs)*float(abcd))
        
        try:  
            if Lang:
                self.__balance__ = result2+ " oto ilość następującej waluty."
            else:
                self.__balance__ = result2+ " here is the amount of the following currency."
            
        except:
            if Lang:
                self.__balance__ = "Error: połączenie niestabilne"
            else:
                self.__balance__ = "Error: connection unstable"


class Aktywa(Screen):

    def __init__(self, **kwargs):
        super(Aktywa, self).__init__(**kwargs)

    
        
        

class Historia(Screen):

    def __init__(self, **kwargs):
        super(Historia, self).__init__(**kwargs)
        self.markers = []  

    def mapa(self, miejsce):
        plik = 'kraje_swiata.txt'  
        pasujace_znaki = self.ids.spinner_id3.text[:2]
        if pasujace_znaki == 'EU':
            wyjatki=["DE", "FR", "IT", "BE", "HR", "CY", "EE", "GR", "IE", "LV", "LT", "LU", "MT", "NL", "AT", "PT", "SK", "SI", "ES"]
            wyniki = znajdz_linie_pasujace(plik, wyjatki)
            
            for linia in wyniki:
                dane = linia.split(',')
                for linia in dane: 
                    latitude = float(dane[1])
                    longitude = float(dane[2])
                    marker = MapMarker(lat=latitude, lon=longitude)
                    self.markers.append(marker)  # Dodaj marker do listy
                    self.ids.mapview.add_marker(marker)
                    
        else:
            wyniki = znajdz_linie_pasujace(plik, pasujace_znaki)
            for linia in wyniki:
                
                
                dane = linia.split(',')
                print(dane)
                print(linia)
                latitude = float(dane[1])
                longitude = float(dane[2])
                marker = MapMarker(lat=latitude, lon=longitude)
                self.markers.append(marker)  # Dodaj marker do listy
                self.ids.mapview.add_marker(marker)
                

    def usun_wszystkie_markery(self):
        for marker in self.markers:
            self.ids.mapview.remove_marker(marker)
        self.markers = []  # Wyczyść listę markerów

def znajdz_linie_pasujace(plik, pasujace_znaki):
    wyniki = []
    with open(plik, 'r') as f:
        for linia in f:
            if any(znak in linia for znak in pasujace_znaki):
                wyniki.append(linia)
    return wyniki

   


class Ustawienia(Screen):

    acc = ObjectProperty(None)
    balance = StringProperty('')
    
    def __init__(self, **kwargs):
        
        super(Ustawienia, self).__init__(**kwargs)
        self.on_change()

    def on_change(self):
        if Lang:
            self.ids.btn11.text = 'Przelicznik walut'
            self.ids.btn12.text = 'Waluta własna'
            self.ids.btn13.text = 'Wszytkie dostępne aktywa'
            self.ids.btn14.text = 'Zmień język na angielski'
            self.ids.btn15.text = 'Historia i występowanie waluty'
        else:
            self.ids.btn11.text = 'Currency converter'
            self.ids.btn12.text = 'Custom currency'
            self.ids.btn13.text = 'All available assets'
            self.ids.btn14.text = 'Change language to polish'
            self.ids.btn15.text = 'History and occurrence of currency'
        
            


    """  self.refresh_kalkulator()
    
    
        

    def refresh_kalkulator(self):
        print(type(self))
        print(self)
        string = "<Screen name='Kalkulator'>"
        class_name = string.split("'")[1]
        klass = eval(class_name)
        Kalkulator.change_lang(self.klass)"""
        
    def zmien_jezyk(self):
        global Lang
        Lang = not Lang 
        print(Lang)


    


Builder.load_file("Express_currency.kv")

class MainApp(MDApp):
    

    def build(self):
       
    
        
        if(platform == 'android' or platform == 'ios'):
            Window.maximize()
        else:
            Window.size = (800,1200)
        
        sm = ScreenManager()
        sm.add_widget(Kalkulator(name='Kalkulator'))
        sm.add_widget(Custom(name='Custom')) 
        sm.add_widget(Aktywa(name='Aktywa'))
        sm.add_widget(Ustawienia(name='Ustawienia'))
        sm.add_widget(Historia(name='Historia'))
        return sm
        


if __name__ == "__main__":
    MainApp().run()
    