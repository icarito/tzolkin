#!/usr/bin/env python

# example menu.py

import pygtk
pygtk.require('2.0')
import gtk

class MenuExample:
    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(200, 100)
        window.set_title("GTK Menu Test")
        window.connect("delete_event", lambda w,e: gtk.main_quit())

        # Init the menu-widget, and remember -- never
        # show() the menu widget!! 
        # This is the menu that holds the menu items, the one that
        # will pop up when you click on the "Root Menu" in the app
        menu = gtk.Menu()

        ### MODIFIED PART!! ###
        item = gtk.MenuItem()

        button = gtk.ProgressBar()
        button.pulse()
        button.show()

        item.add(button)
        item.show()

        menu.append(item)
        #### END MODIFIED PART ####

        # This is the root menu, and will be the label
        # displayed on the menu bar.  There won't be a signal handler attached,
        # as it only pops up the rest of the menu when pressed.
        root_menu = gtk.MenuItem("Root Menu")

        root_menu.show()

        # Now we specify that we want our newly created "menu" to be the
        # menu for the "root menu"
        root_menu.set_submenu(menu)

        # A vbox to put a menu and a button in:
        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.show()

        # Create a menu-bar to hold the menus and add it to our main window
        menu_bar = gtk.MenuBar()
        vbox.pack_start(menu_bar, False, False, 2)
        menu_bar.show()

        # Create a button to which to attach menu as a popup
        button = gtk.Button("press me")
        button.connect_object("event", self.button_press, menu)
        vbox.pack_end(button, True, True, 2)
        button.show()

        # And finally we append the menu-item to the menu-bar -- this is the
        # "root" menu-item I have been raving about =)
        menu_bar.append (root_menu)

        # always display the window as the last step so it all splashes on
        # the screen at once.
        window.show()

    # Respond to a button-press by posting a menu passed in as widget.
    #
    # Note that the "widget" argument is the menu being posted, NOT
    # the button that was pressed.
    def button_press(self, widget, event):
        if event.type == gtk.gdk.BUTTON_PRESS:
            widget.popup(None, None, None, event.button, event.time)
            color = gtk.gdk.rgb_get_colormap().alloc_color('black')
            ebTooltip = gtk.EventBox()
            btnTooltip = gtk.Button("Close")
            ebTooltip.add(btnTooltip)
            ebTooltip.modify_bg(gtk.STATE_NORMAL, color)

            ebTooltip.show()
            # Tell calling code that we have handled this event the buck
            # stops here.
            return True
        # Tell calling code that we have not handled this event pass it on.
        return False

    # Print a string when a menu item is selected
    def menuitem_response(self, widget, string):
        print "%s" % string

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    MenuExample()
    main()
