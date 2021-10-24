import categories
import create_csv


if __name__=="__main__":

   url = "https://books.toscrape.com/" 

   books_categories = categories.get_all_categories(url)
   
   books = []
   for cat in books_categories:
      
      books_by_categorie = categories.get_books_from_categorie(cat[1])
      books += books_by_categorie
      create_csv.csv_by_categorie(cat[0], books_by_categorie)