# Created by: Julie Nguyen
# Created on: Sept 2017
# Created for: ICS3U
# Daily Assignment - Unit0-03
# This program is the Hello, World program, but as a GUI and with a button

import ui

def hello_world_touch_up_inside(sender):
    #print ('Hello, World!')
    view['hello_world_label'].text = ("Hello, World!")

view = ui.load_view()
view.present('sheet')
