import matplotlib.lines as lines
import matplotlib.pyplot as plt
import perceptron
import point
import random
import time

NUM_POINTS = 50
BOUNDS = ((-1, 1), (-1, 1))
COLOR_CLASSIFICATIONS = [
    'black',    # Unclassified
    'blue',     # Classified True (1)
    'red'       # Classified False (0)
]


# TODO: Generate random classification split
def generate_classification_split_line(bounds):
    return (-1, -1), (1, 1)


def generate_line(ax, p0, p1, color='black', style='-'):
    x0, y0 = p0
    x1, y1 = p1
    gradient = (y0 - y1) / (x0 - x1)
    intercept = y1 - gradient * x1
    x = ax.get_xlim()
    data_y = [x[0] * gradient + intercept, x[1] * gradient + intercept]
    return lines.Line2D(x, data_y, color=color, linestyle=style)


def main():
    random.seed(int(time.time() * 10**6))
    points = point.generate_points(NUM_POINTS, BOUNDS)
    classification_split = generate_classification_split_line(BOUNDS)
    percept = perceptron.Perceptron()
    iteration = 1

    for pt in points:
        pt.apply_classification()

    while not perceptron.is_classified(percept, points):
        for pt in points:
            percept.train(int(pt.classification), pt.x, pt.y)
        iteration += 1

    boundary_fn = percept.get_plot_fn()

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.set_title('N={}, Iteration {}, W={}'.format(NUM_POINTS, percept.get_weights(), 1))
    ax.set_xlim(BOUNDS[0])
    ax.set_ylim(BOUNDS[1])

    ax.add_line(generate_line(
        ax, classification_split[0], classification_split[1], 'cyan', '--'
    ))
    ax.add_line(generate_line(ax, (0, boundary_fn(0)), (1, boundary_fn(1))))

    ax.scatter(
        [p.x for p in points], [p.y for p in points],
        c=[p.get_color(COLOR_CLASSIFICATIONS) for p in points], s=50
    )

    plt.show()


if __name__ == '__main__':
    main()
