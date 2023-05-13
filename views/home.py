from tkinter import Frame, Label, Button, Entry


class HomeView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Labels start")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        print('single frame')


        self.btn1 = Button(self, text="Button1")
        self.btn1.grid(row=2, column=0, padx=10, pady=10)

        self.btn2 = Button(self, text="Button2")
        self.btn2.grid(row=3, column=0, padx=10, pady=10)

