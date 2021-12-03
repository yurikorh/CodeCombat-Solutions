# https://codecombat.com/play/level/golden-choice
# You must collect the required amount of gold.
# The gate keeper will tell you how much you need.
# Always move in the direction of the exit.
# For each row you can take only one coin.
# Choose only one from the nearest coins in the next row.

goldMap = [[0 for j in range(2 * lines - 1)] for i in range(lines)]
for coin in hero.findItems():
    row = int((coin.pos.y - zeroPoint.y) / distanceY)
    col = int((coin.pos.x - zeroPoint.x) / distanceX)
    goldMap[row][col] = coin.value

# Distance between rows and coins.
distanceX = 4
distanceY = 6
zeroPoint = {"x": 14, "y": 14}
coinLines = 10

def makeGoldMap(coins):
    template = [[0 for j in range(2 * coinLines - 1)] for i in range(coinLines)]
    for coin in coins:
        row = int((coin.pos.y - zeroPoint.y) / distanceY)
        col = int((coin.pos.x - zeroPoint.x) / distanceX)
        template[row][col] = coin.value
    return template

def convert(row, col):
    return col * distanceX + zeroPoint.x, row * distanceY + zeroPoint.y

# Prepare the gold map.
# [[1, 0, 9, 0, 4],
#  [0, 1, 0, 9, 0],
#  [8, 0, 2, 0, 9]]
goldMap = makeGoldMap(hero.findItems())

# Find your path.
for i in range(len(goldMap) - 1, 0, -1):
    for j in range((i - 1) & 1, len(goldMap[0]) - 1, 2):
        if j == 0:
            goldMap[i - 1][j] += goldMap[i][j + 1]
        elif j == len(goldMap[i]) - 1:
            goldMap[i - 1][j] += goldMap[i][j - 1]
        else:
            goldMap[i - 1][j] += Math.max(goldMap[i][j - 1], goldMap[i][j + 1])

index = 0
max = 0
for i in range(0, len(goldMap[0]) - 1, 2):
    if goldMap[0][i] > max:
        max = goldMap[0][i] 
        index = i

# index = goldMap[0].index(max(goldMap[0]))

x, y = convert(0, index)
hero.jumpTo(Vector(x, hero.pos.y))
hero.moveXY(x, y)

for i in range(1, len(goldMap), 1):
    if index == 0:
        index = 1
    elif index == len(goldMap[0]) - 1:
        index -= 1
    elif goldMap[i][index - 1] >= goldMap[i][index + 1]:
        index -= 1
    else:
        index += 1
    x, y = convert(i, index)
    hero.moveXY(x, y)
