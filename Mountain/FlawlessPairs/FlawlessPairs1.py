# https://codecombat.com/play/level/flawless-pairs
# Collect 4 pairs of gems.
# Each pair must contain equal valued gems.
# Return to the start point to get hasted.

# This function returns two items with the same value.
def findValuePair(items):
    dict = []
    for item in items:
        pair = dict[item.value]
        if pair:
            return [pair, item]
        else:
            dict[item.value] = item


while True:
    gems = hero.findItems()
    gemPair = findValuePair(gems)
    # If the gemPair exists, collect the gems!
    if gemPair:
        # Move to the first gem first (gemPair[0]).
        hero.moveXY(gemPair[0].pos.x, gemPair[0].pos.y)
        # Return to get the haste from the wizard.
        hero.moveXY(40, 44)
        # Move to the second gem first (gempPair[1]).
        hero.moveXY(gemPair[1].pos.x, gemPair[1].pos.y)
        # Return to get the haste from the wizard.
        hero.moveXY(40, 44)
