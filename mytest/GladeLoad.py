from gi.repository import Gtk


'''
xml = Gtk.glade.XML('ui.glade')
widget = xml.get_widget('window1')
xml.autoconnect({
  'some_handler': some_handler
})
'''
class GtkLoader(Gtk.Builder):
    
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("../work/ui.glade")
        self.window = self.builder.get_object("window1")
        self.window.show_all()
        

    def some_handler(widget):
        print ("enter some_handler function!")
        pass

win = GtkLoader()

Gtk.main()
