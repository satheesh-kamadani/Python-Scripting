player = {
    'name': 'Messi',
    'age': 30,
    'team': 'Argentina',
    'position': 'forward',
}
print(player)

print(player['age'])
print(player['position'])

for key in player.values():
    print(key)

for key, value in player.items():
    print(key, value)

