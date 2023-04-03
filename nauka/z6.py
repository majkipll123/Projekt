import os
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

from kivymd.toast import toast

class Kalkulator(Screen):
    pass

class Aktywa(Screen):
    pass
    KV="""
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
class Ustawienia(Screen):
    pass
    def on_press_button(self):
        # get the file chooser
        file_chooser = self.ids.file_chooser

        # get the selected path
        path = file_chooser.path

        # create and write a file to the selected path
        self.parent.select_path(path, "Hello, world!")
"""
class Custom(Screen):
    pass

class Jezyk(Screen):
    pass

class Windowmanager(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.file_manager_open = False
        kv = Builder.load_file("z5.kv")

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
                  

