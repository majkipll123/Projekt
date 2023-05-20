from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
Builder.load_file("z12.kv")

class MyLayot(Widget):
        def spinner_clicked(self, value):
            self.ids.click_label.text = f'you selected {value}'

class MainApp(App):
    def build(self):
        return MyLayot()
    
if __name__ == "__main__":
    MainApp().run()