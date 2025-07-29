from bs4 import BeautifulSoup
import requests

URL = "https://www.basketball-reference.com/players/m/maxeyty01.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Try to find the top meta block directly
meta = soup.find("div", id="meta")

if meta:
    name = meta.find("h1").text.strip()
    position = meta.find("p").text.strip()

    print("Player:", name)
    print("Position:", position)
else:
    print("❌ Could not find div with id='meta'")







