from tkinter import *
from tkinter import font as f
from tkinter import ttk
from tkinter import messagebox
from data import Selector

BLUE = "#3584e4"
WHITE = "#ffffff"
GRAY = "#9a9996"
BLACK = "#000000"
GREEN = "#33d17a"
FONT_NAME = "Cantarell"


class AppInterface:

    def __init__(self, selector: Selector):
        self.selector = selector
        self.root = Tk()
        self.root.title("Phineas")
        self.root.geometry("480x640")
        self.root.config(padx=50, pady=50, bg=GRAY)

        HEADING1 = f.Font(family=FONT_NAME, weight="bold", size=24)
        HEADING2 = f.Font(family=FONT_NAME, weight="bold", size=12)

        self.canvas = Canvas(
            self.root,
            width=350,
            height=300,
            bg=WHITE,
            highlightthickness=1)
        self.activity_text = self.canvas.create_text(
            175,
            125,
            width=280,
            text="What should we do today?",
            fill=BLACK,
            font=HEADING1)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        # Activity label and combobox
        self.activity_lbl = Label(
            self.root,
            text="Activity Type",
            justify="center",
            font=HEADING2,
            bg=GRAY)
        self.activity_lbl.grid(row=2, column=0, padx=10, pady=5)
        self.selected_activity = StringVar()
        self.activity_cb = ttk.Combobox(
            self.root,
            width=15,
            textvariable=self.selected_activity)
        self.activity_cb["values"] = [
            "random",
            "education",
            "recreational",
            "social",
            "diy",
            "charity",
            "cooking",
            "relaxation",
            "music",
            "busywork"]
        self.activity_cb["state"] = "readonly"
        self.activity_cb.grid(row=3, column=0, padx=10, pady=5)

        # Participants label and spinbox
        self.participants_lbl = Label(
            self.root,
            text="Number of Participants",
            justify="center",
            font=HEADING2,
            bg=GRAY)
        self.participants_lbl.grid(row=2, column=1, padx=10, pady=5)
        self.num_participants = StringVar(value=1)
        self.participants_spinbox = ttk.Spinbox(
            self.root,
            from_=1,
            to=5,
            textvariable=self.num_participants,
            wrap=True,
            width=10
        )
        self.participants_spinbox["state"] = "readonly"
        self.participants_spinbox.grid(row=3, column=1, padx=10, pady=5)

        # Price label and spinbox
        self.price_lbl = Label(
            self.root,
            text="Price Range:\nFree(0)-Expensive(10)",
            justify="center",
            font=HEADING2,
            bg=GRAY)
        self.price_lbl.grid(row=4, column=0, padx=5)
        self.price_value = StringVar(value=0)
        self.price_spinbox = ttk.Spinbox(
            self.root,
            from_=0,
            to=10,
            textvariable=self.price_value,
            wrap=False,
            width=10)
        self.price_spinbox.grid(row=5, column=0, padx=10, pady=5)

        # Accessibility label and spinbox
        self.access_lbl = Label(
            self.root,
            text="Ease of Doing",
            justify="center",
            font=HEADING2,
            bg=GRAY)
        self.access_lbl.grid(row=4, column=1, padx=10, pady=5)

        self.access_value = StringVar(value=0)
        self.access_spinbox = ttk.Spinbox(
            self.root,
            from_=0,
            to=100,
            textvariable=self.access_value,
            wrap=True,
            width=10)
        self.access_spinbox.grid(row=5, column=1, padx=5, pady=5)

        self.suggest_btn = Button(
            self.root,
            text="Get a Suggestion\n(using selections)",
            justify="center",
            font=HEADING2,
            width=15,
            bg=GREEN,
            highlightthickness=0,
            command=self.suggest_btn_pressed)
        self.suggest_btn.grid(row=6, column=0, padx=10, pady=20)

        self.random_btn = Button(
            self.root,
            text="Surprise me!\n(completely random)",
            justify="center",
            font=HEADING2,
            width=15,
            bg=BLUE,
            highlightthickness=0,
            command=self.rand_btn_pressed)
        self.random_btn.grid(row=6, column=1, padx=10, pady=20)

        self.root.mainloop()

    def rand_btn_pressed(self):
        activity = self.selector.get_rand_activity()
        self.change_text(activity)

    def suggest_btn_pressed(self):
        activity_type = self.selected_activity.get()
        participants = self.num_participants.get()
        price = str(float(self.price_value.get()) / 10)
        accessibility = str(float(self.access_value.get()) / 100)
        if activity_type == "":
            messagebox.showinfo(
                title="Error",
                message="You forgot to select an activity type!")
            return
        elif activity_type == "random":
            activity_type = str(self.selector.get_rand_type())
        data = self.selector.get_suggestion(
            activity_type,
            participants,
            price,
            accessibility,
        )
        self.change_text(data)

    def change_text(self, data):
        self.canvas.itemconfig(self.activity_text, text=data)
