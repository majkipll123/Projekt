
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.list import OneLineListItem

KV = '''
MDScreen:
    
    MDBoxLayout:
        id:box
        orientation: "vertical"
        md_bg_color: "#1E1E15"

        MDTopAppBar:

            title: "Express Currency "
            left_action_items: [["menu", lambda x: app.callback1()]]
            right_action_items: [["dots-vertical", lambda x: app.callback1()]]
            

    MDBoxLayout:
        orientation: "horizontal"
        MDTextField:

            pos_hint: {"center_x": .5, "center_y": .5}
            multiline: False
            mode: "rectangle"
            hint_text: "Enter amount"
            helper_text: "Enter amount"
            helper_text_mode: "on_focus"
            icon_right: "cash"
            icon_right_color: app.theme_cls.primary_color
            hint_text: "Euro"
            required: True
            helper_text_mode: "on_error"
            helper_text: "Wprowadź walutę"
            height: "10dp"

        MDTextField:
            text: "Wprowadź walutę"
            color_mode: "accent"

        MDTextField:

            pos_hint: {"center_x": .5, "center_y": .5}
            multiline: False
            mode: "rectangle"
            hint_text: "Enter amount"
            helper_text: "Enter amount"
            helper_text_mode: "on_focus"
            icon_right: "cash"
            icon_right_color: app.theme_cls.primary_color
            hint_text: "Złoty"
            required: True
            helper_text_mode: "on_error"
            helper_text: "Wprowadź walutę"
            height: "10dp"
        


'''

class ConverterApp(MDApp):
    
    def build(self):
        screen=Builder.load_string(KV)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        self.user = TextInput(
            multiline=False,
            padding_y=(20,20),
            size_hint=(1,0.5),
            )
        #for name_theme in [
        #    "Primary",
        #    "Secondary",
        #    "Hint",
        #    "Error",
        #]:
        #    screen.ids.box.add_widget(
        #        MDLabel(
        #            text=name_theme,
         #           halign="center",
        #            theme_text_color=name_theme,
         #           
         #       )
         #   )
        def on_start(self):
            for i in range(20):
                self.root.ids.container.add_widget(
                OneLineListItem(text=f"Single-line item {i}")
            )
        return screen
        
       # screen.add_widget(self.textfield)?
    def on_touch_down(self, touch):
         if self.collide_point(*touch.pos):
             self.pressed = touch.pos
             return True
         return super(ConverterApp, self).on_touch_down(touch)
    def touch(sefl):
        print("działa")
    
    

if __name__ == '__main__':
    ConverterApp().run()