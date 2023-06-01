import kivy

kivy.require("1.10.1")
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock

from kivy.properties import  ObjectProperty, StringProperty
from kivy.core.window import Window
from kivy_garden.mapview import  MapMarker
from kivy.utils import platform
import requests
#aplikacja włącza się standardowo w języku polskim
Lang = True

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
        


    def my_callback(self):
        event_trigger = Clock.create_trigger(self.change_lang())
        event_trigger()
    def zamien_miejscami(self, a, b):
        self.ids.spinner_id.text = b
        self.ids.spinner_id2.text = a
    def change_lang(self):
        #"<Screen name='Kalkulator'>"
        if Lang:     
            try:
                self.ids.lb3.text = "Tranzakcja z:"+" "+self.acc.from_currency+" "+"na"+" "+self.acc.to_currency
            except:
                pass   
            self.ids.lb1.text = "Kalkulator walut"
            self.ids.tp.hint_text = "Wpisz kwotę"
            self.ids.btn1.text = "Przelicz"
            self.ids.btn2.text = "Zmień waluty miejscami"
            
            self.ids.spinner_id.text = "Wybierz walute z której chcesz przeliczyć"
            self.ids.spinner_id2.text = "Wybierz walute na jaką chcesz przeliczyć"
            
           
        else:
            self.ids.lb1.text = "Currency converter"
            self.ids.tp.hint_text = "Enter amount"
            self.ids.btn1.text = "Convert"
            self.ids.btn2.text = "Swap currencies"
            
            self.ids.spinner_id.text = "Choose currency you want to convert from"
            self.ids.spinner_id2.text = "Choose currency you want to convert to"
            try:
                self.ids.lb3.text = "Transaction from:"+" "+self.acc.from_currency+" "+"to"+" "+self.acc.to_currency
            except:
                pass

    def update_bilans(self): 
        if Lang:
            try:
                self.ids.lb3.text = "Tranzakcja z:"+" "+self.acc.from_currency+" "+"na"+" "+self.acc.to_currency
            except:
                pass   
        else:
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
        
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = balance

   
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
        self.change_lang()
        
        self.ids.btnc.pos_hint = {'center_x': 0.5, 'center_y': 0.2}


    
        
    def update_balance2(self,value):

        self.kurs = value 
        self.acc = Przelicznik_custom("Main", 0,value)
        
    def change_lang(self):
        
        if Lang:     
            self.ids.lc1.text = "Kalkulator walut własnych"
            self.ids.tc.hint_text = "Wartość"
            self.ids.custom_id.hint_text = "Ustaw swój kurs"
            self.ids.btnc.text = "Przelicz"
            self.ids.top_app_bar.title="Kalkulator walut własnych"
        else:
            self.ids.lc1.text = "Custom currency converter"
            self.ids.tc.hint_text = "Amount"
            self.ids.custom_id.hint_text = "Set your own rate"
            self.ids.btnc.text = "Convert"
            self.ids.top_app_bar.title="Custom currency converter"

    def update_balance(self):
        self.balance = str(self.acc.getBalance())


class Przelicznik_custom():
    def __init__(self, name, balance, kurs):
        
        self.name = name
        self.__balance__ = balance
       
        self.kurs = kurs
        self.amount = balance
   
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
        self.change_lang()
        
    def change_lang(self):
        if Lang:
            self.ids.lc1.text = "Wszystkie dostępne waluty"
            self.ids.spinner_id5.text="Pokaż listę"
            self.ids.lc2.text = "Wszystkie dostępne aktywa"
            self.ids.spinner_id6.text="Pokaż listę"
            self.ids.top_app_bar.title="Wszystkie dostępne waluty i aktywa"
        else:
            self.ids.lc1.text = "All available currencies"
            self.ids.spinner_id5.text="Show list"
            self.ids.lc2.text = "All available assets"
            self.ids.spinner_id6.text="Show list"
            self.ids.top_app_bar.title="All available currencies and assets"

class Historia(Screen):

    def __init__(self, **kwargs):
        super(Historia, self).__init__(**kwargs)
        self.change_lang()
        self.markers = []  

    def change_lang(self):
        if Lang:
            self.ids.spinner_id3.text="Wybierz walutę której wykorzystanie chcesz zobaczyć na świecie"
            self.ids.top_app_bar.title="Mapa wszystkich dostępnych walut "
            self.ids.usun.text="Usuń wszystkie markery"
        else:  
            self.ids.spinner_id3.text="Choose currency to see its usage around the world"
            self.ids.top_app_bar.title="Map of all available currencies"
            self.ids.usun.text="Remove all markers"
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
        elif pasujace_znaki == 'Ch':
            pass      
        else:
            wyniki = znajdz_linie_pasujace2(plik, pasujace_znaki)
            for linia in wyniki:
                
                
                dane = linia.split(',')
                
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
def znajdz_linie_pasujace2(plik, pasujace_znaki):
    wyniki = []
    with open(plik, 'r') as f:
        for linia in f:
            if pasujace_znaki in linia:
                wyniki.append(linia)
    return wyniki


   


class Ustawienia(Screen):
    acc = ObjectProperty(None)
    balance = StringProperty('')
    
    def __init__(self,aktywa_instance,custom_instance,  historia_instance, kalkulator_instance, **kwargs):
        super(Ustawienia, self).__init__(**kwargs)
        self.custom = custom_instance
        self.kalkulator = kalkulator_instance
        self.aktywa = aktywa_instance
        self.historia = historia_instance
        self.on_change()


    def on_change(self):
        if Lang:
            self.ids.btn11.text = 'Przelicznik walut'
            self.ids.btn12.text = 'Waluta własna'
            self.ids.btn13.text = 'Wszytkie dostępne aktywa'
            self.ids.btn14.text = 'Zmień język na angielski'
            self.ids.btn15.text = 'Występowanie Waluty na świecie'
        else:
            self.ids.btn11.text = 'Currency converter'
            self.ids.btn12.text = 'Custom currency'
            self.ids.btn13.text = 'All available assets'
            self.ids.btn14.text = 'Change language to polish'
            self.ids.btn15.text = 'Currency usage around the world'
        
    def zmien_jezyk(self):
        global Lang
        Lang = not Lang 
        self.kalkulator.change_lang()
        self.custom.change_lang()
        self.historia.change_lang()
        self.aktywa.change_lang()
    


Builder.load_file("Express_currency.kv")

class MainApp(MDApp):
    

    def build(self):
       
        

        kalkulator = Kalkulator(name='Kalkulator')
        custom = Custom(name='Custom')  
        aktywa = Aktywa(name='Aktywa')
        historia = Historia(name='Historia')
        ustawienia = Ustawienia(aktywa_instance=aktywa , custom_instance=custom,historia_instance=historia, kalkulator_instance=kalkulator, name='Ustawienia')
        
        
        if(platform == 'android' or platform == 'ios'):
            Window.maximize()
        else:
            Window.size = (800,1200)
        
        sm = ScreenManager()
        sm.add_widget(kalkulator)
        sm.add_widget(custom)
        sm.add_widget(aktywa)
        sm.add_widget(historia)
        sm.add_widget(ustawienia)
        #sm.add_widget(Kalkulator(name='Kalkulator'))
        #sm.add_widget(Custom(name='Custom')) 
        #sm.add_widget(Aktywa(name='Aktywa'))
        #sm.add_widget(Ustawienia(name='Ustawienia'))
        #sm.add_widget(Historia(name='Historia'))
        return sm
        


if __name__ == "__main__":
    MainApp().run()
    