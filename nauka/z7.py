import re
from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

KV = """
BoxLayout:
    orientation: 'vertical'
    FloatInput:
        id: float_input
"""

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


class MainApp(MDApp):
    def build(self):
        kv = Builder.load_string(KV)
        return kv


if __name__ == "__main__":
    MainApp().run()
