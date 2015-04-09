from gi.repository import Gtk, Pango


class MyDialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "MY DIALOG", parent, 0,
                            buttons=(
                                Gtk.STOCK_OK, Gtk.ResponseType.OK,
                                Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        self.show_all()


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="TextView Example")

        self.set_default_size(300, 200)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)
        
        button = Gtk.Button("cliked me")
        button.connect("clicked", self.on_clicked_me)
        hbox.pack_start(button, True, True, 0)

    def on_clicked_me(self, widget):
        dialog = MyDialog(self)
        response = dialog.run()
        if response == Gtk.ResponseType.CANCEL:
            print("The Cancel button was clicked")
            dialog.destroy()
        elif response == Gtk.ResponseType.OK:
            print("The Dialog was hidden")
            dialog.hide()

        


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
