import csv
from knn import KNN
from model import encode, column
from numpy import arange


class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model

        view.set_command("read", self.read)
        view.set_command("knn", self.knn)
        view.set_command("classify", self.classify)
        view.set_command("graph", self.correlation_graph)
        view.set_command("accuracy", self.accuracy_graph)

    def read(self):
        try:
            with open(self.view.entries["trainpath"].get()) as f:
                reader = csv.reader(f, delimiter=';')
                self.model.set_trainset(list(reader))
                self.model.set_colors([encode(row[-1]) for row in self.model.trainset])

            with open(self.view.entries["testpath"].get()) as f:
                reader = csv.reader(f, delimiter=';')
                self.model.set_testset(list(reader))

            self.view.entries["trainpath"].config({"background": "lawn green"})
            self.view.entries["testpath"].config({"background": "lawn green"})
        except FileNotFoundError:
            self.view.entries["trainpath"].config({"background": "orange red"})
            self.view.entries["testpath"].config({"background": "orange red"})

    def knn(self):
        knn = KNN(self.model.trainset, self.model.testset)
        self.view.get_label("accuracy").config(text="Accuracy level: " + "{:.6f}".format(knn.test(int(self.view.get_entry("kval").get()))) + " / 1.00")

    def classify(self):
        knn = KNN(self.model.trainset, None)
        self.view.get_label("guess").config(text="Input classified to: " + knn.classify(self.view.get_entry("inputdata").get().split(';'), int(self.view.get_entry("kval").get())))

    def correlation_graph(self):
        i = int(self.view.entries["column1"].get())
        ii = int(self.view.entries["column2"].get())
        self.model.trainset.sort(key=lambda x: x[i])
        self.view.scatter_graph(column(self.model.trainset, i), column(self.model.trainset, ii), self.model.colors, "cool")

    def accuracy_graph(self):
        xaxis = arange(1, len(self.model.trainset))
        knn = KNN(self.model.trainset, self.model.testset)
        yaxis = [knn.test(int(k)) for k in xaxis]
        self.view.plot_graph(xaxis, yaxis)


