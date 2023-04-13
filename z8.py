import kivy

kivy.require("1.10.1")
from kivy.uix.scrollview import ScrollView
import os
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty


class Przelicznik():
    def __init__(self, name, balance,kurs):
        self.kurs = kurs
        self.name = name
        self.__balance__ = balance

    def getBalance(self):
        return (self.__balance__)

    def setBalance(self, zmena):
        self.__balance__ = str(zmena * self.kurs) + " PLN"

"""
class FloatInput(acc):
    pat = re.compile('[^0-9.]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            # don't allow more than one decimal point
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([
                re.sub(pat, '', ss)
                for ss in substring.split('.', 1)
            ])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)
"""

class Kalkulator(Screen):
    acc = ObjectProperty(None)
    balance = StringProperty('')
    
    def __init__(self, **kwargs):
        super(Kalkulator, self).__init__(**kwargs)
        self.acc = Przelicznik("Main", 0, 4.3)
        self.update_balance()
    # Set label positions
        self.ids.lb1.pos_hint = {'center_x': 1, 'center_y': 0.8}
    
        self.ids.lb2.pos_hint = {'center_x': 1, 'center_y': 0.6}

        self.ids.lb3.pos_hint = {'center_x': 1, 'center_y': 0.5}

        self.ids.tp.pos_hint = {'center_x': 0.5, 'center_y': 0.35}

        self.ids.btn1.pos_hint = {'center_x': 0.5, 'center_y': 0.2}


    def update_balance(self):
        self.balance = str(self.acc.getBalance())

class Custom(Screen):
    pass

class Aktywa(Screen):
    pass

class Ustawienia(Screen):
    pass

Builder.load_file("z8.kv")

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