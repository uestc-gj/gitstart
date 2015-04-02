#!/usr/bin/python
# -*- coding: utf-8
from gi.repository import Gtk

class MyWindow( Gtk.Window ):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        label1 = Gtk.Label(label="Hello World", angle=25, halign=Gtk.Align.END)
        Gtk.Window.set_default_size(self,200,200)
        self.button = Gtk.Button(label='cliked me')
        self.button.connect("clicked", self.on_button_clicked)
        #handler_id = widget.connect("event", callback, data)

        self.add(self.button)
    def on_button_clicked(self, widget):
        print ('Hello World!')

win = MyWindow() #Gtk.Window()
#win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
