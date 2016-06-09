import matplotlib.pyplot as plt
import point
import random
import time

BOUNDS = ((-1, 1), (-1, 1))
COLOR_CLASSIFICATIONS = ['black', 'blue', 'red']
NUM_POINTS = 20


def generate_classification_split_line(bounds):
    return (
        round(random.uniform(bounds[0][0], bounds[0][1]), 3),
        round(random.uniform(bounds[0][0], bounds[0][1]), 3)
    )


def main():
    random.seed(int(time.time() * 10**6))
    points = point.generate_points(NUM_POINTS, BOUNDS)
    classification_split = generate_classification_split_line(BOUNDS)

    for pt in points:
        pt.apply_classification(classification_split)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(
        [p.x for p in points], [p.y for p in points],
        c=[p.get_color(COLOR_CLASSIFICATIONS) for p in points], s=50
    )

    ax.set_title('N={}'.format(NUM_POINTS))
    ax.set_xlim(BOUNDS[0])
    ax.set_ylim(BOUNDS[1])

    plt.show()


if __name__ == '__main__':
    main()
