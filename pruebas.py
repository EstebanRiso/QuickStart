import psycopg2 
from QuickStart.backend.connect import BDD 




DB=BDD()
DB.conectar()
DB.generarcursor()
datos=DB.seleccionarTodos("usuario")    

for r in datos:
    print(f"id {r[0]} correo_electronico {r[1]} contraseña {r[2]} ")


