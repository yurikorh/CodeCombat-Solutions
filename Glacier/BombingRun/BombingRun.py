# http://codecombat.com/play/level/bombing-run
# Incoming oscars! (That's military speak for ogres).
# Тебе нужно рассчитать угол их атаки.
# Используй тригонометрию, чтобы найти угол в радианах!

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        vector = Vector.subtract(enemy.pos, hero.pos)
        rad = Math.atan2(vector.y, vector.x)
        deg = rad * (180 / Math.PI)
        hero.say(deg)
