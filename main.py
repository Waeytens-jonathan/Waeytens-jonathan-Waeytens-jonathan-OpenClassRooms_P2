import categories
import book


if __name__=="__main__":

   url = "https://books.toscrape.com/" 

   books_categories = categories.get_all_categories(url)
   

   books = []
   """for cat in books_categories:
      books += categories.get_books_from_categorie(cat[1])"""

   print(book.get_book('https://books.toscrape.com/catalogue/the-cuckoos-calling-cormoran-strike-1_239/index.html'))#1
   print(book.get_book('https://books.toscrape.com/catalogue/career-of-evil-cormoran-strike-3_137/index.html')["rating"])
   print(book.get_book('https://books.toscrape.com/catalogue/extreme-prey-lucas-davenport-26_154/index.html'))
   print(book.get_book('https://books.toscrape.com/catalogue/the-mysterious-affair-at-styles-hercule-poirot-1_452/index.html')["rating"])
   print(book.get_book('https://books.toscrape.com/catalogue/the-girl-you-lost_66/index.html')["rating"])
   
   #print(books)