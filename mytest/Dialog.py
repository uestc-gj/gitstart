from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="TextView Example")

        self.set_default_size(300, 200)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)
        
        button = Gtk.Button("cliked me")
        button.connect("clicked", self.create_a_normal_dialog,"Good morning")
        hbox.pack_start(button, True, True, 0)

    def on_clicked_me(self, widget):
        '''
        type:
          GTK_MESSAGE_INFO(Gtk.MessageType.INFO)
          GTK_MESSAGE_WARNING
          GTK_MESSAGE_QUESTION
          GTK_MESSAGE_ERROR
        buttontype:
            GTK_BUTTON_OK
            GTK_BUTTON_CLOSE
            GTK_BUTTON_CANCEL
            GTK_BUTTON_YES_NO
            GTK_BUTTON_OK_CANCEL
            GTK_BUTTON_NONE
        '''
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
            Gtk.ButtonsType.OK_CANCEL, "This is an ERROR MessageDialog")
        dialog.format_secondary_text(
            "And this is the secondary text that explains things.")
        dialog.run()
        print("ERROR dialog closed")

        dialog.destroy()
        
    def create_a_normal_dialog(self, widget, str):
        dialog = Gtk.Dialog("Message", self)
        dialog.set_default_size(250, 30)
        label = Gtk.Label()
        label.set_markup(" <big> "+ str +"</big> ")
        box = dialog.get_content_area()
        box.add(label)
        dialog.show_all()
        dialog.run()

        dialog.destroy()

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
