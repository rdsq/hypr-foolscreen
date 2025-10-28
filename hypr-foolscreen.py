#!/usr/bin/env python3
import gi, sys, os
gi.require_version("Gtk", "3.0")

try:
    gi.require_version("GtkLayerShell", '0.1')
except ValueError as e:
    print('Seems like you have to install gtk-layer-shell')
    print('See packages here:')
    print('https://github.com/wmww/gtk-layer-shell?tab=readme-ov-file#distro-packages')
    sys.exit(1)

from gi.repository import Gtk, GtkLayerShell

def do_the_thing(internal, client):
    os.system(f'hyprctl dispatch fullscreenstate {internal} {client}')
    Gtk.main_quit()

def connect_button(button, internal: int, client: int):
    button.connect("clicked", lambda _: do_the_thing(internal, client))

class HyprFoolscreenWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="HyprFoolscreen")
        table = Gtk.Table(n_rows=2, n_columns=2)
        self.add(table)

        # Create options with values accepted by hyprctl
        # https://wiki.hypr.land/Configuring/Dispatchers/#fullscreenstate
        button1 = Gtk.Button(label="Normal")
        connect_button(button1, 0, 0)
        button2 = Gtk.Button(label="App thinks: fullscreen\nReality: tiled")
        connect_button(button2, 0, 2)
        button3 = Gtk.Button(label="App thinks: tiled\nReality: fullscreen")
        connect_button(button3, 2, 0)
        button4 = Gtk.Button(label="Fullscreen")
        connect_button(button4, 2, 2)
        button5 = Gtk.Button(label="Cancel")
        button5.connect("clicked", Gtk.main_quit)

        # Probably (x, y, x up to, y up to)
        table.attach(button1, 0, 1, 0, 1)
        table.attach(button2, 1, 2, 0, 1)
        table.attach(button3, 0, 1, 1, 2)
        table.attach(button4, 1, 2, 1, 2)
        table.attach(button5, 0, 2, 2, 3)

win = HyprFoolscreenWindow()
GtkLayerShell.init_for_window(win)
# win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
