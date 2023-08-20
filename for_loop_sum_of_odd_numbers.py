# Calculate the sum of odd numbers between 0 to 10

odd_numbers_total = 0
for x in range(11):
    if x%2 == 1:
        odd_numbers_total += x

print(odd_numbers_total)
