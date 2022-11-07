"""a program that first asks the user how much change is owed and then
spits out the minimum number of coins with which said change can be made."""

# Try to get the change
change: int = 0
while True:
    try:
        change = int(float(input("Change owed: ")) * 100)
        if change < 0:
            continue

        break
    except ValueError:
        continue

coins = [25, 10, 5, 1]
count = 0

# Count how may coin is needed
for coin in coins:
    while change >= coin:
        change -= coin
        count += 1

print(count)
