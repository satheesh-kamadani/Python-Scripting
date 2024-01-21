# from player_actions import *
import player_actions

players = [
    {'name': 'messi', 'club': 'barcelona'},
    {'name': 'ronaldo', 'club': 'argentina'},
    {'name': 'mbaphe', 'club': 'french'},
]

print(player_actions.find_player('pele', players))
print(player_actions.makeplayer('messi', 30, job = 'footballer', position = 'forward' ))
