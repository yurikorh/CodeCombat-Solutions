# https://codecombat.com/play/level/key-stack
# Open doors and collect treasures.

peasant = hero.findByType("peasant")[0]

goldKey = peasant.findByType("gold-key")[0]
silverKey = peasant.findByType("silver-key")[0]
bronzeKey = peasant.findByType("bronze-key")[0]

# Command the peasant to pick up the gold and silver keys.
hero.command(peasant, "pickUpItem", goldKey)
hero.command(peasant, "pickUpItem", silverKey)
# Now, command the peasant to pick up the last key:
hero.command(peasant, "pickUpItem", bronzeKey)
hero.moveXY(46, 35)
# Command the peasant to drop a key near the first door.
hero.command(peasant, "dropItem", {"x": 40, "y": 34})
# The second key -> the second door.
hero.command(peasant, "dropItem", {"x": 31, "y": 34})
# Drop the first (in the stack) key to the last door:
hero.command(peasant, "dropItem", {"x": 21, "y": 34})
hero.command(peasant, "move", {"x": 73, "y": 36})
# Hurry and collect treasures!
def pickUpItem():
    gem = hero.findNearestItem()
    if gem:
        moveTo(gem.pos)
        
def isClear(target):
    for hazard in hero.findHazards():
        targetVec = Vector.subtract(target, hero.pos)
        hazardVec = Vector.subtract(hazard.pos, hero.pos)
        if targetVec.dot(hazardVec) > 0 and hazardVec.magnitude() < 5:
            return False
    return True
    
# Y axis only
def isClearY(target):
    for hazard in hero.findHazards():
        hazardDiff = hazard.pos.y - hero.pos.y
        targetDiff = target.y - hero.pos.y
        if hazardDiff * targetDiff > 0 and hero.distanceTo(hazard) < 5 :
            return False
    return True

def moveTo(target):
    # alternative: if isClearY(target):
    if isClear(target):
        hero.move(target)
    else: 
        # stop moving
        hero.move(hero.pos)
        # since the jumpTo method waits until it's ready by itself, there's no need to wait manually
        # hero.wait(hero.getCooldown("jump"))
        hero.jumpTo(target)
        # wait for landing
        hero.wait(1)
        
while True:
    pickUpItem()
