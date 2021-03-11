#:kivy !
screen_manager= None

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
from QuickStart.backend.connect import BDD # en el caso tuyo solo es necesario que este from backend.connect import BDD

Window.size =(305,480)






class MainApp(MDApp):


    def change_screen (self,name):
      screen_manager.current=  name


    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        #print(Builder.load_file('images.kv'))

        screen_manager.add_widget(Builder.load_file('login.kv'))
        return screen_manager

    def anim(self,widget):
        anim= Animation(pos_hint={"center_y": 1.16})
        anim.start(widget)

    def anim1(self,widget):
        anim= Animation(pos_hint={"center_y": .85})
        anim.start(widget)

    def icons(self,widget):
        anim= Animation(pos_hint={"center_y": .8})
        anim += Animation(pos_hint={"center_y": .85})
        anim.start(widget)

    def text(self,widget):
        anim= Animation(opacity=0, duration=2)
        anim += Animation(opacity=1)
        anim.start(widget)

    #def on_start(self):
      #  self.fps_monitor_start()



if __name__ == "__main__":
 app = MainApp()
 app.run()