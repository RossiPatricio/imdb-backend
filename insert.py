import psycopg2
from imdb_search import *
from scraping_imdb import *

conn = psycopg2.connect(
    database="peliculas_imdb",
    user="postgres",
    password="010001101000",
    host="localhost",
    port="5432"
)

def insertar_pelicula(conn, title, director, synopsis, team,poster):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO peliculas (title, director, synopsis, team, poster) VALUES (%s, %s, %s, %s, %s)",
            (title, director, synopsis, team,poster)
        )
        conn.commit()

with open('peliculas.txt', 'r') as archivo:
    for linea in archivo:
        linea = linea.strip()
        print(f'Searching for: {linea}')
        resultado = scrap_imdb(get_url(linea))
        print(f'Adding :{resultado["title"]}')
        
        if resultado:
            title = resultado['title']
            director = resultado['director']
            synopsis = resultado['synopsis']
            team = resultado['team']
            poster = resultado['poster']
            insertar_pelicula(conn, title, director, synopsis, team, poster)

conn.close()
