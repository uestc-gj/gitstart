from gi.repository import Gtk,Pango
from sendemail import *

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
        obj = self._get_object(name)
        return obj
    
    def _get_object(self, str):
        print "_get_object not defined!"
        return
           
class GtkLoader(Loader):
    '''
        autoload glade file
    ''' 
    def __init__(self, filename):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(filename)
        self._get_object = self.builder.get_object
        self.builder.connect_signals(self)

class Display(Gtk.Window):
    '''
    combine all widgets,which have already prepared view & model.This is a place
    for staging these boys
    '''
    def __init__(self):
        #Load glade resourse
        self.mainloader = GtkLoader("./ui.glade")

    def show(self):
        #show subview
        self.TreeView_account()
        self.TreeView_maillist()
        self.ToolBar()
        
        self.mainloader.window1.connect("delete-event", Gtk.main_quit)
        self.mainloader.window1.show_all()

    def ToolBar(self):
        #show subview
        toolbar = self.mainloader.toolbar
        box = self.mainloader.box
        #self.grid.attach(toolbar, 0, 0, 3, 1)

        #button_send = Gtk.ToolButton.new(None, "Send Email")
        button_send = Gtk.ToolButton.new_from_stock(Gtk.STOCK_EDIT)
        button_send.connect("clicked", self.on_write_button_clicked)
        toolbar.insert(button_send, 0)

        button_add = Gtk.ToolButton.new_from_stock(Gtk.STOCK_ADD)
        button_add.connect("clicked", self.on_add_button_clicked)
        toolbar.insert(button_add, 1)
       
        #button_search = Gtk.ToolButton.new_from_stock(Gtk.STOCK_FIND)
        #button_search.connect("clicked", self.on_search_clicked)
        #toolbar.insert(button_search, 1)
    
    def TreeView_account(self):
        '''
        show the account list
        '''        
        #retrieve part object
        treeView = self.mainloader.treeview_account
        fixed = self.mainloader.fixed
        
        #Creating the ListStore model, datas are from account file
        self.model = Gtk.ListStore(str)
        #文件处理可以继续优化，密码需要特殊处理
        fh = open('./Accounts.txt')
        for line in fh.readlines():
            username = line.split(':',1)
            if username[0] == "account":
                checkname = username[1].strip()
                self.model.append([checkname])

        fh.close()

        #self.model.append(["916311350@qq.com"])
        #self.model.append(["Charles@sina.cn"])
        #self.model.append(["alfred@163.com"])

        #Sets the model for TreeView
        treeView.set_model(self.model)

        for i, ColumnTitle in enumerate(["Account"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(ColumnTitle, renderer, text=i)
            treeView.append_column(column)

        fixed.add(treeView)

        #add selection
        select = treeView.get_selection()
        select.connect("changed", self.on_account_selection_changed)

    def TreeView_maillist(self):
        '''
        show the maillist
        '''
        #retrieve part object
        treeView = self.mainloader.treeview_maillist
        fixed = self.mainloader.fixed
        
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

        #add selection
        select = treeView.get_selection()
        select.connect("changed", self.on_maillist_selection_changed)
        
    def Text1(self):
        pass

    def show_subwindow(self):
        #show subview
        self.Toolbar_subwindow()
        self.subloader.window1.show_all()

    def Toolbar_subwindow(self):
        #show subview
        toolbar = self.subloader.toolbar
        comboboxtext = self.subloader.comboboxtext

        button_send = Gtk.ToolButton.new(None, "Send Email")
        button_send.connect("clicked", self.on_send_button_clicked)
        toolbar.insert(button_send, 0)
        toolbar.insert(Gtk.SeparatorToolItem(), 1)

        comboboxtext.set_entry_text_column(0)
        comboboxtext.connect("changed", self.on_currency_combo_changed)
        fh = open('./Accounts.txt')
        for line in fh.readlines():
            username = line.split(':',1)
            if username[0] == "account":
                checkname = username[1].strip()
                comboboxtext.append_text(checkname)

        fh.close()
        '''
        currencies = ["Euro", "US Dollars", "British Pound", "Japanese Yen",
                        "Russian Ruble", "Mexican peso", "Swiss franc"]
        comboboxtext.set_entry_text_column(0)
        for currency in currencies:
            comboboxtext.append_text(currency)
        '''


    '''
    followed control part
    '''
    def on_add_button_clicked(self, widget):
        print "You will add a new account!"
    
    def on_write_button_clicked(self, widget):
        #Load glade resourse and show the subwindow
        self.subloader = GtkLoader("./send.glade")
        self.subloader.window1.connect("delete-event",
                                       self.subloader.window1.destroy)
        self.show_subwindow()

    def on_send_button_clicked(self, widget):
        print ("send an email!")

    def on_currency_combo_changed(self, combo):
        sender = combo.get_active_text()
        if sender != None:
            print("sender is : %s" % sender)
    
    def on_account_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        print "Please show the received emails of", model[treeiter][0]

    def on_maillist_selection_changed(self, widget):
        pass

'''        dialog = SearchDialog(self)
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
