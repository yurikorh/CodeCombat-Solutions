# Если ты попробуешь атаковать врага, твой герой будет это делать, игнорируя все флаги. 
# Ты должен убедиться, что ты атакуешь врагов, которые находятся рядом с тобой!
# without flags
while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.pos.x < 50:
        hero.attack(enemy)
