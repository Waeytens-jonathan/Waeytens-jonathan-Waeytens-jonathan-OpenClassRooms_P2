import requests
from bs4 import BeautifulSoup

base_url = "https://books.toscrape.com/"

def get_book(url):

    infos = {}

    infos["product_url"] = url
    book_page = requests.get(url)
    if book_page.ok:
        book_soup = BeautifulSoup(book_page.content, 'html.parser')
        # [6:] permet de supprimer les caractères en trop présent dans l'URL de l'image, la valeur vaut le nombre de caractères
        infos["title"] = book_soup.find('div', class_="col-sm-6 product_main").find('h1').text
        infos["image"] = base_url + book_soup.find('div', class_='item active').find('img').attrs["src"][6:]
        infos["rating"] = book_soup.find('p', class_='star-rating').attrs["class"][1]
        table = book_soup.find('table', class_='table table-striped').find_all('tr')
        for tr in table:
            th_text = tr.find('th').text
            if th_text == "UPC":
                infos["UPC"] = tr.find('td').text
            elif th_text == "Price (incl. tax)":
                infos["price_including_tax"] = tr.find('td').text
            elif th_text == "Price (excl. tax)":
                infos["price_excluding_tax"] = tr.find('td').text
            elif th_text == "Availability":
                infos["number_available"] = tr.find('td').text
        infos["category"] = book_soup.find('ul', class_='breadcrumb').find_all('li')[2].find('a').text
        infos["product_description"] = book_soup.find_all('p')[3].text


    return infos


""" def pagination():

Change de page une fois tous les livres d'une catégorie extrait."""