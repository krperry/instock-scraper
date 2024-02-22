import requests
from bs4 import BeautifulSoup

URL = "https://www.aph.org/product/mantis-q40/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
in_stock = soup.find_all("p", class_="stock")	[0].get_text()
print(f"Mantis: {in_stock}")
