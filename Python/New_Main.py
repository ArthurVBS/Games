#Import - Libraries _________________________________________________________________________________________

import os
from tkinter import *

#Import - Packages __________________________________________________________________________________________

from Utils.images import images
from Utils.defs import main_roots, game_roots, default, show_items_values, start_the_game
from Utils.defs import game_widgets, menu_widgets, credits_widgets, options_widgets, gameover_widgets

#Variables __________________________________________________________________________________________________

title = '- Looking for -\n a way out '
version = 'layout v 2.8.2'
directory = os.path.dirname(__file__)

global items_values
items_values = {
    'level' : 1, 'world' : 1,

    'food' : 5, 'heart' : 80,

    'key_B' : True, 'key_S' : False, 'key_G' : False,

    'item_lighter' : True, 'item_future_friendship' : False,
    'item_wolfhide' : False, 'item_shotgun' : False,
    'item_nausea' : False, 'item_crowbar' : False,
    'item_screwdriver' : False, 'item_gear' : False}

#Tkinter ____________________________________________________________________________________________________

window = Tk()

width = 720
height = 470
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
pos_x = int(width_screen / 2 - width / 2)
pos_y = int(height_screen / 2 - height / 2)

window.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
window.resizable(False,False)
window['background'] = '#000'

#_____________________________________________________________________________________________________________

images = images(directory)

main_roots = main_roots(window)
game_roots = game_roots(main_roots)
game_widgets = game_widgets(window, main_roots, directory, game_roots, images, version, menu_widgets)

default(window, images, game_widgets)
show_items_values(images, game_widgets)

menu_widgets = menu_widgets(window, main_roots, directory, default, version, images, game_widgets, title)
credits_widgets = credits_widgets(window, main_roots, directory, version, title)
options_widgets = options_widgets(window, main_roots, directory, images)
gameover_widgets = gameover_widgets(window, main_roots, directory, menu_widgets)

start_the_game(window, main_roots, directory)

window.mainloop()
