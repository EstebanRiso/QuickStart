#:kivy !
from sys import api_version
from kivy.animation import Animation
from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from psycopg2 import connect
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.icon_definitions import md_icons
from kivy.uix.screenmanager import ScreenManager, Screen
import backend.connect

Window.size =(305,480)

#Builder.load_file('images.kv')

KV = """
MDScreen:
    name: "LoginQuickStart"
    on_enter:
        app.anim(back)
        app.anim1(back1)
    MDFloatLayout:
        MDFloatLayout:
                id: back
                size_hint_y; .6
                pos_hint: {"center_y": 1.8}
                radius: [0, 0, 0, 40]
                canvas:
                    Color:
                        rgb: (1,0,0,1)
                    Rectangle:
                        size: self.size
                        pos: self.pos
        MDFloatLayout:
                id: back1
                size_hint_y; .6
                pos_hint: {"center_y": 1.8}
                radius: [0, 0, 0, 40]
                canvas:
                    Color:
                        rgb: (1,0,0,1)
                    Ellipse:
                        size: self.size
                        pos: self.pos
"""





class MainApp(MDApp):


    def change_screen (self,name):
      screen_manager.current=  name


    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_string(KV))
        return screen_manager

    def anim(self,widget):
        anim= Animation(pos_hint={"center_y": 1.16})
        anim.start(widget)

    def anim1(self,widget):
        anim= Animation(pos_hint={"center_y": .85})
        anim.start(widget)

    #def on_start(self):
      #  self.fps_monitor_start()



if __name__ == "__main__":
 app = MainApp()
app.run()