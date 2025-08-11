import requests
import urllib.parse

def imdb_search(titulo, timeout=5):
    # Normalizar el título antes de codificar
    titulo_norm = titulo.strip().lower()
    if not titulo_norm:
        return None

    query = urllib.parse.quote_plus(titulo_norm)
    first_char = query[0]  # ya es minúscula por título_norm
    url = f"https://v2.sg.media-imdb.com/suggestion/{first_char}/{query}.json"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        resp = requests.get(url, headers=headers, timeout=timeout)
        if resp.status_code != 200:
            return None
        data = resp.json()
    except Exception:
        return None

    items = data.get("d", [])
    first_movie_candidate = None

    # Buscar coincidencia exacta (o parcial) en el título devuelto; si no, devolver el primer "movie"
    for item in items:
        qid = item.get("qid")  # en la API de sugerencias IMDB suele aparecer 'movie', 'tvSeries', 'video', etc.
        title_field = item.get("l", "")  # 'l' contiene el título en la mayoría de respuestas
        if qid == "movie":
            # si el título buscado está dentro del título del resultado, devolverlo
            if titulo_norm in title_field.lower():
                return f"https://www.imdb.com/title/{item['id']}/"
            if first_movie_candidate is None:
                first_movie_candidate = item

    if first_movie_candidate:
        return f"https://www.imdb.com/title/{first_movie_candidate['id']}/"

    return None

def get_url(search):
    return imdb_search(search)
