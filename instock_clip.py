"""A version of instock that uses the clipboard"""
#See readme for module install commands
import requests
from bs4 import BeautifulSoup
import clipboard

# List of URLs and device names
urls = [
    ("https://www.aph.org/product/mantis-q40/", "Mantis"),
    ("https://www.aph.org/product/chameleon-20/", "Chameleon"),
    ("https://www.aph.org/product/pixblaster/", "PixBlaster"),
    ("https://www.aph.org/product/pageblaster/", "PageBlaster"),
    ("https://www.aph.org/product/digital-talking-book-cartridge/", "Green Talking Book Cart"),
    ("https://www.aph.org/product/sunu-band/", "Sunu Band")
]

# Loop through each URL and device name
result = ""
for url, device_name in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    in_stock = soup.find_all("p", class_="stock")[0].get_text()
    result += f"{device_name}: {in_stock}\n"

clipboard.copy(result)
print("Stock information has been copied to the clipboard.")
