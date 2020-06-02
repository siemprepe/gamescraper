import input
import functions
import gamescraper_mail
import engine_lamar
import engine_nedgame
import engine_madgameshop
import engine_jprs
import engine_gamesenco
import engine_twente
import engine_groningen
import engine_gamecorner
import engine_pressstart
import engine_gameking
import engine_passionforgames

print("Scraping for " + functions.getToday())
print("Reading input")
inputList = input.readInput("input.txt")
print("Reading done")

print("Processing Lamar Games")
results = engine_lamar.process(inputList)
print("Processing NedGame")
results.extend(engine_nedgame.process(inputList))
print("Processing MAD-Gameshop")
results.extend(engine_madgameshop.process(inputList))
print("Processing JPRS Games")
results.extend(engine_jprs.process(inputList))
print("Processing GamesEnCo")
results.extend(engine_gamesenco.process(inputList))
print("Processing Gameshop Twente")
results.extend(engine_twente.process(inputList))
print("Processing Gameland Groningen")
results.extend(engine_groningen.process(inputList))
print("Processing RetroGamesCorner")
results.extend(engine_gamecorner.process(inputList))
print("Processing Press Start Games")
results.extend(engine_pressstart.process(inputList))
print("Processing Retro Game King")
results.extend(engine_gameking.process(inputList))
print("Processing Passion for games")
results.extend(engine_passionforgames.process(inputList))

print("Peparing and sending email")
gamescraper_mail.sendHtmlMail(functions.buildHTML(results))
print("Done!")