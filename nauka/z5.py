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


class Jezyk(Screen):
    pass

class Windowmanager(ScreenManager):
    pass




class MainApp(MDApp):
    def build(self):
        kv = Builder.load_file("z5.kv")
        
        return kv
    def callback1(self):
        #to nie działa ale jest w razie w ale juz dziala w .kv
        #self.root.manager.transition.direction = 'right'
        #self.root.manager.current = 'Ustawienia'
        print("callback1")

if __name__ == "__main__":
    MainApp().run()