import engine_lamar
import gamescraper_mail
import input
import functions
import game_result

'''
ilist = input.readInput("input.txt")

words = ['shrek', '2']
sentence = ['shrek 2','shrek']
title = 'shrek'

def check(inputList, titleParts): 
    res = list(map(lambda x: all(map(lambda y:y.upper() in x.split(), titleParts)), inputList)) 
    out = [inputList[i].upper() for i in range(0, len(res)) if res[i]]
    return out != []

def check2(title, words): 
    res = [] 
    for substring in title: 
        k = [ w for w in words if w in substring.upper() ] 
        if (len(k) == len(words) ): 
            res.append(substring) 
              
    return res != []

def titlePresent(title, inputList):
    for i in inputList:
        if check2([title],i.split()):
            result = True
            break
    else:
        result = False
    return result

print(titlePresent(title,ilist))'''

results = engine_lamar.process(input.readInput("input.txt"))
for i in results:
    i.print()

'''content = "<html><body><h1>TESTING</h1><p>test</p></body></html>"
gamescraper_mail.sendHtmlMail(content)

results = []
results.append(game_result.GameResult("title1","5.00","http://google.com","SHOP 1"))
results.append(game_result.GameResult("title2","9.00","http://google.com","SHOP ssdd"))
results.append(game_result.GameResult("title3","12.00","http://google.com","SHOP 6"))

gamescraper_mail.sendHtmlMail(functions.buildHTML(results))'''