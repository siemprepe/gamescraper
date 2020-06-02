import engine_passionforgames
import gamescraper_mail
import input
import functions
import game_result

results = engine_passionforgames.process(input.readInput("input.txt"))
for i in results:
    i.print()