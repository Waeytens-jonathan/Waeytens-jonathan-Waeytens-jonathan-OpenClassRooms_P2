import requests
from bs4 import BeautifulSoup


def get_all_categories(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    categories = []

    all_categories = soup.find('div', class_='side_categories').find('ul', class_='nav nav-list').find('ul').find_all('li')

    for li in all_categories:
        url_cat = []
        url_cat.append(li.find('a').text.strip())
        url_cat.append(requests.compat.urljoin(url, li.find('a').attrs['href']))
        categories.append(url_cat)
    
    return categories

def get_books_from_categorie(url):
    pass