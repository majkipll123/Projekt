import os
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp





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
        kv = Builder.load_file("z5stage1.kv")

        return kv
    #def callback1(self):
        #to nie działało ale jest w razie w ale juz dziala w .kv
        #self.root.manager.transition.direction = 'right'
        #self.root.manager.current = 'Ustawienia'
        #print("callback1")
    
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
