from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from parse_all import final_parse


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.label = TextInput(text='!!!', multiline = True)
        #self.final_parse_text = final_parse()
    def btn_pressed(self, *args):
        self.label.text = final_parse()
    def build(self):
        box = BoxLayout(orientation = 'vertical')
        parse_button = Button(text='PARSE',pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint = (0.3,0.1))
        parse_button.bind(on_press=self.btn_pressed)
        box.add_widget(self.label)
        box.add_widget(parse_button)
        return box
MyApp().run()
