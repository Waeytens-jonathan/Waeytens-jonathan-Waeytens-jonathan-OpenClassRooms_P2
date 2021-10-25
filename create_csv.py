import csv

def csv_by_categorie(title, all_books):

    title += '.csv'
    csv_columns = []

    if len(all_books):
        csv_columns = all_books[0].keys()

    else: 
        return

    with open(title, 'w', encoding='utf-8') as csv_file:

        writer = csv.DictWriter(csv_file, fieldnames = csv_columns )
        writer.writeheader()

        for book in all_books:

            writer.writerow(book)