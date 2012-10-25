import gtk

def display(pixbuf):
    i = gtk.Image()
    i.set_from_pixbuf(pixbuf)
    i.show_all()

    w = gtk.Dialog()
    v = w.vbox
    v.pack_start(i)

    w.run()
    w.destroy()

#colormap = gtk.gdk.colormap_get_system()
#pixmap = gtk.gdk.Window(None, 45, 61, gtk.gdk.WINDOW_CHILD, gtk.gdk.BUTTON_PRESS_MASK,
#                        gtk.gdk.INPUT_OUTPUT)
pixbuf = gtk.gdk.pixbuf_new_from_file("/home/icarito/Proyectos/tzolkin/images/orig/13b.png")
pixbuf2 = gtk.gdk.pixbuf_new_from_file("/home/icarito/Proyectos/tzolkin/images/tonos/tono2.png")
pixbuf_end = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, True, 8, 45, 61)

pixbuf.copy_area(0,0,45,41, pixbuf_end, 0, 20)
pixbuf2.copy_area(0,0,45,20, pixbuf_end, 0, 0)
#pixmap.set_colormap(colormap)

#_,mask = pixbuf.render_pixmap_and_mask()

#gc = pixmap.new_gc()

#pixmap = gtk.gdk.Pixmap(gtk.Window(), 45, 61, 8)
#pixmap.draw_pixbuf(None, pixbuf, 0, 0, 0, 0, -1, -1, gtk.gdk.RGB_DITHER_NONE)
#pixmap.draw_pixbuf(None, pixbuf2, 0, 0, 0, 21, -1, -1, gtk.gdk.RGB_DITHER_NONE)

#pixbuf_end = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, True, 8, 45, 61)
#pixbuf_end.get_from_drawable(pixmap, colormap, 0, 0, 0, 0, -1, -1)
display(pixbuf_end)

