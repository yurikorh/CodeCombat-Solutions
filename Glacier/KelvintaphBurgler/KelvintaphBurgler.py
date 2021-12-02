def lowHP():
    friends = hero.findFriends()
    lowest = 9999
    dying = None
    if len(friends):
        for friend in friends:
            hp = friend.health
            if hp < friend.maxHealth / 3 and hp < lowest and hp > 0:
                lowest = hp
                dying = friend
    return dying

archerDest = Vector(55, 38)
def commandArcher(archer):
    enemies = hero.findByType("chieftain")
    if len(enemies):
        enemy = enemies[0]
        if archer.distanceTo(archerDest) < 1:
            hero.command(archer, "attack", enemy)
        elif archer.distanceTo(enemy) > 20 or enemy.pos.x > 60:
            hero.command(archer, "move", archerDest)
        else:
            hero.command(archer, "move", archer.pos)

paladinDest = Vector(78, 40)
def commandPaladin(paladin):
    dying = lowHP()
    if dying and paladin.canCast('heal'):
        hero.command(paladin, "cast", 'heal', dying)
    elif paladin.canCast('heal') and hero.health < 2 * hero.maxHealth / 3:
        hero.command(paladin, "cast", 'heal', hero)
    elif paladin.pos.x >= paladin.x:
        hero.command(paladin, "shield")
    else:
        hero.command(paladin, "move", paladinDest)

def command():
    for friend in hero.findFriends():
        type = friend.type
        if type == 'paladin':
            commandPaladin(friend)
        elif type == 'archer':
            commandArcher(friend)

def atk():
    robots = hero.findByType("robot-walker")
    if len(robots):
        hero.move(Vector(14, 21))
    else:
        chief = hero.findNearest(hero.findByType("chieftain"))
        if chief:
            witch = hero.findNearest(hero.findByType("witch"))
            if witch and hero.canCast("chain-lightning", witch) and chief.pos.x > 60:
                hero.cast("chain-lightning", witch)
            hero.move(Vector(62, 18))
        else:
            hero.move(Vector(78, 14))


def run():
    hero.move(Vector(14, 21))
    robots = hero.findByType("robot-walker")
    hero.summon("griffin-rider")
    rider = hero.findByType("griffin-rider")[0]
    riderTarget = Vector.add(robots[0].pos, robots[1].pos)
    riderTarget = Vector.divide(riderTarget, 2)
    hero.command(rider, "move", riderTarget)
    
    while True:
        atk()   
        command()

run()
