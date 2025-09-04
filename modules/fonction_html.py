from bs4 import BeautifulSoup
import requests

def extract_into_file(adresse,fichier):
    
    url = adresse
    page=requests.get(url)

    with open(fichier,'w', encoding="utf-8") as file:
        file.write(page.text)

a = 77