import matplotlib.pyplot as plt
import matplotlib.lines as lines
import point
import random
import time

BOUNDS = ((-1, 1), (-1, 1))
COLOR_CLASSIFICATIONS = ['black', 'blue', 'red']
NUM_POINTS = 50


# TODO: Generate random classification split
def generate_classification_split_line(bounds):
    return (-1, -1), (1, 1)
    # return (
        # (round(random.uniform(bounds[0][0], bounds[0][1]), 3),
        # round(random.uniform(bounds[0][0], bounds[0][1]), 3)),
        # (round(random.uniform(bounds[0][0], bounds[0][1]), 3),
        # round(random.uniform(bounds[0][0], bounds[0][1]), 3))
    # )


def main():
    random.seed(int(time.time() * 10**6))
    points = point.generate_points(NUM_POINTS, BOUNDS)
    classification_split = generate_classification_split_line(BOUNDS)

    for pt in points:
        pt.apply_classification()

    fig, ax = plt.subplots(figsize=(8, 8))

    print(classification_split)
    # split_line = lines.Line2D(
        # classification_split[0], classification_split[1], linestyle='--'
    # )

    split_line = lines.Line2D(
        [p[0] for p in classification_split],
        [p[1] for p in classification_split], linestyle='--'
    )

    ax.set_title('N={}'.format(NUM_POINTS))
    ax.set_xlim(BOUNDS[0])
    ax.set_ylim(BOUNDS[1])

    ax.add_line(split_line)
    ax.scatter(
        [p.x for p in points], [p.y for p in points],
        c=[p.get_color(COLOR_CLASSIFICATIONS) for p in points], s=50
    )

    plt.show()


if __name__ == '__main__':
    main()
