  
from typing import Text
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDTextButton
from kivymd.uix.screen import Screen
from kivy.core.window import Window
#Window.size =(305,480)


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        text = MDTextButton(text='Ingresar como Usuario', pos_hint={'center_x': 0.3, 'center_y': 0.4})
        btn = MDFloatingActionButton(icon="account-circle",
                                     pos_hint={'center_x': 0.3, 'center_y': 0.5},
                                     )
        
        text2 = MDTextButton(text='Ingresar como Especialista', pos_hint={'center_x': 0.65, 'center_y': 0.4})
        btn2 = MDFloatingActionButton(icon="face",
                                     pos_hint={'center_x': 0.65, 'center_y': 0.5},
                                     )



        screen.add_widget(btn)
        screen.add_widget(text)
        screen.add_widget(btn2)
        screen.add_widget(text2)
        return screen


DemoApp().run()