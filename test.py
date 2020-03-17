import engine_madgameshop
import gamescraper_mail
import input
import functions
import game_result

results = engine_madgameshop.process(input.readInput("input.txt"))
for i in results:
    i.print()