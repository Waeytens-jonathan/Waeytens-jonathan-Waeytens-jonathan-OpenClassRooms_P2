import categories
import create_csv
import os


if __name__=="__main__":

   url = "https://books.toscrape.com/" 

   books_categories = categories.get_all_categories(url)

   if not os.path.exists("all_books_categories"): #conditionne la création des dossiers
      os.mkdir("all_books_categories")

   if not os.path.exists("images"):
      os.mkdir("images")
   
   
   for cat in books_categories:
      
      books_by_categorie = categories.get_books_from_categorie(cat[1])
      create_csv.csv_by_categorie(cat[0], books_by_categorie)