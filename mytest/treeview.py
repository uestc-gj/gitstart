from gi.repository import Gtk

class Tree(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Treeview Filter Demo")
        self.set_default_size(200,300)
        self.set_border_width(10)
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)
        
        #Creating the ListStore model
        self.model = Gtk.ListStore(str, int)
        self.model.append(["Benjamin", 12])
        self.model.append(["Charles", 14])
        self.model.append(["alfred", 11])
        self.model.append(["Alfred", 12])
        self.model.append(["David", 20])
        self.model.append(["charles", 17])
        self.model.append(["david", 12])
        self.model.append(["benjamin", 13])

        self.treeView = Gtk.TreeView(self.model)
        
        for i, ColumnTitle in enumerate(["Names", "Age"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(ColumnTitle, renderer, text=i)
            self.treeView.append_column(column)

        # retrieve data for the row selected
        self.select = self.treeView.get_selection()
        self.select.connect("changed", self.on_tree_selection_changed)

        #setting up the layout, putting the treeview in a scrollwindow
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        self.scrollable_treelist.add(self.treeView)

        
    def on_tree_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter != None:
            print "You selected", model[treeiter][0]
    

win = Tree()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
