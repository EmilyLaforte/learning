import tcod as libtcod

def render_all(con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors):
    for y in range(game_map.height):
        for x in range(game_map.width):
            visible = libtcod.map_is_in_fov(fov_map, x, y)
            wall = game_map.tiles[x][y].block_sight
            if visible:
                if wall:
                    color_name = "light_wall"

                else:
                    color_name = "light_ground"

            else:
                if wall:
                    color_name = "dark_wall"

                else:
                    color_name = "dark_ground"
                
            libtcod.console_set_char_background(con, x, y, colors.get(color_name), libtcod.BKGND_SET)
                
    #Draw all entities in the list
    for entity in entities:
        draw_entity(con, entity)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)

def draw_entity(con, entity):
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

def clear_entity(con, entity):
    #erase the character that represents this object
    libtcod.console_put_char(con, entity.x, entity.y, " ", libtcod.BKGND_NONE)