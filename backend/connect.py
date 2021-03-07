import psycopg2 

#coneccion a la base de datos

def connection() :

    con = psycopg2.connect(

        host="localhost",
        database="postgres",
        user="postgres",
        password="importante")

    #cursor
    #cur=con.cursor()

    #ur.execute("select * from Usuario")

#rows=cur.fetchall()

#for r in rows:
 #   print(f"id {r[0]} correo electronico {r[1]} contraseña {r[2]}")



# cerrar la base da datos
    #con.close()

    return con


def insertUser(self):
    if  self.connection() :
        print("conexion exitosa equisde")

    else :
        print("gg wp no funciono")
