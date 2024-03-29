import tcod as libtcod
from .game_message import Message
from roguelike.components.ai import ConfusedMonster

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

def cast_fireball(*args, **kwargs):
    entities = kwargs.get("entities")
    fov_map = kwargs.get("fov_map")
    damage = kwargs.get("damage")
    radius = kwargs.get("radius")
    target_x = kwargs.get("target_x")
    target_y = kwargs.get("target_y")

    results = []
    
    if not libtcod.map_is_in_fov(fov_map, target_x, target_y):
        results.append({"consumed" : False, "message" : Message("You cannot feel the love of a tile outside your field of view(Future-octopus-vision)", libtcod.light_magenta)})
        return results
        
    results.append({"consumed" : True, "message" : Message("No enemy is close enough for god to descend.".format(radius), libtcod.light_magenta)})

    for entity in entities:
        if entity.distance(target_x, target_y) <= radius and entity.fighter:
            results.append({"message" : Message("The {0} gets burned by a love beam for {1} love points.".format(entity.name, damage), libtcod.lighter_crimson)})
            results.extend(entity.fighter.take_damage(damage))
        
    
    return results

def cast_confuse(*args, **kwargs):
    entities = kwargs.get("entities")
    fov_map = kwargs.get("fov_map")
    target_x = kwargs.get("target_x")
    target_y = kwargs.get("target_y")

    results = []
    
    if not libtcod.map_is_in_fov(fov_map, target_x, target_y):
        results.append({"consumed" : False, "message" : Message("You cannot feel the love of a tile outside your field of view(Future-octopus-vision)", libtcod.light_magenta)})
        return results

    for entity in entities:
        if entity.x == target_x and entity.y == target_y and entity.ai:
            confused_ai = ConfusedMonster(entity.ai, 10)
            confused_ai.owner = entity
            entity.ai = confused_ai

            results.append({"consumed"  : True, "message" : Message("The {0}'s love starts to fade away, he looks like he went crazy!".format(entity.name), libtcod.light_sepia)})

            break
        
    else:
        results.append({"consumed" : False, "message" : Message("There is no targetable enemy at that location.", libtcod.dark_crimson)})

    return results