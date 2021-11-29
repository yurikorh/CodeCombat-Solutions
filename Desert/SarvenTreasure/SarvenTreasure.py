while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    portals = [{"x":5, "y":49}, {"x":5, "y":19}, {"x":76, "y":51}, {"x":77, "y":19}]
    if item:
        #if hero.distanceTo(enemy) > 10:
        if enemy:
            if hero.distanceTo(item) < item.distanceTo(enemy) - 4:
                #safe to collect
                hero.move(item.pos)
            else:
                nearest = hero.findNearest(portals)
                if hero.isReady("jump"):
                    hero.jumpTo(nearest)
                else:
                    hero.move(nearest)
        else:
            hero.move(item.pos)

