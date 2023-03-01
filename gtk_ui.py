import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from data import Selector


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Phineas")

        self.button = Gtk.Button(label="Ask Again")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    @staticmethod
    def on_button_clicked(self, widget):
        print(Selector.get_rand_activity())


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
