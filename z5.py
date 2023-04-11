import os
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty
import re


KV = """
Windowmanager:
    Kalkulator:
    Ustawienia:
    Aktywa:
    Custom:
    Jezyki:
<Kalkulator>:
    name: "Kalkulator"
    
    MDScreen:
    
        MDBoxLayout:
            id:box
            orientation: "vertical"
            md_bg_color: "#3A3E59"
            MDTopAppBar:
                mode: "end"
                md_bg_color: "#C36B84"
                title: "Express Currency "
                MDFloatingActionButton:
                    md_bg_color:"F9AC66"
                    icon: "account-cash"
                    pos_hint: {"center_x": .1, "center_y": .1}
                    spacing: "56dp"
                    text: 'Back to menu'
                    on_press:
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'Ustawienia'
            
        MDBoxLayout:
            def 
            orientation: "horizontal"
            
            FloatInput:
                text: "0"
                
                input_type: 'number'  
                id: float_input
                name: "waluta1"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: 1, .1
                multiline: False
                mode: "rectangle"
                hint_text: "Enter amount"
                helper_text: "Enter amount"
                helper_text_mode: "on_focus"
                icon_left: "cash"
                icon_left_color: app.theme_cls.primary_color
                hint_text: "Euro"
                height: "10dp"
                on_focus: 
                    self.text
                    
          
            MDTextField:
                id: wynik
                name: "wynik"
                pos_hint: {"center_x": .5, "center_y": .5}
                multiline: False
                mode: "rectangle"
                hint_text: "Enter amount"
                helper_text: "Enter amount"
                helper_text_mode: "on_focus"
                icon_left: "cash"
                icon_left_color: app.theme_cls.primary_color
                hint_text: "Złoty"
                on_focus: 
                    self.text= self.text*2
                height: "10dp"
                
<Custom>:
    name: "Custom"
        
    MDScreen:
    
        MDBoxLayout:
            id:box
            orientation: "vertical"
            md_bg_color: "#C36B84"
            
            MDTopAppBar:
                md_bg_color: "#F9AC66"
                title: "Waluta własna "
                MDFloatingActionButton:
                    pos_hint: {"center_x": .5, "center_y": .1}
                    md_bg_color:"#ED6B5B"
                    icon: "account-cash"
                    spacing: "56dp"
                    text: 'Back to menu'
                    on_press:
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'Ustawienia' 
            
                    
            
        MDBoxLayout:
            orientation: "horizontal"
            
            MDTextField:
                id: waluta1
                pos_hint: {"center_x": .5, "center_y": .5}
                multiline: False
                mode: "rectangle"
                hint_text: "Enter amount"
                helper_text: "Enter amount"
                helper_text_mode: "on_focus"
                icon_left: "cash"
                icon_left_color: app.theme_cls.primary_color
                hint_text: "Waluta użytkowanika 1 "
                
                height: "10dp"
             
            MDTextField:
                id: kurs
                pos_hint: {"center_x": .5, "center_y": .5}
                multiline: False
                mode: "rectangle"
                hint_text: "Enter amount"
                helper_text: "Enter amount"
                helper_text_mode: "on_focus"
                icon_left: "cash"
                icon_left_color: app.theme_cls.primary_color
                hint_text: "Twoja waluta"
                
                height: "10dp"
            
    
            
            MDTextField:
            
                id: waluta2
                pos_hint: {"center_x": .5, "center_y": .5}
                multiline: False
                mode: "rectangle"
                hint_text: "Enter amount"
                helper_text: "Enter amount"
                helper_text_mode: "on_focus"
                icon_left: "cash"
                icon_left_color: app.theme_cls.primary_color
                hint_text: "Twoja waluta"
                
                height: "10dp"
    
<Aktywa>:
    name: "Aktywa"
    MDScreen:
    
        MDBoxLayout:
            id:box
            orientation: "vertical"
            md_bg_color: "#C36B84"
            TextInput: 
                text: "Wszystkie dostępne towary"
                readonly: True
            TextInput: 
                text: "Wszystkie dostępne towary"
                readonly: True
            TextInput: 
                text: "Wszystkie dostępne towary"
                readonly: True
            TextInput: 
                text: "Wszystkie dostępne towary"
                readonly: True
            
            MDTopAppBar:
                md_bg_color: "#F9AC66"
                title: "Wszystko czego dusza zapragnie "
                MDFloatingActionButton:
                    pos_hint: {"center_x": .5, "center_y": .1}
                    md_bg_color:"#ED6B5B"
                    icon: "account-cash"
                    spacing: "56dp"
                    text: 'Back to menu'
                    on_press:
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'Ustawienia' 
<Jezyki>:
    MDScreen:
    
        MDBoxLayout:
            id:box
            orientation: "vertical"
            md_bg_color: "#C36B84"
            
            MDTopAppBar:
                md_bg_color: "#F9AC66"
                title: "Waluta własna "
                MDFloatingActionButton:
                    pos_hint: {"center_x": .5, "center_y": .1}
                    md_bg_color:"#ED6B5B"
                    icon: "account-cash"
                    spacing: "56dp"
                    text: 'Back to menu'
                    on_press:
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'Ustawienia'
<Ustawienia>:
    name: "Ustawienia"
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Przelicznik walut'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'Kalkulator'
        Button:
            text: 'Custom'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'Custom'
        Button:
            text: 'Aktywa'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'Aktywa'
        Button:
            text: 'Ustawienia języka'
            on_press:
        Button:
            text: 'Aktualizuj dane??'
            on_press:
        
"""


