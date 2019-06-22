import tcod as libtcod
from .game_states import GameStates
from .render_functions import RenderOrder
from roguelike.game_message import Message

def kill_player(player):
    player.char = "$"
    player.color = libtcod.dark_fuchsia

    return Message("You got hugged to death!", libtcod.pink), GameStates.PLAYER_DEAD

def kill_monster(monster):
    death_message = Message("{0} is dead from love overflow".format(monster.name.capitalize()), libtcod.magenta)

    monster.char = "$"
    monster.color = libtcod.darker_fuchsia
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = "love remains of " + monster.name
    monster.render_order = RenderOrder.CORPSE

    return death_message