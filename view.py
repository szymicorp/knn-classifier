from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import rc
from model import column


class View:

    def __init__(self, master=None):
        self.master = master
        self.figure = None
        self.canvas = None
        self.labels = {}
        self.entries = {}
        self.buttons = {}
        self.createview()

    def createview(self):
        self.master.title("K-NN Classifier")
        self.master.geometry("400x800")

        self.create_label("Train set path:", row=0, column=0, columnspan=1, pady=10)
        self.create_label("Test set path:", row=0, column=1, columnspan=1, pady=10)
        self.create_label("Column 1 number", row=4, column=0)
        self.create_label("Column 2 number", row=5, column=0)
        self.create_label("KNN Classification, k:", row=8, column=0)
        self.create_label("Classify data (csv) :", row=11, column=0)
        self.create_label(row=10, columnspan=2, varname="accuracy")
        self.create_label(row=13, columnspan=2, varname="guess")
        self.create_label("Graph", row=15, columnspan=2)

        self.create_entry(1, 0, "trainpath")
        self.create_entry(1, 1, "testpath")
        self.create_entry(4, 1, "column1")
        self.create_entry(5, 1, "column2")
        self.create_entry(8, 1, "kval")
        self.create_entry(11, 1, "inputdata")

        self.create_button("Load data", row=2, columnspan=2, varname="read")
        self.create_button("Draw graph", row=6, columnspan=2, varname="graph")
        self.create_button("Classify test data", row=9, varname="knn")
        self.create_button("Accuracy(k) graph", row=9, column=1, varname="accuracy")
        self.create_button("Classify input", row=12, columnspan=2, varname="classify")

        self.create_separator(3, 2, pady=20)
        self.create_separator(7, 2, pady=20)
        self.create_separator(14, 2, pady=20)

        font = {'family': 'Arial',
                'weight': 'bold',
                'size': 6}

        rc('font', **font)

        self.create()

    def create_label(self, text="", textvar=None, row=0, column=0, columnspan=1, pady=0, varname=""):
        if varname == "":
            varname = text
        self.labels[varname] = Label(master=self.master, text=text, textvariable=textvar)
        self.labels[varname].grid(row=row, column=column, columnspan=columnspan, pady=pady)

    def create_entry(self, row, column, varname):
        self.entries[varname] = Entry(self.master)
        self.entries[varname].grid(row=row, column=column)

    def create_button(self, text, row=0, column=0, columnspan=1, varname=""):
        if varname == "":
            varname = text
        self.buttons[varname] = Button(self.master, text=text)
        self.buttons[varname].grid(row=row, column=column, columnspan=columnspan)

    def create_separator(self, row, columnspan, orient="horizontal", pady=0):
        ttk.Separator(self.master, orient=orient).grid(row=row, columnspan=columnspan, sticky="ew", pady=pady)

    def set_command(self, varname, command):
        self.buttons[varname]["command"] = command

    def get_label(self, varname):
        return self.labels[varname]

    def get_entry(self, varname):
        return self.entries[varname]

    def create(self):
        self.figure = Figure(figsize=(4, 3))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)

    def clear(self):
        self.canvas.get_tk_widget().destroy()
        self.create()

    def scatter_graph(self, x, y, colors, cmap):
        self.clear()

        a = self.figure.add_subplot(111)
        a.scatter(x, y, c=colors, cmap=cmap)

        self.canvas.get_tk_widget().grid(row=16, column=0, columnspan=2)
        self.canvas.draw()

    def plot_graph(self, x, y):
        self.clear()

        a = self.figure.add_subplot(111)
        a.plot(x, y)

        self.canvas.get_tk_widget().grid(row=16, column=0, columnspan=2)
        self.canvas.draw()