from gi.repository import Gtk

class GtkLoader(Gtk.Builder):
    
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./ui.glade")
        self.window = self.builder.get_object("window1")
        self.TreeView_account = self.builder.get_object("treeview_account")
        self.TreeView_maillist = self.builder.get_object("treeview_maillist")
        self.fixed = self.builder.get_object("fixed")
        self.Toolbar = self.builder.get_object("toolbar")
        self.ToolbarBox = self.builder.get_object("box")
  
        #self.window.show_all()

class Display(Gtk.Window):
    '''
    combine all widgets,which have already prepared view & model.This is a place
    for staging these boys
    '''
    def __init__(self):
        #Load glade resourse
        self.loader = GtkLoader()

    def show(self):
        #show subview
        self.TreeView_account()
        self.TreeView_maillist()
        self.ToolBar()
        
        self.loader.window.connect("delete-event", Gtk.main_quit)
        self.loader.window.show_all()

    def ToolBar(self):
        #show subview
        toolbar = self.loader.Toolbar
        box = self.loader.ToolbarBox
        #self.grid.attach(toolbar, 0, 0, 3, 1)

        button_send = Gtk.ToolButton.new(None, "Send Email")
        #button_send.connect("clicked", self.on_send_button_clicked)
        toolbar.insert(button_send, 0)

        #button_search = Gtk.ToolButton.new_from_stock(Gtk.STOCK_FIND)
        #button_search.connect("clicked", self.on_search_clicked)
        #toolbar.insert(button_search, 1)
    
    def TreeView_account(self):
        '''
        show the account list
        '''        
        #retrieve part object
        treeView = self.loader.TreeView_account
        fixed = self.loader.fixed
        
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

        #Sets the model for TreeView
        treeView.set_model(self.model)

        for i, ColumnTitle in enumerate(["Names", "Age"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(ColumnTitle, renderer, text=i)
            treeView.append_column(column)

        fixed.add(treeView)

    def TreeView_maillist(self):
        '''
        show the maillist
        '''
        #retrieve part object
        treeView = self.loader.TreeView_maillist
        fixed = self.loader.fixed
        
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

        #Sets the model for TreeView
        treeView.set_model(self.model)

        for i, ColumnTitle in enumerate(["Names", "Age"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(ColumnTitle, renderer, text=i)
            treeView.append_column(column)

        fixed.add(treeView)

    def Text1(self):
        pass
'''
    def on_send_button_clicked(self):
        dialog = SearchDialog(self)
        response = dialog.run()
		if response == Gtk.ResponseType.OK:
			cursor_mark = self.textbuffer.get_insert()
			start = self.textbuffer.get_iter_at_mark(cursor_mark)
			if start.get_offset() == self.textbuffer.get_char_count():
				start = self.textbuffer.get_start_iter()

			self.search_and_mark(dialog.entry.get_text(), start)

		dialog.destroy()
'''
win = Display()
win.show()

Gtk.main()
