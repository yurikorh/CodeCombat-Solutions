def weakestFriend():
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

def commandArcher(archer, chief):
    if chief:
        if archer.pos.y < 40:
            hero.command(archer, "attack", chief)
        elif archer.distanceTo(chief) > 20 or chief.pos.x > 60:
            hero.command(archer, "move", chief.pos)
        else:
            hero.command(archer, "move", archer.pos)

def commandSoldier(soldier, chief):
    if chief:
        if soldier.distanceTo(chief) > 20 or chief.pos.x > 60:
            hero.command(soldier, "attack", chief)
        else:
            hero.command(soldier, "move", soldier.pos)
            
paladinDest = Vector(78, 40)
def commandPaladin(paladin, chief):
    dying = weakestFriend()
    if dying and paladin.canCast('heal'):
        hero.command(paladin, "cast", 'heal', dying)
        return
    if chief and chief.pos.x > 60 and chief.health > 100:
        hero.command(paladin, "attack", chief)
    else:
        hero.command(paladin, "move", paladinDest)

def commandRider():
    pass

commands = {'paladin': commandPaladin, 'archer': commandArcher, 'soldier': commandSoldier, 'griffin-rider': commandRider}

def command(chief):
    for friend in hero.findFriends():
        commands[friend.type](friend, chief)

def moveTo(target):
    if hero.isReady("jump"):
        hero.jumpTo(target)
    hero.move(target)

def atk(chief):
    robots = hero.findByType("robot-walker")
    if len(robots):
        hero.move(Vector(14, 21))
    elif chief:
        witch = hero.findNearest(hero.findByType("witch"))
        if witch and hero.canCast("chain-lightning", witch) and chief.pos.x > 60:
            hero.cast("chain-lightning", witch)
        else:
            hero.move(Vector(62, 14))
    else:
        moveTo(Vector(78, 14))

def cheatRobot():
    hero.move(Vector(14, 21))
    robots = hero.findByType("robot-walker")
    hero.summon("griffin-rider")
    rider = hero.findByType("griffin-rider")[0]
    riderTarget = Vector.add(robots[0].pos, robots[1].pos)
    riderTarget = Vector.divide(riderTarget, 2)
    hero.command(rider, "move", riderTarget)

def run():
    cheatRobot()
    while True:
        chief = hero.findNearest(hero.findByType("chieftain"))
        atk(chief)   
        command(chief)

run()

