import categories
import book


if __name__=="__main__":

   url = "https://books.toscrape.com/" 

   books = book.get_book("https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html")
   print(books)
   

   books_categories = categories.get_all_categories(url)
   

   print(books_categories[0])
   
 
   for cat in books_categories:
      categories.get_books_from_categorie(cat[1])


   

    