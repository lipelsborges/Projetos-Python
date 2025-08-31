import requests

def buscar(tipo, nome):

    if tipo == "artist":
        url = f"https://api.deezer.com/search/artist?q={nome}"  
    elif tipo == "album":
        url = f"https://api.deezer.com/search/album?q={nome}"
    else:
        url = f"https://api.deezer.com/search?q={nome}"
    
    res = requests.get(url)
    dados = res.json()

    if "data" not in dados or len(dados["data"]) == 0:
        print("Nenhum resultado encontrado.")
    return


aaaa