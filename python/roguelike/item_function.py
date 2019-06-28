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

def cast_lightning(*args, **kwargs):
    caster = args[0]
    entities = kwargs.get("entities")
    fov_map = kwargs.get("fov_map")
    damage = kwargs.get("damage")
    maximum_range = kwargs.get("maximum_range")

    results = []

    target = None
    closest_distance = maximum_range + 1

    for entity in entities:
        if entity.fighter and entity != caster and libtcod.map_is_in_fov(fov_map, entity.x, entity.y):
            distance = caster.distance_to(entity)

            if distance < closest_distance:
                target = entity
                closest_distance = distance
    
    if target:
        results.append({"consumed" : True, "target" : target, "message" : Message("A god descend's from heaven and gives a BIG HUG to the {0}! It made it lose {1} love points".format(target.name, damage))})
        results.extend(target.fighter.take_damage(damage))
    else:
        results.append({"consumed" : False, "target" : None, "message" : Message("No enemy is close enough for god to descend.", libtcod.light_magenta)})
    
    return results