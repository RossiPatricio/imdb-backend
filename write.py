from imdb_search import *
from scraping_imdb import *

def asd(user_input):
        try:
            result = scrap_imdb(get_url(user_input))
            print(result['title'], result['director'])
            team = ''
            for name in result['team']:
                team += f'{name} '
            print(team)
            print(result['synopsis'])
            print(result['poster'])
        except Exception as e:
            print(e)

lista_de_diccionarios = []

with open('peliculas.txt', 'r') as archivo:
    for linea in archivo:
        linea = linea.strip()
        print(f'Searching for: {linea}')
        try:
            result = scrap_imdb(get_url(linea))
            print(f'Adding {result['title']}')
            lista_de_diccionarios.append(result)
        except Exception as e:
            print(e)
            
with open('output.txt', 'w', encoding="utf-8") as file_object:
    for dic in lista_de_diccionarios:
        # Extraer el título y el año del campo title
        title_full = dic["title"]
        # Suponiendo que el título tiene el formato "TÍTULO (AÑO)"
        if '(' in title_full and ')' in title_full:
            title = title_full[:title_full.rfind('(')].strip()
            year = title_full[title_full.rfind('(')+1:title_full.rfind(')')].strip()
        else:
            title = title_full
            year = "N/A"  # En caso de que no haya año

        # Formatear la línea según el formato deseado
        s = f'{title}\t {year}\t {dic["director"]}\t {dic["synopsis"]}\t {dic["team"]}\t {dic["poster"]}\n'
        file_object.writelines(s)