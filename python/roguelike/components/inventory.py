import tcod as libtcod

from roguelike.game_message import Message

class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        results = []

        if len(self.items) >= self.capacity:
            results.append({
                "item_added" : None,
                "message" : Message("You cannot get more, you received too much love!".format(item.name), libtcod.lightest_purple)

            })

        else:
            results.append({
                "item_added" : None,
                "message" : Message("You pickup the {0} with love!".format(item.name), libtcod.lightest_purple)

            })

            self.items.append(item)

        return results
        