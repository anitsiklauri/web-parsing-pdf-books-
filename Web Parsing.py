import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

def scrape_books(url, page_limit):
    headers = {'Accept-Language': 'en-US'}
    csv_file = open('PDF_BOOKS.csv', 'w', encoding='UTF-8_sig', newline='\n')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title', 'Author', 'Editions'])

    for page in range(1, page_limit+1):
        payloads = {'page': page}
        response = requests.get(url, params=payloads, headers=headers)
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        books_soup = soup.find('ul', class_='list-books')
        all_books = books_soup.find_all('li', class_='searchResultItem')

        for book in all_books:
            title = book.find('div', class_='resultTitle').text.strip()
            author = book.find('span', class_='bookauthor').text.strip()
            editions = book.find('span', class_='resultPublisher').a.text.strip()
            csv_writer.writerow([title, author, editions])
            print(f"Title: {title}, Author: {author}, Editions: {editions}")

        sleep(randint(5, 10))

    csv_file.close()

url = 'https://openlibrary.org/trending/daily'
page_limit = 5

scrape_books(url, page_limit)
