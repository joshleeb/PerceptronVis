import matplotlib.pyplot as plt
import point
import random
import time

BOUNDS = ((-1, 1), (-1, 1))
COLOR_CLASSIFICATIONS = ['black', 'blue', 'red']
NUM_POINTS = 20


def main():
    random.seed(int(time.time() * 10**6))
    points = point.generate_points(NUM_POINTS, BOUNDS)

    x = [p.x for p in points]
    y = [p.y for p in points]
    colors = [p.get_color(COLOR_CLASSIFICATIONS) for p in points]

    plt.scatter(x, y, c=colors)
    plt.show()


if __name__ == '__main__':
    main()
