
# Books-Scraper

Ce programme sert à extraire les données des livres du site: https://books.toscrape.com/

Il extrait les informations suivantes:

- product_page_url
- universal_ product_code (upc)
- title
- price_including_tax
- price_excluding_tax
- number_available
- product_description
- category
- review_rating
- image_url
- image.jpg

Il ajoute un dossier "all_books_categories" dans lequel il va écrire toutes les infos 
dans un fichier .CSV

Il ajoute un dossier "images" dans lequel il va stocker toutes les images 
dans un fichier .jpg

---
Version Python: 3.9.6 
---

Bibliothèques:

- requests
- BeautifulSoup
- csv 
- os

Le lancement du programme ce fait à partir du main.py
