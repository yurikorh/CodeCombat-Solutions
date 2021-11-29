while True:
    enemy = hero.findNearestEnemy()
    xPos = hero.pos.x + 5
    yPos = 17
    if enemy:
        # 调整y值，使其向上或向下以摆脱牦牛。
        if enemy.pos.y > hero.pos.y:
            # 如果牦牛在你上面，从yPos中减去3。
            yPos -= 3
            pass
        elif enemy.pos.y < hero.pos.y:
            # 如果牦牛在你下面，给yPos加上3。
            yPos += 3
            pass
    hero.moveXY(xPos, yPos)
