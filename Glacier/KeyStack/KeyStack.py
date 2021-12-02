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

# Command the peasant to drop a key near the first door.
hero.command(peasant, "dropItem", {"x": 40, "y": 34})
# The second key -> the second door.
hero.command(peasant, "dropItem", {"x": 31, "y": 34})
# Drop the first (in the stack) key to the last door:
hero.command(peasant, "dropItem", {"x": 21, "y": 34})
hero.command(peasant, "move", {"x": 73, "y": 36})
# Hurry and collect treasures!
hero.moveXY(14, 34)
hero.jumpTo(Vector(14, 50))
hero.moveXY(11, 58)
hero.moveXY(8, 40)
hero.wait(hero.getCooldown("jump"))
hero.jumpTo(Vector(6, 20))
hero.moveXY(10, 11)
