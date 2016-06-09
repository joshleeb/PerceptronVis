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

    def get_color(self, colors):
        if self.classification is None:
            return colors[0]
        return colors[1] if self.classification else colors[2]

    def apply_classification(self, classification_split):
        self.classification = self.x > classification_split[0] and self.y < classification_split[1]

    @classmethod
    def create_random(cls, bounds, rounding=3):
        rand_x = round(random.uniform(bounds[0][0], bounds[0][1]), rounding)
        rand_y = round(random.uniform(bounds[1][0], bounds[1][1]), rounding)
        return Point(rand_x, rand_y)


def generate_points(n, bounds):
    return [Point.create_random(bounds) for i in range(n)]
