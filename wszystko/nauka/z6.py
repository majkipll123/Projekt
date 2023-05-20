import os
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

from kivymd.toast import toast
KV="""
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
            orientation: "horizontal"
            
            MDTextField:
                id: gang
                pos_hint: {"center_x": .5, "center_y": .5}
                multiline: False
                mode: "rectangle"
                hint_text: "Enter amount"
                helper_text: "Enter amount"
                helper_text_mode: "on_focus"
                icon_left: "cash"
                icon_left_color: app.theme_cls.primary_color
                hint_text: "Euro"
                
                height: "10dp"

                
                

            MDTextField:

                pos_hint: {"center_x": .5, "center_y": .5}
                multiline: False
                mode: "rectangle"
                hint_text: "Enter amount"
                helper_text: "Enter amount"
                helper_text_mode: "on_focus"
                icon_left: "cash"
                icon_left_color: app.theme_cls.primary_color
                hint_text: "Złoty"
                
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
    
class Custom(Screen):
    pass

class Jezyk(Screen):
    pass

class Windowmanager(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.file_manager_open = False
        kv = Builder.load_string(KV)

        return kv

    def callback1(self):
        #to nie działa ale jest w razie w ale juz dziala w .kv
        #self.root.manager.transition.direction = 'right'
        #self.root.manager.current = 'Ustawienia'
        print("callback1")

    def file_manager_open(self):
        if not self.file_manager_open:
            self.file_manager_open = True
            self.manager_open = True
            self.file_manager.show('/')

    def select_path(self, path, data):
        self.current_path = path  # <-- update the current path
        self.exit_manager()
        self.exit_manager()

        # check if selected path is a file
        if os.path.isfile(path):
            with open(path, 'w') as f:
                f.write(data)
                toast('File created and written to: ' + path)
        elif os.path.isdir(path):
            file_path = os.path.join(path, "example.txt")
            f.write(data)
            toast("file created adn written to:"  + file_path)
        else:
            toast('Invalid selection: ' + path)

if __name__ == "__main__":
    MainApp().run()
                  

