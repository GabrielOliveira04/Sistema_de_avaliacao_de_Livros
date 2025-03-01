import requests

def get_livros():
    response = requests.get('http://127.0.0.1:8000/api/livros')
    return response.json()

