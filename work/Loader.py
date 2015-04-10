from gi.repository import Gtk

class Loader(object):
    '''
    implement ui autoload and properties creation.
    '''
    def __init__(self, filename):
        '''
        Constructor define private virtual function _get_object
        '''
        self._get_object = None
        
    def __getattr__(self, name):   
        #internal attribute should be start with "_"
        obj = self._get_object(name[1:])
        setattr(self, "_" + name[1:], obj)
        return obj
    
    def _get_object(self, str):
        print "_get_object not defined!"
        return
        
        
class GtkLoader(Loader):
    '''
        autoload glade file
    ''' 
    def __init__(self, filename):
        from gi.repository import Gtk
        self.builder = Gtk.Builder()
        self.builder.add_from_file(filename)
        self._get_object = self.builder.get_object
        self.builder.connect_signals(self)


gtkld = GtkLoader("./ui.glade")
gtkld._window1.connect("delete-event", Gtk.main_quit)
gtkld._window1.show_all()
Gtk.main()
