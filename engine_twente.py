from bs4 import BeautifulSoup
import requests
import re
import math
import functions
import sys
from game_result import GameResult

def process(inputList):
    shop = "Gameshop-Twente"
    results = []
    try:
        begin = 1
        increment = 16
    
        basicUrl = "https://www.gameshop-twente.nl/inhoudZoeken.php?blz={0}&&maxAantalResults={1}&&productgroep=&&systeem=Genre_Games&&genre=&&actie=navbar_klik&&tagNegeer=niets&&meegekregenTermen=_@Systeem@XBX_@Groep@Games"
        source = requests.get(basicUrl.format(begin,increment)).text
        soup = BeautifulSoup(source, 'lxml')
        pages = soup.find('input', id='aantalBladzijden')['value']

        for x in range(1, int(pages)+1):
            if x > 1:
                source = requests.get(basicUrl.format(x,increment)).text
                soup = BeautifulSoup(source, 'lxml')
            
            for div in soup.findAll('div', id='browse_resultbox_zoekpagina'):
                title = div.find('table').find('a').text.strip()
                prices = div.findAll('div', class_='genoegVoorraad')
                if len(prices) > 0:
                    price = ""
                    for i in prices:
                        price = price + i.find('span', id='prijs_center').text.strip() + " "
                    url = div.find('table').find('a')['href']
                    res = functions.titlePresent(title,inputList)
                    if res:
                        results.append(GameResult(title,price,"https://www.gameshop-twente.nl/" + url,shop))
        return results
    except:
        print(sys.exc_info()[0])
        results.append(GameResult("ERROR","404","",shop))
        return results