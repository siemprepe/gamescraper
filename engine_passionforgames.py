from bs4 import BeautifulSoup
import requests
import re
import math
import functions
import sys
from game_result import GameResult

def process(inputList):
    shop = "Passion For Games"
    results = []
    try:
        begin = 1
        basicUrl = "https://www.gamewebshop.eu/en/xbox/page{0}.html"
        source = requests.get(basicUrl.format(begin)).text
        soup = BeautifulSoup(source, 'lxml')
        pageSelection = soup.find('div', class_='pagination-container')
        size = pageSelection.findAll('li')[-2].text

        for x in range(1, int(size)+1):
            if x > 1:
                source = requests.get(basicUrl.format(x)).text
                soup = BeautifulSoup(source, 'lxml')
            
            for div in soup.findAll('div', class_='product'):
                title = div.find('h3').find('a').text.strip()
                pricetag = div.find('div', class_='product-price')
                price = pricetag.span.text.strip()
                url = div.find('h3').find('a')['href']
                
                res = functions.titlePresent(title,inputList)
                if res:
                    results.append(GameResult(title,price,url,shop))
        return results
    except:
        print(sys.exc_info()[0])
        results.append(GameResult("ERROR","404","",shop))
        return results