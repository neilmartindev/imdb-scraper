import random
from typing import Mapping
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'

def main():
    response = requests.get(url)
    html = response.text
    
    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select('td.titleColumn')
    movietag0 = movietags[0]
    moviesplit = movietag0.text.split()
    
    print(moviesplit)
    
    
if __name__ == '__main__':
    main()