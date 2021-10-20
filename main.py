import page
import categories
import create_csv
import book


if __name__=="__main__":

   url = "https://books.toscrape.com/" 

   books = book.get_book("https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html")
   print(books)

   test = categories.get_all_categories(url)
   print(test)

   

    