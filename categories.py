import page




#url = page.parse_main_page()

def get_all_categories(url):

    soup = page.parse_main_page(url)

    categories = {}

    all_categories = soup.find('div', class_='side_categories').find_all('li').text

    '''for categorie in all_categories:
        
        categories + all_categories'''

        

    print(all_categories)

get_all_categories("https://books.toscrape.com/")
    
    
    
    
    
    
    # Récupère toute les url des catégories des livres



#def get_book_by_categorie():
    # pour chaque livre dans catégorie stocker les urls des livres
