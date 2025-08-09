from imdb_search import *
from scraping_imdb import *

def imdb(input):
    return scrap_imdb(get_url(input))

while True:
    user_input = input('Search:')
    if user_input == 'q':
        break
    else:
        try:
            result = imdb(user_input)
            print(result['title'], result['director'])
            team = ''
            for name in result['team']:
                team += f'{name} '
            print(team)
            print(result['synopsis'])
            print(result['poster'])
            print()
        except Exception as e:
            print(e)

#deberia if name = main ?