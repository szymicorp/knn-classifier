from math import sqrt


class KNN(object):

    def __init__(self, train, test):
        self.trains = train
        self.tests = test
        self.best = []

    def test(self, k):
        accuracy = 0.0
        for test in self.tests:
            guess = self.classify(test[:-1], k)
            if guess == test[-1]:
                accuracy += 1.0/len(self.tests)
        return accuracy

    def classify(self, test, k):
        self.best.clear()
        for x in range(k):
            self.best.append([None, 99999999])
        for train in self.trains:
            summary = [float(a) - float(b) for a, b in zip(test, train[:-1])]
            summary = [s ** 2 for s in summary]
            summary = sqrt(sum(summary))

            b = self.max()
            if summary < b[1]:
                self.best.remove(b)
                self.best.append([train[-1], summary])
        occur = 0
        guess = ""
        names = [row[0] for row in self.best]
        for b in names:
            current = names.count(b)
            if current > occur:
                guess = b
                occur = current
        return guess

    def max(self):
        maximum = [None, -999999999]
        for b in self.best:
            if b[1] > maximum[1]:
                maximum = b
        return maximum