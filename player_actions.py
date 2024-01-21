def makeplayer(name, age, **dict):
    player = {}
    player['name'] = name
    player['age'] = age
    for k, v in dict.items():
        player[k] = v
    return player

def find_player(name, players):
    for player in players:
        if player['name'] == name:
            return True
        else:
            return False