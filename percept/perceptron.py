import random


def rand_w():
    '''
    Generate a random weight.
    '''
    return round(random.uniform(-1, 1), 3)


class Perceptron:
    def __init__(
        self, w0=rand_w(), w1=rand_w(), w2=rand_w(), learning_rate=0.1):
        self.w0, self.w1, self.w2 = w0, w1, w2
        self.learning_rate = learning_rate

    def train(self, y, x1, x2):
        y_hat = self.predict(x1, x2)

        if y_hat < y:
            self.w0 += self.learning_rate
            self.w1 += self.learning_rate * x1
            self.w2 += self.learning_rate * x2
        if y_hat > y:
            self.w0 -= self.learning_rate
            self.w1 -= self.learning_rate * x1
            self.w2 -= self.learning_rate * x2
        self.round_weights()

    def evaluate(self, x1, x2):
        return self.w0 + self.w1 * x1 + self.w2 * x2

    def activate(self, y):
        return int(y >= 0)

    def predict(self, x1, x2):
        return self.activate(self.evaluate(x1, x2))

    def round_weights(self, dp=3):
        self.w0 = round(self.w0, dp)
        self.w1 = round(self.w1, dp)
        self.w2 = round(self.w2, dp)

    def get_weights(self):
        return (self.w0, self.w1, self.w2)

    def get_plot_fn(self):
        def fn(x):
            return -self.w1 / self.w2 * x - self.w0 / self.w2
        return fn


def is_classified(percept, points):
    '''
    Checks if all points are correctly classified by the perceptron.
    '''
    for pt in points:
        if percept.predict(pt.x, pt.y) != int(pt.classification):
            return False
    return True
