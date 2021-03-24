import csv
from tkinter import *
from tkinter import ttk
from numpy import arange
from matplotlib import rc
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from knn import KNN


def column(matrix, i):
    return [row[i] for row in matrix]


def encode(name):
    i = 0
    for c in name:
        i += ord(c)
    return i


class Main:

    def __init__(self):
        self.dataset = None
        self.testset = None
        self.colors = None
        self.root = Tk()
        self.root.title("Iris")
        self.root.geometry("420x800")

        Label(master=self.root, text="Train set path:").grid(row=0, pady=10)
        Label(master=self.root, text="Test set path:").grid(row=0, column=1, pady=10)
        Label(master=self.root, text="Kolumna 1").grid(row=4)
        Label(master=self.root, text="Kolumna 2").grid(row=5)
        Label(master=self.root, text="Klasyfikacja KNN. K:").grid(row=8)
        Label(master=self.root, text="Własne dane(csv) :").grid(row=11)
        self.accuracy = StringVar()
        Label(master=self.root, textvariable=self.accuracy).grid(row=10, columnspan=2)
        self.guess = StringVar()
        Label(master=self.root, textvariable=self.guess).grid(row=13, columnspan=2)
        Label(master=self.root, text="Wykres").grid(row=15, columnspan=2)

        ttk.Separator(self.root, orient="horizontal").grid(row=3, columnspan=2, sticky="ew", pady=20)
        ttk.Separator(self.root, orient="horizontal").grid(row=7, columnspan=2, sticky="ew", pady=20)
        ttk.Separator(self.root, orient="horizontal").grid(row=14, columnspan=2, sticky="ew", pady=20)

        self.trainval = StringVar()
        self.color1 = StringVar()
        self.color1.set("white")
        self.train = Entry(self.root, textvariable=self.trainval, bg=self.color1.get())
        self.train.grid(row=1, column=0)
        self.testval = StringVar()
        self.color2 = StringVar()
        self.color2.set("white")
        self.test = Entry(self.root, textvariable=self.testval, bg=self.color2.get())
        self.test.grid(row=1, column=1)
        self.e1val = StringVar()
        self.e1 = Entry(self.root, textvariable=self.e1val).grid(row=4, column=1)
        self.e2val = StringVar()
        self.e2 = Entry(self.root, textvariable=self.e2val).grid(row=5, column=1)
        self.kval = StringVar()
        self.k = Entry(self.root, textvariable=self.kval).grid(row=8, column=1)
        self.entrytext = StringVar()
        self.entry = Entry(self.root, textvariable=self.entrytext).grid(row=11, column=1)

        self.create()

        Button(self.root, text="Wczytaj dane", command=self.read).grid(row=2, columnspan=2)
        Button(self.root, text="Rysuj wykres", command=self.graph).grid(row=6, columnspan=2)
        Button(self.root, text="Klasyfikuj testy", command=self.knn).grid(row=9, column=0)
        Button(self.root, text="Wykres accuracy(k)", command=self.accgraph).grid(row=9, column=1)
        Button(self.root, text="Klasyfikuj wpisane dane", command=self.classify).grid(row=12, columnspan=2)

        font = {'family': 'Arial',
                'weight': 'bold',
                'size': 5}

        rc('font', **font)

        self.root.mainloop()

    def read(self):
        try:
            with open(self.trainval.get()) as f:
                reader = csv.reader(f, delimiter=';')
                self.dataset = list(reader)
                self.colors = [encode(row[-1]) for row in self.dataset]

            with open(self.testval.get()) as f:
                reader = csv.reader(f, delimiter=';')
                self.testset = list(reader)
            self.train.config({"background": "lawn green"})
            self.test.config({"background": "lawn green"})
        except FileNotFoundError:
            self.train.config({"background": "orange red"})
            self.test.config({"background": "orange red"})

    def create(self):
        self.figure = Figure(figsize=(4, 3))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)

    def graph(self):
        self.clear()

        i = int(self.e1val.get())
        ii = int(self.e2val.get())
        self.dataset.sort(key=lambda x: x[i])

        a = self.figure.add_subplot(111)
        a.scatter(column(self.dataset, i), column(self.dataset, ii), c=self.colors, cmap="cool")
        self.canvas.get_tk_widget().grid(row=16, column=0, columnspan=2)
        self.canvas.draw()

    def clear(self):
        self.canvas.get_tk_widget().destroy()
        self.create()

    def knn(self):
        knn = KNN(self.dataset, self.testset)
        self.accuracy.set("Dokładność na poziomie: " + "{:.6f}".format(knn.test(int(self.kval.get()))) + " / 1.00")

    def classify(self):
        knn = KNN(self.dataset, None)
        self.guess.set("Wynik klasyfikacji knn tych danych: " + knn.classify(self.entrytext.get().split(';'),
                                                                             int(self.kval.get())))

    def accgraph(self):
        self.clear()
        xaxis = arange(1, len(self.dataset))
        knn = KNN(self.dataset, self.testset)
        yaxis = [knn.test(int(k)) for k in xaxis]

        a = self.figure.add_subplot(111)
        a.plot(xaxis, yaxis)
        self.canvas.get_tk_widget().grid(row=16, column=0, columnspan=2)
        self.canvas.draw()


app = Main()
