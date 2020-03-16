from bs4 import BeautifulSoup
import requests
import functions
import sys
from game_result import GameResult

source = ""
soup = ""
pageIndex = 1
next = True

def process(inputList):
    global next
    global source
    global soup
    global pageIndex
    results = []
    
    while next:
        results.extend(runInternal(inputList))
    
        pageSelection = soup.find('div', class_='paging_full_numbers')
        nextBtn = pageSelection.findAll('span')[-1].text
        next = True if nextBtn == "»" else False
        if next:
            pageIndex = pageIndex + 1

    return results


def runInternal(inputList):
    shop = "NedGame"
    results = []
    try:
        global next
        global source
        global soup
        global pageIndex
        
        basicUrl = "https://www.nedgame.nl/xbox/games/&aantal=100&pagina={0}"
        source = requests.get(basicUrl.format(pageIndex)).text
        soup = BeautifulSoup(source, 'lxml')

        for tr in soup.findAll('tr', id=lambda x: x and x.startswith('prod_id')):
            titleDiv = tr.find('div', class_='titlewrapper')
            title = titleDiv.find('h3').text.strip()
            price = tr.find('div', class_='currentprice').text.strip()
            url = titleDiv.find('a')['href'] 
            res = functions.titlePresent(title,inputList)
            if res:
                results.append(GameResult(title,price,url,shop))
        return results
    except:
        print(sys.exc_info()[0])
        results.append(GameResult("ERROR","404","",shop))
        return results