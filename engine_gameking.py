from bs4 import BeautifulSoup
import requests
import re
import math
import functions
import sys
from game_result import GameResult

def process(inputList):
    shop = "RetroGameKing"
    results = []
    try:
        begin = 1
        increment = 60
        basicUrl = "https://www.retrogameking.com/epages/78704979.sf/nl_NL/?ViewAction=View&ObjectPath=/Shops/78704979/Categories/Xbox/Xbox_Games&PageSize={1}&Page={0}"
        source = requests.get(basicUrl.format(begin,increment)).text
        soup = BeautifulSoup(source, 'lxml')
        pageSelection = soup.find('ul', class_='PagerSizeContainer')
        size = pageSelection.findAll('li')[-2].text

        for x in range(1, int(size)+1):
            if x > 1:
                source = requests.get(basicUrl.format(x,increment)).text
                soup = BeautifulSoup(source, 'lxml')
            
            for div in soup.findAll('div', class_='InfoArea'):
                title = div.find('h3').find('a').text.strip()
                pricetag = div.find('span', class_='price-value')
                price = pricetag.span.text.strip()
                url = div.find('h3').find('a')['href']
                
                res = functions.titlePresent(title,inputList)
                if res:
                    results.append(GameResult(title,price,"https://www.retrogameking.com/epages/78704979.sf/nl_NL/" + url,shop))
        return results
    except:
        print(sys.exc_info()[0])
        results.append(GameResult("ERROR","404","",shop))
        return results