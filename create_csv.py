import csv

def csv_by_categorie(title, all_books):

    title += '.csv'
    print(title)

    with open(title, 'w', encoding='utf-8') as csv_files:

        writer = csv.writer(csv_files, delimiter=',')
        writer.writerow(all_books)