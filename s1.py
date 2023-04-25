import kivy

kivy.require("1.10.1")
from kivy.uix.scrollview import ScrollView
import os
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel


from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp


from kivy.uix.widget import Widget
from kivy.properties import  ObjectProperty, StringProperty
from kivy.uix.dropdown import DropDown
import requests





class Przelicznik():
    def __init__(self, name, balance, from_currency, to_currency):
        
        self.name = name
        self.__balance__ = balance
        print(self.__balance__)
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = balance
    def getBalance(self):
        
        return (self.__balance__)

    def setText(self, text):
        self.__balance__ = self.from_currency

    def setBalance(self, abcd):
        url = "https://api.apilayer.com/exchangerates_data/convert"


        querystring = {"to":"PLN","from":"EUR","amount":str(abcd)}

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
            self.__balance__ = "Error: połączenie niestabilne"
"""
tutaj musi byc wywolanie classy ktora bedzie odpowiedzialna za budowanie listy z aktywami


class AktywaList():
    def __init__(self, **kwargs):
"""



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

        #self.response = requests.request("GET", self.url, headers=self.headers, data = self.payload)
        #self.symbols = self.response.symbols

        self.acc = Przelicznik("Main", 0,"PLN","USD")
        self.update_balance()
    # Set label positions
        self.ids.lb1.pos_hint = {'center_x': 1, 'center_y': 0.8}
    
        self.ids.lb2.pos_hint = {'center_x': 1, 'center_y': 0.6}

        self.ids.lb3.pos_hint = {'center_x': 1, 'center_y': 0.5}
        self.ids.lb3.text = self.acc.from_currency
        self.ids.tp.pos_hint = {'center_x': 0.5, 'center_y': 0.35}

        self.ids.btn1.pos_hint = {'center_x': 0.5, 'center_y': 0.2}


    def update_balance(self):
        self.balance = str(self.acc.getBalance())

class Custom(Screen):
    pass

class Aktywa(Screen):

    def __init__(self, **kwargs):
        super(Aktywa, self).__init__(**kwargs)
        self.dropdown = DropDown()
        for index in range(10):
            btn = Button(text='Value %d' % index, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)
        self.mainbutton = Button(text='Hello', size_hint=(None, None))
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.add_widget(self.mainbutton)

    pass
    

class Ustawienia(Screen):
    pass

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