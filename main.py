import categories
import book


if __name__=="__main__":

   url = "https://books.toscrape.com/" 

   books_categories = categories.get_all_categories(url)
   
   books = []
   """for cat in books_categories:
      books += categories.get_books_from_categorie(cat[1])"""
      
   books += categories.get_books_from_categorie("https://books.toscrape.com/catalogue/category/books/mystery_3/index.html") # passe l'url en dur pour les test
      
   print(books)


   

     