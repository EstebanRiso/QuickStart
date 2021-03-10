import psycopg2 
import importlib

#coneccion a la base de datos





class BDD():

    def __init__(self):
        self.con=None
        self.cur=None

    def conectar(self):
        self.con=psycopg2.connect(  
                host="localhost",
                database="postgres",
                user="postgres",
                password="importante")

    def generarcursor(self):
        self.cur=self.con.cursor
        

    def insertar(self,grupo,columnas,valores):
        
        concatenacion_01="".join(columnas)
        concatenacion_02="".join(valores)
        syntaxis="insert into "+grupo+" "+concatenacion_01+" values "+concatenacion_02

        self.cur.execute(syntaxis)
        self.con.commit()

         
    def seleccionarTodos(self,grupo):

        syntaxis="select * from "+grupo

        self.cur.execute(syntaxis)
        rows=self.cur.fetchall()
        return rows

    def seleccionar(self,grupo,columnas):

        syntaxis="select ("+columnas+") from "+grupo

        self.cur.execute(syntaxis)
        rows=self.cur.fetchall()
        return rows



    def desconectar(self):
        self.con.close()

