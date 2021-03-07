#:kivy !
from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from psycopg2 import connect

import backend.connect


Builder.load_file('images.kv')



class MyGrid(Widget):
    
      connect.connection()
      

    

class MyApp(App):

    def build(self):

        self._app_name="QuickStart"  
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()



