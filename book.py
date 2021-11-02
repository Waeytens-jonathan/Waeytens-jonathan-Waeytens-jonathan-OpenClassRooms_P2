import requests
from bs4 import BeautifulSoup


def get_book(url):
    '''Get all infos for one book'''

    infos = {}

    infos["product_url"] = url
    book_page = requests.get(url)
    if book_page.ok:
        book_soup = BeautifulSoup(book_page.content, 'html.parser')
        # [6:] permet de supprimer les caractères en trop présent dans l'URL de l'image, la valeur vaut le nombre de caractères
        infos["title"] = book_soup.find('div', class_="col-sm-6 product_main").find('h1').text
        infos["image"] = requests.compat.urljoin(url, book_soup.find('div', class_='item active').find('img').attrs["src"])
        infos["rating"] = numbers_str_to_int(book_soup.find('p', class_='star-rating').attrs["class"][1])
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
                available = tr.find('td').text.strip()
                infos["number_available"] = int(available[10:-11])
        infos["category"] = book_soup.find('ul', class_='breadcrumb').find_all('li')[2].find('a').text
        infos["product_description"] = book_soup.find_all('p')[3].text


        download_image(infos["UPC"],infos["image"])
    else:
        print("Error get book")

    return infos

def numbers_str_to_int(rating):
    '''convert string to int'''

    rating_change = {'One': 1,'Two': 2,'Three': 3, 'Four': 4, 'Five': 5}

    return rating_change[rating]


def download_image(upc, image):
    '''Get all images'''

    image_requests = requests.get(image)

    if image_requests.ok:

        upc += '.jpg'

        with open('images/' + upc, 'wb') as files:
            files.write(image_requests.content)
    else:
        print("Download image is impossible")