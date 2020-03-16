from bs4 import BeautifulSoup
import requests
import re
import math
import functions
import sys
from game_result import GameResult

def process(inputList):
    shop = "Gameland-Groningen"
    results = []
    try:
        begin = 1
        basicUrl = "https://www.gameland-groningen.nl/nl/xbox/xbox-classic/games/page{0}.html"

        source = requests.get(basicUrl.format(begin)).text
        soup = BeautifulSoup(source, 'lxml')
        pageSelection = soup.find('span', class_='page-product-count').text.strip()
        increment = soup.find('span', class_='page-info').find('option', selected=True).text.strip()
        total = int(pageSelection)
        total = total / int(increment)

        for x in range(1, math.ceil(total)+1):
            if x > 1:
                source = requests.get(basicUrl.format(x)).text
                soup = BeautifulSoup(source, 'lxml')
            for div in soup.findAll('div', class_='product'):
                title = div.find('div', class_='info').find('a').text.strip()
                price = div.find('span', class_='new-price').text.strip()
                url = div.find('div', class_='info').find('a')['href'] 
                res = functions.titlePresent(title,inputList)
                if res:
                    results.append(GameResult(title,price,url,shop))
        return results
    except:
        print(sys.exc_info()[0])
        results.append(GameResult("ERROR","404","",shop))
        return results