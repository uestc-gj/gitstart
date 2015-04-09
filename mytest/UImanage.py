from gi.repository import Gtk,Gdk

UI_INFO = """
<ui>
  <menubar name='MenuBar'>
    <menu action='FileMenu'>
      <menu action='FileNew'>
        <menuitem action='FileNewStandard' />
        <menuitem action='FileNewFoo' />
        <menuitem action='FileNewGoo' />
      </menu>
      <separator />
      <menuitem action='FileQuit' />
    </menu>
    <menu action='EditMenu'>
      <menuitem action='EditCopy' />
      <menuitem action='EditPaste' />
      <menuitem action='EditSomething' />
    </menu>
    <menu action='ChoicesMenu'>
      <menuitem action='ChoiceOne'/>
      <menuitem action='ChoiceTwo'/>
      <separator />
      <menuitem action='ChoiceThree'/>
    </menu>
    <menu action='AboutMenu'>
      <menuitem action='About'/>
      <separator />
    </menu>
  </menubar>
  <toolbar name='ToolBar'>
    <toolitem action='FileNewStandard' />
    <toolitem action='FileQuit' />
  </toolbar>
  <popup name='PopupMenu'>
    <menuitem action='EditCopy' />
    <menuitem action='EditPaste' />
    <menuitem action='EditSomething' />
  </popup>
</ui>

"""
class MenuExampleWindow(Gtk.Window):
    def __init__(self):
        '''
        #-----action------
        action_group = Gtk.ActionGroup("my_actions")

        self.add_file_menu_actions(action_group)
        self.add_edit_menu_actions(action_group)
        self.add_choices_menu_actions(action_group)
        '''
        Gtk.Window.__init__(self, title="Menu Example")
        self.set_default_size(200, 200)

        #-----uimanager------
        self.uimanager = Gtk.UIManager()
        self.uimanager.add_ui_from_string(UI_INFO)

        # Add the accelerator group to the toplevel window
        accelgroup = self.uimanager.get_accel_group()
        self.add_accel_group(accelgroup)

        #-----box------
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        menubar = self.uimanager.get_widget("/MenuBar")
        toolbar = self.uimanager.get_widget("/ToolBar")
        self.box.pack_start(menubar, False, False, 0)
        self.box.pack_start(toolbar, False, False, 0)

        self.add(self.box)

window = MenuExampleWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
