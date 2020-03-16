from bs4 import BeautifulSoup
import requests
import re
import functions
import sys
from game_result import GameResult

def process(inputList):
    shop = "JPRS Games"
    results = []
    try:
        begin = 1
        end = 40
        increment = 39
    
        basicUrl = "https://jprsgames.nl/index.php/xbox/games2013-04-03-09-00-102013-04-03-09-00-10-3/results,{0}-{1}"

        source = requests.get(basicUrl.format(begin,end)).text
        soup = BeautifulSoup(source, 'lxml')
        pageSelection = soup.find('div', class_='display-number').contents[0].strip()
        total = int(next(re.finditer(r'\d+$', pageSelection)).group(0)) + increment

        while end < total:
            if begin > 1:
                source = requests.get(basicUrl.format(begin,end)).text
                soup = BeautifulSoup(source, 'lxml')
            
            for div in soup.findAll('div', class_='product'):
                titleDiv = div.find('div', class_=lambda x: x and x.startswith('vm-product-descr-container'))
                title = titleDiv.find('h2').text.strip()
                price = div.find('span', class_='PricesalesPrice').text.strip()
                url = titleDiv.find('h2').find('a')['href'] 
                res = functions.titlePresent(title,inputList)
                if res:
                    results.append(GameResult(title,price,'https://jprsgames.nl' + url,shop))

            begin = begin + 39
            end = end + 39
        return results
    except:
        print(sys.exc_info()[0])
        results.append(GameResult("ERROR","404","",shop))
        return results