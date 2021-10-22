import requests
from bs4 import BeautifulSoup
import book


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

    all_books = []
    
    while url:

        books_page = requests.get(url)
        soup_page = BeautifulSoup(books_page.content, "html.parser")
        

        books_li = soup_page.find('div', class_='col-sm-8 col-md-9').find('ol', class_='row').find_all('li')
        for li in books_li:
            book_url = requests.compat.urljoin(url, li.find('h3').find('a').attrs['href'])
            all_books.append(book.get_book(book_url))
    
        li_next = soup_page.find('li', class_='next')

        if li_next:
            url = requests.compat.urljoin(url, li_next.find('a').attrs['href'])
        else:
            break
    
    return all_books
