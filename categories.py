import page
from bs4 import BeautifulSoup


def get_all_categories(url):

    soup = page.parse_main_page(url)

    categories = []

    all_categories = soup.find('div', class_='side_categories').find('ul', class_='nav nav-list').find('ul').find_all('li')

    for li in all_categories:
        url_cat = []
        url_cat.append(li.find('a').text.strip())
        url_cat.append(url + li.find('a').attrs['href'])
        categories.append(url_cat)
    
    return categories
        
    

#get_all_categories("https://books.toscrape.com/")
    
    
    
    
    
    




#def get_book_by_categorie():
    # pour chaque livre dans catégorie stocker les urls des livres
