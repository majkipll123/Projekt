from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput 

class MainApp(App):
    def build(self):
        self. icon="miniaturka.png"
        self.operators = ["/","*","+","-"]
        self.last_was_operator= None
        self.last_button = None

        main_layout = BoxLayout(orientation = "vertical")
        #add another layout to the main layout
        #layout bedzie wysuwał sie z boku onka po kliknięciu na przycisk
        self.solution = TextInput(multiline = False, readonly = True, halign = "right", font_size = 55)    

        main_layout.add_widget(self.solution)
        buttons = [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            [".","0","C","+"]
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(   
                    text = label, font_size = 32, background_color = "black", pos_hint = {"center_x":0.5, "center_y":0.5}
                    )
                button.bind(on_press = self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        equal_buton = Button(text = "=", font_size = 32, background_color = "black", pos_hint = {"center_x":0.5, "center_y":0.5})
        equal_buton.bind(on_press = self.on_solution)
        main_layout.add_widget(equal_buton)
        return main_layout
    
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution
    def build(self):

        btn = Button(text = "$$$",
                     size_hint = (0.1, 0.1),
                     pos_hint = {"center_x":0.5, "center_y":0.5},
                     background_color = (0,0,0,0),
                     background_normal = "")
        return btn    
    root = Button()

if __name__ == "__main__":
    
    app = MainApp()
    app.run()