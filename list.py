fruites = ['mango', 'banana', 'grapes']
print(fruites)
fruites.append('kiwi')
print(fruites)
fruites.insert(0, 'apple')
print(fruites)
fruites.remove('grapes')
print(fruites)

for i in fruites:
    if len(i) <= 5:
        print(i)

