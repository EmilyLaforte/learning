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
                "item_added" : item,
                "message" : Message("You pickup the {0} with love!".format(item.name), libtcod.lightest_purple)

            })

            self.items.append(item)

        return results

    def use(self, item_entity, **kwargs):
        results = []

        item_component = item_entity.item

        if item_component.use_function is None:
            results.append({"message" : Message("The {0} cannot be used".format(item_entity.name), libtcod.lighter_fuchsia)})
        else:
            kwargs = {**item_component.function_kwargs, **kwargs}
            item_use_results = item_component.use_function(self.owner, **kwargs)

            for item_use_result in item_use_results:
                if item_use_result.get("consumed"):
                    self.remove_item(item_entity)

            results.extend(item_use_results)

        return results

    def remove_item(self, item):
        self.items.remove(item)

    def drop_item(self, item):
        results = []
        item.x = self.owner.x
        item.y = self.owner.y

        self.remove_item(item)
        results.append({"item_dropped" : item, "message": Message("You drop the {0}, you regret droping it. You do not feel it's love anymore".format(item.name), libtcod.lightest_fuchsia)})

        return results