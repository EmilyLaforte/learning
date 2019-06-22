import tcod as libtcod

from roguelike.game_message import Message

class Fighter:
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
    
    def take_damage(self, amount):
        results = []
        self.hp -= amount

        if self.hp <= 0:
            results.append({"dead" : self.owner})

        return results

    def attack(self, target):
        results = []
        damage = self.power - target.fighter.defense
        if damage > 0 :
            target.fighter.take_damage(damage)
            results.append({"message" : Message("{0} hugs {1} for {2} love points, " .format(
                            self.owner.name.capitalize(), target.name, str(damage)), libtcod.magenta)})
            results.extend(target.fighter.take_damage(damage))
        else:
            results.append({"message" : Message("{0} hugs {1} but gets no love back." .format(
                            self.owner.name.capitalize(), target.name, str(damage)), libtcod.magenta)})
        return results