# Nice icons:
# human-edit


from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.uix.label import Label
from functools import partial

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from kivy.factory import Factory
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.pickers import MDDatePicker
from random import randint

from kivy.properties import ObjectProperty, StringProperty
from datetime import date
import requests
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


class Przelicznik():
    def __init__(self, name, balance, from_currency, to_currency):
        
        self.name = name
        self.__balance__ = balance
        print(self.__balance__)
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = balance
    def getBalance(self):
        
        return (self.__balance__)

    def setBalance(self, abcd):
        url = "https://api.apilayer.com/exchangerates_data/convert"


        querystring = {"to":"PLN","from":"EUR","amount":str(abcd)}

        headers= {
        "apikey": "xoVqRitppuJgc9tx8Q45wayzXqWuAehN"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        status_code = response.status_code
        result = response.json()
        result2=str(result["result"])
        
        try:   
            self.__balance__ = result2+ " PLN"
        except:
            self.__balance__ = "Error: połączenie niestabilne"

class Kalkulator(Screen):
    acc = ObjectProperty(None)
    balance = StringProperty('')
    
    def __init__(self, **kwargs):
        super(Kalkulator, self).__init__(**kwargs)
        self.acc = Przelicznik("Main", 0,"PLN","USD")
        self.update_balance()
    # Set label positions
        self.ids.lb1.pos_hint = {'center_x': 1, 'center_y': 0.8}
    
        self.ids.lb2.pos_hint = {'center_x': 1, 'center_y': 0.6}

        self.ids.lb3.pos_hint = {'center_x': 1, 'center_y': 0.5}

        self.ids.tp.pos_hint = {'center_x': 0.5, 'center_y': 0.35}

        self.ids.btn1.pos_hint = {'center_x': 0.5, 'center_y': 0.2}


    def update_balance(self):
        self.balance = str(self.acc.getBalance())

class Custom(Screen):
    pass

class Aktywa(Screen):
    url = "https://api.apilayer.com/exchangerates_data/symbols"
    payload = {}
    headers= {
    "apikey": "xoVqRitppuJgc9tx8Q45wayzXqWuAehN"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text
class Ustawienia(Screen):
    pass
class DemoGPBApp(MDApp):
    def build(self, *args):
        Window.size = (1080, 1920)
        self.licz_waluty = 0
        self.licz_waluty_ekran = 0
        sm = ScreenManager()
        sm.add_widget(Kalkulator(name='Kalkulator'))
        sm.add_widget(Custom(name='Custom')) # use Custom here
        sm.add_widget(Aktywa(name='Aktywa'))
        sm.add_widget(Ustawienia(name='Ustawienia'))
        return sm
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # global variables
        self.activeExerciseList = [[], []]
        self.activewalutycreenList = []
        self.date = str(date.today())

        # Flags
        self.flagIsHidenEdit_uix = False
        self.flagEdit_button = True

    def build(self, *args):

        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepOrange"
        Window.size = (480, 800)

        self.liczwaluty = 0
        self.countPopup = 0

        self.liczwalutyScreen = 0

        return Builder.load_file("s15.kv")

    def on_start(self, *args):
        self.liczwaluty = 0
        store = JsonStore("save.json")
        # Load all the waluty
        for item in store.find(name="Waluty"):
            self.add_new_widget((item[1]).get("text"), mode="load")
            self.liczwaluty += 1

        if(self.liczwaluty == 0):
            self.add_new_widget("Deafult", mode="add")
        self.liczwalutyScreen = 0        
        store = JsonStore("waluty.json")
        # Load all the waluty
        for item in store.find(name="Waluty"):
            self.liczwalutyScreen += 1

        # On start hide the edit section
        partial(
            self.hide_me,
            [self.root.ids.exercise_name_input, self.root.ids.addExercise_button],
        )()

       

        self.sort_waluty("AZ_asc")

    def visibility_handler(self, widgets, *args):
        if self.flagIsHidenEdit_uix:
            self.hide_me(widgets)
        else:
            self.show_me(widgets)

        self.flagIsHidenEdit_uix = not self.flagIsHidenEdit_uix

    def hide_me(self, widgets, *args):
        if type(widgets) != list:
            widgets = [widgets]
        for widget in widgets:
            widget.opacity = 0
            widget.disabled = True

    def show_me(self, widgets, *args):
        if type(widgets) != list:
            widgets = [widgets]
        for widget in widgets:
            widget.opacity = 1
            widget.disabled = False

    def sort_waluty(self, mode, *args):

        self.activeExerciseList[1] = list()
        for exercise in self.activeExerciseList[0]:
            self.activeExerciseList[1].append(exercise.children[1].text.lower())

        tupleResult = list(zip(self.activeExerciseList[0], self.activeExerciseList[1]))

        if mode == "AZ_asc":
            activewalutyortTempList = sorted(tupleResult, key=lambda x: x[1])
        elif mode == "AZ_des":
            activewalutyortTempList = sorted(
                tupleResult, key=lambda x: x[1], reverse=True
            )


        self.activeExerciseList = list(zip(*activewalutyortTempList))
        self.activeExerciseList[0] = list(self.activeExerciseList[0])
        self.reload_waluty()


    def reload_waluty(self, *args):
        self.root.ids.exercise_box.clear_widgets()
        for exercise in self.activeExerciseList[0]:
            self.root.ids.exercise_box.add_widget(exercise)

    def add_new_widget(self, text, mode="add", *args):

        if text == "" or text in self.activeExerciseList[1] or len(text) > 20:
            return

        store = JsonStore("save.json")
        vp_height = self.root.ids.exercise_scroll.viewport_size[1]
        sv_height = self.root.ids.exercise_scroll.height

        # add a new widget (must have preset height)
        boxlayout = MDBoxLayout(
            orientation="horizontal", size_hint=(1, None), height=50
        )
        boxlayout.add_widget(
            MDLabel(
                text=text,
                size_hint=(1, None),
                height=50,
                valign="center",
                halign="center",
            )
        )
        removeAndInfo_button = MDIconButton(
            icon="information-outline",
            theme_icon_color="Custom",
            icon_color=self.theme_cls.primary_color,
            size_hint=(0.25, None),
            height=50,
        )
        boxlayout.add_widget(removeAndInfo_button)

        self.activeExerciseList[0].append(boxlayout)


        self.root.ids.exercise_box.add_widget(boxlayout)

        if mode != "load":
            store.put(name="Waluty", text=text, key=self.liczwaluty)
            self.liczwaluty += 1

        # On adding new element, show remove button

        if mode != "load":
            for widget in self.activeExerciseList[0]:
                widget.children[0].icon = "delete"
                widget.children[0].on_release = partial(self.remove_widget, widget)

        if vp_height > sv_height:  # otherwise there is no scrolling
            # calculate y value of bottom of scrollview in the viewport
            scroll = self.root.ids.exercise_scroll.scroll_y
            bottom = scroll * (vp_height - sv_height)

            # use Clock.schedule_once because we need updated viewport height
            # this assumes that new widgets are added at the bottom
            # so the current bottom must increase by the widget height to maintain position
            Clock.schedule_once(partial(self.adjust_scroll, bottom), -1)

    def adjust_scroll(self, bottom, *args):
        vp_height = self.root.ids.exercise_scroll.viewport_size[1]
        sv_height = self.root.ids.exercise_scroll.height
        self.root.ids.exercise_scroll.scroll_y = bottom / (vp_height - sv_height)

    def remove_widget(self, widgetsToRemove, *args):

        store = JsonStore("save.json")
        if type(widgetsToRemove) != list:
            widgetsToRemove = [widgetsToRemove]

        for widgetToRemove in widgetsToRemove:
            try:
                self.root.ids.exercise_box.remove_widget(widgetToRemove)
                self.liczwaluty -= 1
                for item in store.find(text=widgetToRemove.children[1].text):
                    store.delete(item[0])
                self.activeExerciseList[0].remove(widgetToRemove)
                self.activeExerciseList[1].remove(widgetToRemove.children[1].text)
            except:
                pass







    def add_new_widget_aktywa_screen(
        self, title, reps, sets, dirty,idOfEx, date="" , mode="add", *args
    ):
        if(reps == "" or sets == "" or dirty == ""):
            return
        
        store = JsonStore("waluty.json")
        vp_height = self.root.ids.aktywa_screen_scroll.viewport_size[1]
        sv_height = self.root.ids.aktywa_screen_scroll.height

        gridlayout = MDGridLayout(
            cols=5, rows=1, size_hint=(1, None), height=50, _md_bg_color="#2f2f2f", id=idOfEx
        )
        if(mode == "add"):
            gridlayout.add_widget(
                MDLabel(
                    text=str(self.date),
                    size_hint=(1, None),
                    height=50,
                    valign="center",
                    halign="center",
                )
            )
        else:
            gridlayout.add_widget(
                MDLabel(
                    text=str(date),
                    size_hint=(1, None),
                    height=50,
                    valign="center",
                    halign="center",
                )
            )
        gridlayout.add_widget(
            MDLabel(
                text="Reps: " + str(reps),
                size_hint=(1, None),
                height=50,
                valign="center",
                halign="center",
            )
        )
        gridlayout.add_widget(
            MDLabel(
                text="Sets: " + str(sets),
                size_hint=(1, None),
                height=50,
                valign="center",
                halign="center",
            )
        )
        if dirty:
            gridlayout.add_widget(
                MDLabel(
                    text="Dirty",
                    size_hint=(1, None),
                    height=50,
                    valign="center",
                    halign="center",
                )
            )
        else:
            gridlayout.add_widget(
                MDLabel(
                    text="Clean",
                    size_hint=(1, None),
                    height=50,
                    valign="center",
                    halign="center",
                )
            )
        gridlayout.add_widget(
            MDIconButton(
                icon="delete",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                on_release=partial(self.remove_exercise, gridlayout),
            )
        )

        # self.activewalutycreenList[0].append(boxLayaout)
        self.activewalutycreenList.append(gridlayout)

        self.root.ids.aktywa_screen_box.add_widget(gridlayout)

        if mode != "load":
            store.put(
                name="Waluty",
                reps=reps,
                sets=sets,
                dirty=dirty,
                title=title,
                date = self.date,
                key=self.liczwalutyScreen,
                id=randint(1000, 10000000),
            )
            self.liczwalutyScreen += 1

        if vp_height > sv_height:
            scroll = self.root.ids.aktywa_screen_scroll.scroll_y
            bottom = scroll * (vp_height - sv_height)

            Clock.schedule_once(partial(self.adjust_scroll_screen, bottom), -1)

    def adjust_scroll_screen(self, bottom, *args):
        vp_height = self.root.ids.aktywa_screen_scroll.viewport_size[1]
        sv_height = self.root.ids.aktywa_screen_scroll.height
        self.root.ids.aktywa_screen_scroll.scroll_y = bottom / (vp_height - sv_height)

    def load_waluty_screen(self, *args):
        store = JsonStore("waluty.json")
        # Load all the waluty
        for item in store.find(name="Waluty"):
            self.add_new_widget_aktywa_screen((item[1]).get("text"), mode="load")
            self.liczwalutyScreen += 1

    def edit_button_handler_aktywa_screen(self, *args):
        # On start hide the edit section
        if self.flagEdit_button:

            for widget in self.activeExerciseList[0]:
                # Change to delete button
                widget.children[0].icon = "delete"
                widget.children[0].on_release = partial(self.remove_widget, widget)

            self.root.ids.edit_button.icon = "check-circle-outline"

        else:

            for widget in self.activeExerciseList[0]:
                # Change to delete button
                widget.children[0].icon = "information-outline"
                widget.children[0].on_release = partial(
                    partial(
                        self.screen_change,
                        "walutycreen",
                        widget.children[1].text,
                        "right",
                    ),
                    partial(self.load_waluty_screen, widget.children[1].text),
                )

            self.root.ids.edit_button.icon = "circle-edit-outline"

        self.flagEdit_button = not self.flagEdit_button

    def remove_exercise(self, widgetsToRemove, *args):

            print("remove_exercise")
            store = JsonStore("waluty.json")
            if type(widgetsToRemove) != list:
                widgetsToRemove = [widgetsToRemove]

            for widgetToRemove in widgetsToRemove:
                try:
                    self.root.ids.aktywa_screen_box.remove_widget(widgetToRemove)
                    self.liczwalutyScreen -= 1
                    print(widgetToRemove.id)
                    for item in store.find(id=int(widgetToRemove.id)):
                        print(item)
                        store.delete(item[0])
                    self.activeExerciseList[0].remove(widgetToRemove)
                    self.activeExerciseList[1].remove(widgetToRemove.children[1].text)
                except:
                    pass

    def on_save(self, instance, value, date_range):
            '''
            Events called when the "OK" dialog box button is clicked.

            :type instance: <kivymd.uix.picker.MDDatePicker object>;

            :param value: selected date;
            :type value: <class 'datetime.date'>;

            :param date_range: list of 'datetime.date' objects in the selected range;
            :type date_range: <class 'list'>;
            '''
            print(instance, value, date_range)
            self.date = str(value)
    
    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


if __name__ == "__main__":
    DemoGPBApp().run()