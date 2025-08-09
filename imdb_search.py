import requests
import urllib.parse

def imdb_search(titulo):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    query = urllib.parse.quote_plus(titulo)
    url = f"https://v2.sg.media-imdb.com/suggestion/{query[0]}/{query}.json"
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None

    data = response.json()
    # Busca el primer resultado que sea de tipo 'movie'
    for item in data.get("d", []):
        if item.get("qid") in ("movie"):
            return f"https://www.imdb.com/title/{item['id']}/"

    return None

def get_url(search):
    return imdb_search(search)
