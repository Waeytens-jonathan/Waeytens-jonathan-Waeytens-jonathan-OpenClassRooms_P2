import requests
from bs4 import BeautifulSoup





def parse_main_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    return(soup)

