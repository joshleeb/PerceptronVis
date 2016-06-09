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

    # TODO: Apply classifications from class_boundary.
    def apply_classification(self, class_boundary):
        '''
        Applies the classification rule to the point.
        '''
        self.classification = self.y >= self.x

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
