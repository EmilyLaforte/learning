import tcod as libtcod
from .game_message import Message

def heal(*args, **kwargs):
    entity = args[0]
    amount = kwargs.get("amount")

    results = []
    
    if entity.fighter.hp == entity.fighter.max_hp:
        results.append({"consumed" : False, "message" : Message("You are already at maximum love points.", libtcod.lightest_fuchsia)})
    else:
        entity.fighter.heal(amount)
        results.append({"consumed" : True, "message" : Message("You feel your love points increasing!", libtcod.light_violet)})

    return results