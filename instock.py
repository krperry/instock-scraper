import requests
import time
from bs4 import BeautifulSoup

URL = "https://www.aph.org/product/mantis-q40/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
in_stock = soup.find_all("p", class_="stock")   [0].get_text()
print(f"Mantis: {in_stock}")

URL = "https://www.aph.org/product/chameleon-20/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
in_stock = soup.find_all("p", class_="stock")   [0].get_text()
print(f"Chameleon: {in_stock}")

URL = "https://www.aph.org/product/pixblaster/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
in_stock = soup.find_all("p", class_="stock")   [0].get_text()
print(f"PixBlaster: {in_stock}")

URL = "https://www.aph.org/product/pageblaster/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
in_stock = soup.find_all("p", class_="stock")   [0].get_text()
print(f"PageBlaster: {in_stock}")


URL = "https://www.aph.org/product/digital-talking-book-cartridge/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
in_stock = soup.find_all("p", class_="stock")   [0].get_text()
print(f"Green Talking Book Cart: {in_stock}")

URL = "https://www.aph.org/product/sunu-band/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
in_stock = soup.find_all("p", class_="stock")   [0].get_text()
print(f"Sunu Band: {in_stock}")

