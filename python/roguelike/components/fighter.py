class Fighter:
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
    
    def take_damage(self, amount):
        self.hp -= amount

    def attack(self, target):
        damage = self.power - target.fighter.defense
        if damage > 0 :
            target.fighter.take_damage(damage)
            print("{0} hugs {1} for {2} love points, " .format(self.owner.name.capitalize(), target.name, str(damage)))
        else:
            print("{0} hugs {1} but does not love.".format(self.owner.name.capitalize(), target.name))