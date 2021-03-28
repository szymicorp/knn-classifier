def column(matrix, i):
    return [row[i] for row in matrix]


def encode(name):
    i = 0
    for c in name:
        i += ord(c)
    return i


class Model:

    def __init__(self, root):
        self.root = root
        self.trainset = None
        self.testset = None
        self.colors = None

    def set_trainset(self, trainset):
        self.trainset = trainset

    def set_testset(self, testset):
        self.testset = testset

    def set_colors(self, colors):
        self.colors = colors

