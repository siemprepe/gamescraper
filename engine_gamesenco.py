from bs4 import BeautifulSoup
import requests
import re
import math
import functions
import sys
from game_result import GameResult

def process(inputList):
    shop = "GamesEnCo"
    results = []
    try:
        begin = 1
        increment = 20
    
        basicUrl = "https://www.gamesenco.be/product-categorie/xbox-2/xbox/page/{0}"

        source = requests.get(basicUrl.format(begin)).text
        soup = BeautifulSoup(source, 'lxml')
        pageSelection = soup.find('p', class_='woocommerce-result-count').text.strip()
        total = int(re.findall(r'\d+', pageSelection)[-1])
        total = total / increment

        for x in range(1, math.ceil(total)+1):
            if x > 1:
                source = requests.get(basicUrl.format(x)).text
                soup = BeautifulSoup(source, 'lxml')
            
            ul = soup.find('ul', class_='products')
            for li in ul.findAll('li', class_='product'):
                title = li.find('h2', class_='woocommerce-loop-product__title').text.strip()
                price = li.find('span', class_='woocommerce-Price-amount').text.strip()
                url = li.find('a')['href'] 
                res = functions.titlePresent(title,inputList)
                if res:
                    results.append(GameResult(title,price,url,shop))
        return results
    except:
        print(sys.exc_info()[0])
        results.append(GameResult("ERROR","404","",shop))
        return results