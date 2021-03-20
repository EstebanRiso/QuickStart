#:kivy !
screen_manager= None

from logging import root
from sys import api_version
from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from psycopg2 import connect
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.icon_definitions import md_icons
from kivy.uix.screenmanager import ScreenManager, Screen
from backend.connect import BDD # en el caso tuyo solo es necesario que este from backend.connect import BDD
Window.size =(305,480)




class MainApp(MDApp):




    def change_screen (self,name):
      screen_manager.current=  name


    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        self.title="QuickStart"
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


    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        Clock.schedule_once(self.UserData)

    
    def UserData(self, *args ,**kwargs):
        #global correoScr, passScr 
        correoData =self.root.ids.correo.text
        passData = self.root.ids.password.text
        print(correoData, passData)
       # listaData = [correoData,passData]    
        #return listaData

       
 



    




#llamada base de datos
BaseDD= BDD()
conexionBDD = BaseDD.conectar()

#llamada funciones del main
Main= MainApp()
#data = Main.UserData()
#print(data)


if __name__ == "__main__":
 app = MainApp()
 app.run()                        