class Kalkulator(Screen):
    
    pass

class Aktywa(Screen):
    pass


class Ustawienia(Screen):
    pass
    

class Custom(Screen):
    pass

class Jezyki(Screen):
    pass

class Jezyk(Screen):
    pass

class Windowmanager(ScreenManager):
    pass



class FloatInput(TextInput):
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




# ANDROID PATH   storage/emulated/0/Download
class MainApp(MDApp):
    def build(self):#budowanie ekranu
        kv = Builder.load_string(KV)
        
        return kv
    kurs=4.5
    waluta2=14
    def sprawdz(self, text):
        self.text = text
        if text == "":
            self.text = "0"
        else:
            self.text = "0"
    def oblicz(self, waluta, waluta2, kurs):
        
        
        self.waluta = waluta
        self.waluta2 = float(waluta2)
        self.kurs = float(kurs)

        waluta = [float(x) for x in waluta]
        waluta=waluta*kurs
    def getwaluta(self):
        return (self.waluta)
    def getwaluta2(self):
        return (self.waluta2)
    def getkurs(self):
        return (self.kurs)
    def setwaluta(self, waluta, kurs):
        self.waluta = waluta
        self.kurs = kurs
    #def callback1(self):
        #to nie działało ale jest w razie w ale juz dziala w .kv
        #self.root.manager.transition.direction = 'right'
        #self.root.manager.current = 'Ustawienia'
        #print("callback1")
    def przeliczaj(self, instance): 
        #tutaj musze pobrac wartosc z pola tekstowego i przeliczyc na walute
        waluta1=self.root.get_screen('Kalkulator').ids.waluta1.float
        waluta2=waluta1*2
        self.root.ids.kalkulator.ids.waluta2.text=waluta2
        print(waluta1)
        print(waluta2)
    def czytaj_waluty():
        with open('waluty.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line)
                #zamiast printowac potrzebuje zeby tworzyly sie linijki w liscie w pliku z5.kv
                #ale nie wiem jak to zrobic
    class FloatInput(TextInput):

        pat = re.compile('[^0-9]')
        def insert_text(self, substring, from_undo=False):
            pat = self.pat
            if '.' in self.text:
                s = re.sub(pat, '', substring)
            else:
                s = '.'.join(
                    re.sub(pat, '', s)
                    for s in substring.split('.', 1)
                )
            return super().insert_text(s, from_undo=from_undo)          


if __name__ == "__main__":
    MainApp().run()
    
    current_path=os.getcwd()