#:kivy !
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from mysql.connector import Error
import mysql.connector
Builder.load_file('kiv_index.kv')

cnx = mysql.connector.connect(user='root', password='12345678',
                              host='127.0.0.1',
                              database='app01')




class MyGrid(Widget):
    pass

class MyApp(App):

    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()



cnx.close()    