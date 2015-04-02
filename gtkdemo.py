# -*- coding: utf-8
from gi.repository import Gtk

class MyWindow(object):
        def __init__(self,title,width,height):
                self.window = Gtk.Window()
                self.window.set_title(title)
                self.window.set_default_size(width,height)
                self.window.connect("destroy",lambda q:Gtk.main_quit())
                self.switch = Gtk.Switch()

                self.window.add(self.switch)
                self.window.show_all()


        def main(self):
                Gtk.main()

if __name__ == '__main__':
        gui=MyWindow('myninewindow',600,400)
        gui.main()
