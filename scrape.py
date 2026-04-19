import requests
from bs4 import BeautifulSoup
import json

#git  => version control system
# git config --global user.name "Anisha Lama"
# git config --global user.email "anishamktn23@gmail.com"
# git status => if you want to check what are the status of files
# git add . =>track all file in current directory
# git commit -m "first commit" => commit the changes with message

url = "https://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)
    #print(response.status_code)
    #response(response)
    #response(request.text) 


    if response.status_code != 200:
        print("Failed to fetch page")
        return []

    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    all_books = []

    for book in books:
        title = book.h3.a['title']
        price_text = book.find("p", class_="price_color").text.strip()

        currency = price_text[0]
        price = float(price_text[1:])

        my_book = {
            "title": title,
            "price": price,
            "currency": currency
        }
             
        all_books.append(my_book)

    return all_books


# function call (IMPORTANT: function बाहिर हुनुपर्छ)
books = scrape_books(url)

# save to JSON
with open("books.json", "w", encoding="utf-8") as f:
    json.dump(books, f, indent=4, ensure_ascii=False)


 