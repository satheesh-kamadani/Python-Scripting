fruites = ['mango', 'banana', 'grapes']
print(fruites)
fruites[1] = 'kiwi_fruite'
fruites.append('kiwi')
print(fruites)
fruites.insert(0, 'apple')
print(fruites)
fruites.remove('grapes')
print(fruites)
fruites.append('cherries')
print(fruites)

removed_items = fruites.pop()
print(removed_items)
print(fruites)
fruites.pop(0)
print(fruites)

for i in fruites:
    if len(i) <= 5:
        print(i)

