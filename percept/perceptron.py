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
        '''
        Train the perceptron using input values x1, x2 and an expected output
        value y.
        '''
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
        '''
        Evaluate input values x1, x2.
        '''
        return self.w0 + self.w1 * x1 + self.w2 * x2

    def activate(self, y):
        '''
        Apply the activation function on a value y.
        '''
        return int(y >= 0)

    def predict(self, x1, x2):
        '''
        Predict an output value given input values x1, x2.
        '''
        return self.activate(self.evaluate(x1, x2))

    def round_weights(self):
        '''
        Round weights to 3dp. This is mainly to make plot generation and
        debugging easier.
        '''
        self.w0 = round(self.w0, 3)
        self.w1 = round(self.w1, 3)
        self.w2 = round(self.w2, 3)

    def get_weights(self):
        '''
        Get weights as a tuble. Easier than doing
        `percept.w0, percept.w1, percept.w2` all the time.
        '''
        return (self.w0, self.w1, self.w2)


def is_classified(percept, points):
    '''
    Checks if all points are correctly classified by the perceptron.
    '''
    for pt in points:
        if percept.predict(pt.x, pt.y) != int(pt.classification):
            return False
    return True
