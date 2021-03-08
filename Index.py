#:kivy !
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from Backend.connect import BDD 
Builder.load_file('kiv_index.kv')



BDD=BDD()

BDD.conectar()
BDD.desconectar()

class MyGrid(Widget):
    pass

class MyApp(App):

    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()



  