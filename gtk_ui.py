import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from data import Selector

css_provider = Gtk.CssProvider()
css_provider.load_from_path("gtk.css")
style_context = Gtk.StyleContext()
style_context.add_provider_for_screen(
    Gdk.Screen.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Phineas")

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.add(self.box)

        self.label = Gtk.Label(label="This is a normal label")
        self.label.set_line_wrap(True)
        self.label.set_justify(Gtk.Justification.FILL)
        self.label.set_max_width_chars(32)
        self.box.pack_start(self.label, True, True, 0)

        self.button = Gtk.Button(label="Ask Again")
        self.button.set_name("action")
        self.button.connect("clicked", self.on_button_clicked)
        # self.add(self.button)
        self.box.pack_start(self.button, True, True, 0)

    @staticmethod
    def on_button_clicked(self):
        activity = Selector.get_rand_activity()
        print(activity)
        label.set_markup(activity)
        # self.label = Gtk.Label(label=activity)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
