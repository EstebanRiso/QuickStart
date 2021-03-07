import psycopg2 

#coneccion a la base de datos

con = psycopg2.connect(

    host="localhost",
    database="postgres",
    user="postgres",
    password="importante")

#cursor
cur=con.cursor()

for i in range(2):
    cur.execute("insert into Usuario (id_usuario")

cur.execute("select * from Usuario")

rows=cur.fetchall()

for r in rows:
    print(f"id {r[0]} correo electronico {r[1]} contraseña {r[2]}")

cur.close()

# cerrar la base da datos
con.close()