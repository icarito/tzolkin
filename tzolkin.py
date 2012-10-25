#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pygtk, glib
import gobject
pygtk.require('2.0')
import gtk
import pynotify
pynotify.init('Tzolkin')

import webbrowser
from sincronario import *
from datetime import date


def kin_pixbuf(sello, tono):
    img_sello = gtk.gdk.pixbuf_new_from_file('images/orig/' +
                                                str(sello) + 'b.png')
    img_tono = gtk.gdk.pixbuf_new_from_file('images/tonos/tono' +
                                                str(tono) + '.png')
    img_kin = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, True, 8, 45, 61)

    img_sello.copy_area(0,0,45,41, img_kin, 0, 20)
    img_tono.copy_area(0,0,45,20, img_kin, 0, 0)

    return img_kin

class TzolkinTray:

    def __init__(self):
        #midnight = datetime.now().replace(hour=23, minute=59, second=59, microsecond=999)
        #delta = midnight - datetime.now()
        #seconds_to_midnight = delta.seconds
        self.midnight_timer = gobject.timeout_add(1000*5, self.set_day)
        #self.midnight_timer = gobject.timeout_add(1000 * seconds_to_midnight, self.set_day)

        self.fecha = date.today()
        self.kin_string = "Kin %s\n%s %s %s" % (str(kin(self.fecha)),
                    sello(self.fecha), tono(self.fecha), raza(self.fecha))

        self.statusIcon = gtk.StatusIcon()
        self.statusIcon.set_from_file("images/%sb.png" %
                                str(sellonum(self.fecha)))

        self.menu = gtk.Menu()
        self.menuItem = gtk.ImageMenuItem(gtk.STOCK_REFRESH)
        self.menuItem.set_label('Umbral Galáctico')
        self.menuItem.connect('activate', self.execute_cb, self.statusIcon)
        self.menu.append(self.menuItem)

        self.menuItem = gtk.MenuItem()
        self.menu.append(self.menuItem)

        self.menuItem = gtk.ImageMenuItem(gtk.STOCK_INFO)
        self.menuItem.set_label('Acerca de Hoy')
        self.menuItem.connect('activate', self.about_today_cb,
                                            self.statusIcon)
        self.menu.append(self.menuItem)

        self.menuItem = gtk.ImageMenuItem(gtk.STOCK_INFO)
        self.menuItem.set_label('Consultar día')
        self.menuItem.connect('activate', self.about_someday_cb,
                                            self.statusIcon)
        self.menu.append(self.menuItem)

        self.menuItem = gtk.ImageMenuItem(gtk.STOCK_INFO)
        self.menuItem.set_label('Oráculo de Hoy')
        self.menuItem.connect('activate', self.show_oracle_cb,
                                            self.statusIcon)
        self.menu.append(self.menuItem)

        self.menuItem = gtk.MenuItem()
        self.menu.append(self.menuItem)

        self.menuItem = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        self.menuItem.set_label('Cerrar')
        self.menuItem.connect('activate', self.quit_cb, self.statusIcon)
        self.menu.append(self.menuItem)

        self.statusIcon.connect('popup-menu', self.popup_menu_cb, self.menu)
        self.statusIcon.connect('activate', self.hover_cb, self.menu)

    def set_day(self):
        #from random import random
        #self.fecha = date.today().replace(day=int(random()*30+1))
        #self.fecha = datetime.now().replace(hour=23, minute=59, second=59, microsecond=999) + timedelta(seconds=30)
        #self.fecha = date.now() + timedelta(seconds=30)
        self.fecha = date.today()
        self.kin_string = "Kin %s\n%s" % (str(kin(self.fecha)),
                                          firma(self.fecha))

        self.statusIcon.set_from_file("images/%sb.png" %
                                str(sellonum(self.fecha)))

        return True

    def execute_cb(self, widget, event, data=None):
        webbrowser.open_new('http://www.13lunas.net/umbralgalacticohoy.htm')

    def quit_cb(self, widget, data=None):
        gtk.main_quit()

    def hover_cb(self, widget, event):
        try:
            self.notification.close()
            need_new_note = False
        except:
            need_new_note = True

        if need_new_note:
            self.notification = pynotify.Notification(firma(self.fecha),
                    'Kin ' + str(kin(self.fecha)))
            self.notification.set_icon_from_pixbuf(
                                    kin_pixbuf(sellonum(self.fecha),
                                                tononum(self.fecha)))
            self.notification.add_action('hoy', 'Energía del día',
                                                    self.about_today_cb)
            self.notification.add_action('oraculo', 'Oráculo',
                                                        self.show_oracle_cb)

            try:
                self.notification.attach_to_status_icon(self.statusIcon)
            except AttributeError:
                pass

            self.notification.show()

    def show_wave_cb(self):
        pass

    def show_oracle_cb(self, widget, event):
        oracle_win = gtk.Dialog('Oráculo')
        vbox = oracle_win.vbox
        tono = tononum(self.fecha)
        tonooculto = 14 - tono
        sello = sellonum(self.fecha)
        fecha = self.fecha

        guia_button = gtk.Image()
        guia_button.set_from_pixbuf(kin_pixbuf(guia(fecha), tono))
        guia_button.set_tooltip_text('Guía')
        vbox.pack_start(guia_button)

        oculto_button = gtk.Image()
        oculto_button.set_from_pixbuf(kin_pixbuf(oculto(fecha), tonooculto))
        oculto_button.set_tooltip_text('Oculto')
        vbox.pack_end(oculto_button)

        hbox = gtk.HBox()
        antipoda_button = gtk.Image()
        antipoda_button.set_from_pixbuf(kin_pixbuf(antipoda(fecha), tono))
        antipoda_button.set_tooltip_text('Antípoda')
        hbox.pack_start(antipoda_button)

        destino_button = gtk.Image()
        destino_button.set_from_pixbuf(kin_pixbuf(sello, tono))
        destino_button.set_tooltip_text('Destino')
        hbox.pack_start(destino_button)

        analogo_button = gtk.Image()
        analogo_button.set_from_pixbuf(kin_pixbuf(analogo(fecha), tono))
        analogo_button.set_tooltip_text('Análogo')
        hbox.pack_end(analogo_button)
        vbox.pack_end(hbox)

        vbox.show_all()

        oracle_win.run()
        oracle_win.destroy()


    def popup_menu_cb(self, widget, event, time, data=None):

        self.menu.show_all()
        self.menu.popup(None, None, gtk.status_icon_position_menu,
                             3, time, self.statusIcon)

    def about_today_cb(self, widget, arg):
        self.show_about_dialog(self.fecha)

    def about_someday_cb(self, widget, arg):
        cal_dialog = gtk.Dialog()
        vbox = cal_dialog.vbox
        cal = gtk.Calendar()
        vbox.pack_start(cal)
        vbox.show_all()

        cal_dialog.add_button('Aceptar', True)
        ok = cal_dialog.run()
        if ok:
            y, m, d = cal.get_date()
            fecha = date(y, m+1, d)
            self.show_about_dialog(fecha)
        cal_dialog.destroy()

    def show_about_dialog(self, fecha):
        about_dialog = gtk.AboutDialog()

        about_dialog.set_destroy_with_parent(True)

        about_dialog.set_name("Kin %s\n%s" % (str(kin(fecha)),
                                          firma(fecha)))
        about_dialog.set_title('Energía del día')
        about_dialog.set_comments(afirmacion(fecha))

        logo = kin_pixbuf(sellonum(fecha), tononum(fecha))
        about_dialog.set_logo(logo)

        about_dialog.run()
        about_dialog.destroy()

if __name__ == "__main__":
    tzolkin = TzolkinTray()
    gtk.main()

