#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

import webbrowser
from sincronario import *
from datetime import date

class TzolkinTray:
    def __init__(self):
        self.fecha = date.today()

        self.statusIcon = gtk.StatusIcon()
        self.statusIcon.set_from_file("images/%sb.gif" % str(kin(self.fecha)%20))
        self.statusIcon.set_visible(True)
        #self.statusIcon.set_tooltip("Consulta el Tzolkin")

        self.menu = gtk.Menu()
        self.menuItem = gtk.ImageMenuItem(gtk.STOCK_REFRESH)
        self.menuItem.set_label('Umbral Galáctico')
        self.menuItem.connect('activate', self.execute_cb, self.statusIcon)
        self.menu.append(self.menuItem)

        self.menuItem = gtk.ImageMenuItem(gtk.STOCK_INFO)
        self.menuItem.set_label('Energía de Hoy')
        self.menuItem.connect('activate', self.show_about_dialog, self.statusIcon)
        self.menu.append(self.menuItem)

        self.menuItem = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        self.menuItem.set_label('Adios')
        self.menuItem.connect('activate', self.quit_cb, self.statusIcon)
        self.menu.append(self.menuItem)

        #self.statusIcon.connect('popup-menu', self.popup_menu_cb, self.menu)
        self.statusIcon.connect('activate', self.activate_cb, self.menu)

        self.statusIcon.set_visible(1)

    def execute_cb(self, widget, event, data=None):
        webbrowser.open_new('www.13lunas.net')

    def quit_cb(self, widget, data=None):
        gtk.main_quit()

    def popup_menu_cb(self, widget, button, time, data=None):
        if data:
            data.show_all()
            data.popup(None, None, gtk.status_icon_position_menu,
                                 button, time, data=self.statusIcon)

    def activate_cb(self, widget, button, data=None):
        button.show_all()
        time = gtk.current_event_time
        button.popup(None, None, gtk.status_icon_position_menu,
                             button, time, data=self.statusIcon)

    def show_about_dialog(self, widget, arg):
        fecha = self.fecha
        about_dialog = gtk.AboutDialog()

        about_dialog.set_destroy_with_parent(True)

        kin_string = "Kin %s %s %s" % (str(kin(fecha)), sello(fecha),
                    tono(fecha)) + raza(fecha)
        about_dialog.set_name(kin_string)
        about_dialog.set_comments('aqui va algo')
        about_dialog.set_copyright('basado en el trabajo de José Argüelles - Valum Votan Kin 11')
        about_dialog.set_logo(gtk.gdk.pixbuf_new_from_file("images/%sb.gif" % str(kin(fecha)%20)))

        about_dialog.run()
        about_dialog.destroy()

if __name__ == "__main__":
    tzolkin = TzolkinTray()
    gtk.main()

