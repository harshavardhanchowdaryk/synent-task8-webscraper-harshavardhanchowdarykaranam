import requests
from bs4 import BeautifulSoup
import csv

# Website URL
url = "https://books.toscrape.com/"

# Sending request to website
response = requests.get(url)

# Parsing HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Finding all book containers
books = soup.find_all("article", class_="product_pod")

# Creating CSV file
file = open("books_data.csv", "w", newline="", encoding="utf-8")

writer = csv.writer(file)

# Writing header
writer.writerow(["Book Title", "Price"])

# Extracting data
for book in books:

    title = book.h3.a["title"]

    price = book.find("p", class_="price_color").text

    writer.writerow([title, price])

    print("Title:", title)
    print("Price:", price)
    print("---------------------")

file.close()

print("Data saved to books_data.csv")