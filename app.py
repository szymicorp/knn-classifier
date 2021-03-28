from model import Model
from view import View
from controller import Controller
from tkinter import Tk

class App():
    def __init__(self):
        root = Tk()
        model = Model(root)
        view = View(root)
        controller = Controller(view, model)
        root.mainloop()

app = App()