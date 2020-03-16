from bs4 import BeautifulSoup
import requests
import re
import math
import functions
import sys
from game_result import GameResult

def process(inputList):
    shop = "RetroGamesCorner"
    results = []
    try:
        begin = 1
        increment = 24
    
        basicUrl = "https://www.retrogamescorner.com/44-xbox?page={0}"

        source = requests.get(basicUrl.format(begin)).text
        soup = BeautifulSoup(source, 'lxml')
        pageSelection = soup.find('div', class_='total-products').text.strip()
        total = int(re.findall(r'\d+', pageSelection)[-1])
        total = total / increment

        for x in range(1, math.ceil(total)+1):
            if x > 1:
                source = requests.get(basicUrl.format(x)).text
                soup = BeautifulSoup(source, 'lxml')
            
            for article in soup.findAll('article', class_='product-miniature'):
                title = article.find('h1', class_='product-title').find('a').text.strip()
                price = article.find('span', class_='price').text.strip()
                url = article.find('h1', class_='product-title').find('a')['href']
                res = functions.titlePresent(title,inputList)
                if res:
                    results.append(GameResult(title,price,url,shop))
        return results
    except:
        print(sys.exc_info()[0])
        results.append(GameResult("ERROR","404","",shop))
        return results