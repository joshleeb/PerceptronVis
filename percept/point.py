import random


class Point:
    def __init__(self, x, y, classification=None):
        self.x = x
        self.y = y
        self.classification = None

    def __repr__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.classification)

    def __str__(self):
        return self.__repr__()

    def apply_classification(self, class_boundary):
        '''
        Applies the classification rule to the point.
        '''
        class_fn = generate_class_fn(class_boundary)
        self.classification = self.y >= class_fn(self.x)

    @classmethod
    def create_random(cls, bounds):
        '''
        Creates a point with random coordinates within the specified bounds.
        '''
        rand_x = round(random.uniform(bounds[0][0], bounds[0][1]), 3)
        rand_y = round(random.uniform(bounds[1][0], bounds[1][1]), 3)
        return Point(rand_x, rand_y)


def generate_points(n, bounds):
    '''
    Generates a list of n points with random coordinates.
    '''
    return [Point.create_random(bounds) for i in range(n)]


def generate_class_fn(bounds):
    '''
    Generates a function used to classify the generated points. The function
    returned is the equation of the class boundary points specified.
    '''
    x0, y0, x1, y1 = bounds[0][0], bounds[0][1], bounds[1][0], bounds[1][1]
    gradient = (y0 - y1) / (x0 - x1)

    def fn(x):
        return gradient * (x - x0) + y0
    return fn
