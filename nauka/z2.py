from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.lang import Builder

KV = '''
MDBoxLayout:
    orientation: "vertical"
    md_bg_color: "#1E1E15"

    MDTopAppBar:
        title: "Express Currency "
        left_action_items: [["menu", lambda x: app.callback()]]
        right_action_items: [["dots-vertical", lambda x: app.callback1()]]

        

    MDLabel:
        text: "Content"
        halign: "center"
'''

class ConverterApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)
        
       # screen.add_widget(self.textfield)?
    def callback(self):
        print("działa! ")
    def callback1(self):
        print("działa! jeszcze lepiej ")

if __name__ == '__main__':
    ConverterApp().run()