# Defeat as many ogres as you can.
# Use 'cast' and 'canCast' for spells.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if enemy.type == "ogre":
            hero.moveXY(5, 34)
        elif enemy.type == "catapult":
            if hero.canCast("lightning-bolt", enemy):
                hero.cast("lightning-bolt", enemy)
        elif hero.canCast("chain-lightning", enemy):
            hero.cast("chain-lightning", enemy)
        else:
            hero.attack(enemy)
    else:
        if hero.canCast("regen", hero):
            hero.cast("regen", hero)
        else:
            hero.moveXY(8, 30)
