# http://codecombat.com/play/level/goalkeeper
# Управляйте крестьянами, чтобы не позволить ограм забить гол.
# Тип огненного шара (файербол) - "ball"
while True:
    item = hero.findNearest(hero.findByType('ball'))
    friends = hero.findFriends()
    v = item.velocity
    vx = v.x
    vy = v.y
    if vx < 0:
        # ball radius should be considered
        # the faster the ball moves, the earlier we should defence
        y = (item.pos.x - 20 + vx * 0.1) / vx * vy + item.pos.y
        if y < 20:
            y = 60 - (60 - y)  % 40
        elif y > 60:
            y = 20 + (y - 20) % 40
    else:
        # back to middle and wait
        y = 40
    hero.command(friends[0], "move", {"x": 15, "y": y - 2.5})
    hero.command(friends[1], "move", {"x": 15, "y": y + 2.5})    
