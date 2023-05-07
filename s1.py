import kivy

kivy.require("1.10.1")
from kivy.uix.scrollview import ScrollView
import os
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel


from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner


from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp


from kivy.uix.widget import Widget
from kivy.properties import  ObjectProperty, StringProperty



import requests



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
        print(Lang)
        
    
    def change_lang(self, value):
        
        
        """
            
        """



    def update_from_currency(self,value,value2):
    

        self.from_currency = value 
        self.to_currency = value2
        
        self.acc = Przelicznik("Main", 0,value,value2)
        
        #self.response = requests.request("GET", self.url, headers=self.headers, data = self.payload)
        #self.symbols = self.response.symbols
    
        

    # Set label positions
        self.ids.lb1.pos_hint = {'center_x': 1, 'center_y': 0.8}

        self.ids.lb1.text = "Your currency converter"
    
        self.ids.lb2.pos_hint = {'center_x': 1, 'center_y': 0.6}

        

        self.ids.lb3.pos_hint = {'center_x': 1, 'center_y': 0.5}
        
        self.ids.tp.pos_hint = {'center_x': 0.5, 'center_y': 0.35}
        self.ids.spinner_id.text
        self.ids.btn1.pos_hint = {'center_x': 0.5, 'center_y': 0.2}

        if Lang:
            self.ids.lb3.text = "Tranzakcja z:"+" "+self.acc.from_currency+" "+"na"+" "+self.acc.to_currency
            self.ids.lb1.text = "Twój kalkulator walutowy"
            self.ids.tp.hint_text = "Wpisz kwotę"
            self.ids.btn1.text = "Przelicz"
            """
            self.ids.spinner_id.text = "Wybierz walute z której chcesz przeliczyć"
            self.ids.spinner_id2.text = "Wybierz walute na jaką chcesz przeliczyć"
            """
           
        else:
            self.ids.lb1.text = "Your currency converter"
            self.ids.tp.hint_text = "Enter amount"
            self.ids.btn1.text = "Convert"
            """
            self.ids.spinner_id.text = "Choose currency you want to convert from"
            self.ids.spinner_id2.text = "Choose currency you want to convert to"
            """
            self.ids.lb3.text = "Transaction from:"+" "+self.acc.from_currency+" "+"to"+" "+self.acc.to_currency
            


    


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
        result2=str(result["result"])
        
        try:  
            self.__balance__ = result2+" "+self.to_currency
            
        except:
            if Lang:
                self.__balance__ = "Error: połączenie niestabilne"
            else:  
                self.__balance__ = "Error: connection unstable"
"""
tutaj musi byc wywolanie classy ktora bedzie odpowiedzialna za budowanie listy z aktywami


class AktywaList():
    def __init__(self, **kwargs):
"""

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
        
        
    def update_balance2(self,value):
    

        self.kurs = value 
        
        
        self.acc = Przelicznik_custom("Main", 0,value)
        
        #self.response = requests.request("GET", self.url, headers=self.headers, data = self.payload)
        #self.symbols = self.response.symbols
    
        

    # Set label positions
        
# Set label positions
        self.ids.lc1.pos_hint = {'center_x': 0.5, 'center_y': 0.8}
        self.ids.lc2.pos_hint = {'center_x': 0.5, 'center_y': 0.9}

        

        self.ids.tc.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.ids.custom_id.pos_hint = {'center_x': 0.5, 'center_y': 0.35}
        
        self.ids.btnc.pos_hint = {'center_x': 0.5, 'center_y': 0.2}
    


    def update_balance(self):
        self.balance = str(self.acc.getBalance())


class Przelicznik_custom():
    def __init__(self, name, balance, kurs):
        
        self.name = name
        self.__balance__ = balance
        print(self.__balance__)
        self.kurs = kurs
        self.amount = balance

    def update_from_currency(self, value): 
            print(value)

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
        
    pass
    

class Ustawienia(Screen):

    acc = ObjectProperty(None)
    balance = StringProperty('')
    
    def __init__(self, **kwargs):
        
        super(Ustawienia, self).__init__(**kwargs)

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
    
       
        

    def refresh_kalkulator(self):
        Kalkulator.change_lang(self,Lang)
        
    def zmien_jezyk(self):
        global Lang
        Lang = not Lang
        print(Lang)


    


Builder.load_file("s1.kv")

class MainApp(MDApp):
    

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Kalkulator(name='Kalkulator'))
        sm.add_widget(Custom(name='Custom')) # use Custom here
        sm.add_widget(Aktywa(name='Aktywa'))
        sm.add_widget(Ustawienia(name='Ustawienia'))
        return sm


        
    
  





if __name__ == "__main__":
    MainApp().run()