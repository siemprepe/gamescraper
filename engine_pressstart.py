from bs4 import BeautifulSoup
import requests
import functions
import sys
from game_result import GameResult

def process(inputList):
    shop = "Press Start Games"
    results = []
    try:
        basicUrl = "https://www.press-startgames.com/c-3103097/complete-cib-pal/"
        pageUrl = "https://www.press-startgames.com/c-3103097-{0}/complete-cib-pal/"

        source = requests.get(basicUrl).text
        soup = BeautifulSoup(source, 'lxml')
        pageSelection = soup.find('div', class_='page-selection')
        size = pageSelection.findAll('li')[-2].text

        for x in range(1, int(size)+1):
            sourceUrl = pageUrl.format(x) if x != 1 else basicUrl
            source = requests.get(sourceUrl).text
            soup = BeautifulSoup(source, 'lxml')
            for li in soup.findAll('li', id=lambda x: x and x.startswith('article_')):
                title = li.find('a', class_='title').text.strip()
                pricetag = li.find('span', class_='pricetag')
                price = pricetag.span.text.strip()
                url = li.find('a', class_='image')['href']

                res = functions.titlePresent(title,inputList)
                if res:
                    results.append(GameResult(title,price,url,shop))

        '''run for ntsc put this in common function'''    
        basicUrl = "https://www.press-startgames.com/c-3103098/complete-cib-ntsc/"
        pageUrl = "https://www.press-startgames.com/c-3103098-{0}/complete-cib-ntsc/"

        source = requests.get(basicUrl).text
        soup = BeautifulSoup(source, 'lxml')
        pageSelection = soup.find('div', class_='page-selection')
        if pageSelection is None:
            size = 1
        else:
            size = pageSelection.findAll('li')[-2].text


        for x in range(1, int(size)+1):
            sourceUrl = pageUrl.format(x) if x != 1 else basicUrl
            source = requests.get(sourceUrl).text
            soup = BeautifulSoup(source, 'lxml')
            for li in soup.findAll('li', id=lambda x: x and x.startswith('article_')):
                title = li.find('a', class_='title').text.strip()
                pricetag = li.find('span', class_='pricetag')
                price = pricetag.span.text.strip()
                url = li.find('a', class_='image')['href']

                res = functions.titlePresent(title,inputList)
                if res:
                    results.append(GameResult(title,price,url,shop))
        
        return results
    except:
        print(sys.exc_info()[0])
        results.append(GameResult("ERROR","404","",shop))
        return results