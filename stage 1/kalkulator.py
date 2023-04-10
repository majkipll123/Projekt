import os
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.properties import ObjectProperty, StringProperty




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



# ANDROID PATH   storage/emulated/0/Download
class MainApp(MDApp):
    def build(self):#budowanie ekranu
        kv = Builder.load_file("kalkulator.kv")
        
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
            


if __name__ == "__main__":
    MainApp().run()
    
    current_path=os.getcwd()
