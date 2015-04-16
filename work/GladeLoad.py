# -*- coding: utf-8 -*-
from gi.repository import Gtk,Pango
from sendemail import *
from receiveemail import *

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

        toolbar.insert(Gtk.SeparatorToolItem(), 1)

        button_add = Gtk.ToolButton.new_from_stock(Gtk.STOCK_ADD)
        button_add.connect("clicked", self.on_add_button_clicked)
        toolbar.insert(button_add, 2)

        button_remove = Gtk.ToolButton.new_from_stock(Gtk.STOCK_REMOVE)
        button_remove.connect("clicked", self.on_remove_button_clicked)
        toolbar.insert(button_remove, 3)

        toolbar.insert(Gtk.SeparatorToolItem(), 4)

        #button_search = Gtk.ToolButton.new_from_stock(Gtk.STOCK_FIND)
        #button_search.connect("clicked", self.on_search_clicked)
        #toolbar.insert(button_search, 1)

    def TreeView_account(self):
        '''
        show the account list
        '''
        #retrieve part object
        self.treeview_account = self.mainloader.treeview_account
        scrolledwindow2 = self.mainloader.scrolledwindow2

        #Creating the ListStore model, datas are from account file
        self.account_model = Gtk.ListStore(str)
        #密码可加密处理
        fh = open('./Accounts.txt')
        for line in fh.readlines():
            username = line.split(':',1)
            if username[0] == "account":
                checkname = username[1].strip()
                self.account_model.append([checkname])

        fh.close()

        #Sets the model for TreeView
        self.treeview_account.set_model(self.account_model)

        for i, ColumnTitle in enumerate(["Account"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(ColumnTitle, renderer, text=i)
            self.treeview_account.append_column(column)

        scrolledwindow2.add(self.treeview_account)

        #add selection
        select = self.treeview_account.get_selection()
        select.connect("changed", self.on_account_selection_changed)

    def TreeView_maillist(self):
        '''
        show the maillist
        '''
        #retrieve part object
        self.treeview_maillist = self.mainloader.treeview_maillist
        scrolledwindow1 = self.mainloader.scrolledwindow1

        #Creating the ListStore model
        self.maillist_model = Gtk.ListStore(str)
        '''
        self.model.append(["Benjamin", 12])
        self.model.append(["Charles", 14])
        self.model.append(["alfred", 11])
        self.model.append(["Alfred", 12])
        self.model.append(["David", 20])
        self.model.append(["charles", 17])
        self.model.append(["david", 12])
        self.model.append(["benjamin", 13])
        '''
        #Sets the model for TreeView
        self.treeview_maillist.set_model(self.maillist_model)

        for i, ColumnTitle in enumerate(["Mail List"]):
            renderer = Gtk.CellRendererText()
            renderer.props.wrap_mode = Pango.WrapMode.WORD
            column = Gtk.TreeViewColumn(ColumnTitle, renderer, text=i)
            self.treeview_maillist.append_column(column)

        scrolledwindow1.add(self.treeview_maillist)

        #add selection
        select = self.treeview_maillist.get_selection()
        select.connect("changed", self.on_maillist_selection_changed)

    def Text1(self, message):
        '''
        message represent an email, details in receivemail module
        contain 4 parts:
            message[0]:subject
            message[1]:sender
            message[2]:receiverlist
            message[3]:content
        '''
        self.textview_mailcontent = self.mainloader.textview_mailcontent
        scrolledwindow = self.mainloader.scrolledwindow
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)

        #self.textview_mailcontent.set_text
        self.textbuffer = self.textview_mailcontent.get_buffer()
        str = ''.join(["Subject:" , message[0] , "\n" ,
        "Sender:" , message[1] , "\n" ,
        "Content:\n" , message[3] , "\n"])

        self.textbuffer.set_text(str)
        self.textview_mailcontent.set_editable(False)

    def show_subwindow(self):
        #show subview
        self.Toolbar_subwindow()
        self.subloader.window1.show_all()

    def Toolbar_subwindow(self):
        #show subview
        toolbar = self.subloader.toolbar
        comboboxtext = self.subloader.comboboxtext
        comboboxtext.set_entry_text_column(0)
        #
        comboboxtext.connect("changed", self.on_currency_combo_changed)
        fh = open('./Accounts.txt')
        for line in fh.readlines():
            username = line.split(':',1)
            if username[0] == "account":
                checkname = username[1].strip()
                comboboxtext.append_text(checkname)
        fh.close()
        #设置一个默认的account
        comboboxtext.set_active(0)
        self.sender = comboboxtext.get_active_text()

        button_send = Gtk.ToolButton.new(None, "Send Email")
        button_send.connect("clicked", self.on_send_button_clicked)
        toolbar.insert(button_send, 0)
        toolbar.insert(Gtk.SeparatorToolItem(), 1)
        '''
        currencies = ["Euro", "US Dollars", "British Pound", "Japanese Yen",
                        "Russian Ruble", "Mexican peso", "Swiss franc"]
        comboboxtext.set_entry_text_column(0)
        for currency in currencies:
            comboboxtext.append_text(currency)
        '''

    def show_message_dialog(self, widget, str):
        '''
        used for showing send result,and all warnings
        '''
        dialog = Gtk.Dialog("Message", widget)#self.subloader.window1)
        dialog.set_default_size(250, 30)
        label = Gtk.Label()
        label.set_markup(" <big> "+ str +"</big> ")
        box = dialog.get_content_area()
        box.add(label)
        dialog.show_all()
        dialog.run()

        dialog.destroy()

    def create_account_dialog(self, widget):

        dialog = Gtk.Dialog("新建账号", self.mainloader.window1, 0,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_OK, Gtk.ResponseType.OK))
        dialog.set_default_size(350, 200)

        box = dialog.get_content_area()
        label_addr = Gtk.Label("E-mail 地址")
        entry_addr = Gtk.Entry()
        label_pass = Gtk.Label("密码")
        entry_pass = Gtk.Entry()
        entry_pass.set_visibility(False)

        table = Gtk.Table(5,5,True)
        box.add(table)
        table.attach(label_addr, 1, 2, 1, 2)
        table.attach(entry_addr, 2, 4, 1, 2)
        table.attach(label_pass, 1, 2, 4, 5)
        table.attach(entry_pass, 2, 4, 4, 5)

        dialog.show_all()
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            addrbuffer = entry_addr.get_buffer()
            address = addrbuffer.get_text()
            passbuffer = entry_pass.get_buffer()
            password = passbuffer.get_text()

            if not check_username(address):#False means exist
                self.show_message_dialog(self.mainloader.window1, "这个账号已存在！")
            else:#True means not exist, do verification and save it
                #验证邮箱
                if not email_verification(address, password):
                    self.show_message_dialog(self.mainloader.window1, "该账号无效！")
                else:
                    save_an_account(address,password)
                    # refresh account in treeview
                    self.account_model.append([address])
                    self.treeview_account.set_model(self.account_model)

            print("The OK button was clicked")

        elif response == Gtk.ResponseType.CANCEL:
            print("The Cancel button was clicked")

        dialog.destroy()

    def remove_account_dialog(self, widget):
        dialog = Gtk.Dialog("删除账户", self.mainloader.window1, 0,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_OK, Gtk.ResponseType.OK))
        dialog.set_default_size(350, 200)

        box = dialog.get_content_area()
        label_remove = Gtk.Label("请输入删除E-mail 地址")

        label_addr = Gtk.Label("E-mail 地址")
        entry_addr = Gtk.Entry()

        table = Gtk.Table(5,5,True)
        box.add(table)
        table.attach(label_remove, 1, 4, 1, 2)
        table.attach(label_addr, 1, 2, 3, 4)
        table.attach(entry_addr, 2, 4, 3, 4)
        dialog.show_all()

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            addrbuffer = entry_addr.get_buffer()
            address = addrbuffer.get_text()
            remove_an_account(address)
            #refresh account in treeview
            treeiter = self.account_model.get_iter_first()
            while treeiter != None:
                if address == self.account_model[treeiter][0]:
                    self.account_model.remove(treeiter)
                treeiter = self.account_model.iter_next(treeiter)

            self.treeview_account.set_model(self.account_model)
        dialog.destroy()
    '''
    followed control part
    '''
    def on_add_button_clicked(self, widget):
        self.create_account_dialog(self)
        print "You will add a new account!"

    def on_remove_button_clicked(self, widget):
        self.remove_account_dialog(self)
        print "You will remove an account!"


    def on_write_button_clicked(self, widget):
        #Load glade resourse and show the subwindow
        self.subloader = GtkLoader("./send.glade")
        self.subloader.window1.connect("delete-event",
                                       self.subloader.window1.destroy)
        self.show_subwindow()

    def on_send_button_clicked(self, widget):
        '''
        this function works when "send email" button is pressed.Perform the
         following actions:
        1.get entry and text content,which are the receiver(s) and body of email;
        2.get sender and create an object of class Account;
        3.call send_email in another module and send it.
        :param widget:
        :return:
        '''
        print ("send an email!")
        #get entry and text content,which are the receiver(s) and body of email
        entry_rcv = self.subloader.entry_rcv
        entry_sub = self.subloader.entry_sub
        textview_content = self.subloader.textview_content

        receiverbuffer = entry_rcv.get_buffer()
        receiverlist = receiverbuffer.get_text().split(',')

        subjectbuffer = entry_sub.get_buffer()
        subject = subjectbuffer.get_text()

        contentbuffer = textview_content.get_buffer()
        bounds = contentbuffer.get_bounds()
        start, end = bounds
        content = contentbuffer.get_text(start, end, False)

        #get sender, create an object of class Account
        senderAccount = Account(self.sender)
        #call send func
        rst = email_send(senderAccount, receiverlist, subject, content)
        del senderAccount
        if rst:
            self.show_message_dialog(self.subloader.window1, "发送成功!")
        else:
            self.show_message_dialog(self.subloader.window1, "发送失败, 请核对收件人信息!")

        self.subloader.window1.destroy()



    def on_currency_combo_changed(self, combo):
        '''
        set sender from combobox
        :param combo:
        :return:
        '''
        self.sender = combo.get_active_text()
        if self.sender != None:
            print("sender is : %s" % self.sender)

    def on_account_selection_changed(self, selection):
        '''
        1.create an account, get his email_list with email_get method
        2.refresh the sender, subject of email_list in treeview
        :param selection:
        :return:
        '''
        model, treeiter = selection.get_selected()
        print "Please show the received emails of", model[treeiter][0]

        receiveAccount = Account(model[treeiter][0])
        self.maillist = email_get(receiveAccount)


        self.maillist_model.clear()
        for message in self.maillist:#get one envelope
            #order the subject and sender
            #if len(message[0])>40
            self.maillist_model.append([message[0] + '\n' + message[1]])
        self.treeview_maillist.set_model(self.maillist_model)

        #del maillist

    def on_maillist_selection_changed(self, selection):
        treemodel, treepath = selection.get_selected_rows()
        print "Please show the mail index:", treepath[0]
        #type-transfer,TreePath-str-int
        select_message = int(treepath[0].to_string())
        #select message content
        self.Text1(self.maillist[select_message])


        pass

if __name__ == "__main__":
    win = Display()
    win.show()

    Gtk.main()
