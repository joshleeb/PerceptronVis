import os
import perceptron
import plot
import point
import random
import sys
import time

NUM_POINTS = 100
BOUNDS = ((-1, 1), (-1, 1))


def usage():
    print('Usage:')
    print('python3 percept <directory path>')


def generate_class_boundary_line(bounds):
    '''
    Generates a classification boundary to be used on the randomly places
    points before the perceptron is trained.
    '''
    return (
        (round(random.uniform(bounds[0][0], bounds[0][1]), 3),
        round(random.uniform(bounds[0][0], bounds[0][1]), 3)),
        (round(random.uniform(bounds[0][0], bounds[0][1]), 3),
        round(random.uniform(bounds[0][0], bounds[0][1]), 3))
    )


def save_plot(path, iteration, weights, class_boundary, points):
    plt = plot.generate(
        'N={}, Iteration {}, W={}'.format(NUM_POINTS, iteration, weights),
        class_boundary, weights, points, BOUNDS
    )
    plt.savefig(os.path.join(path, 'iteration{}.png'.format(iteration)))


def main(path='./'):
    random.seed(int(time.time() * 10**6))
    points = point.generate_points(NUM_POINTS, BOUNDS)
    class_boundary = generate_class_boundary_line(BOUNDS)
    percept = perceptron.Perceptron()
    iteration = 0

    # Apply classification to randomply places points.
    for pt in points:
        pt.apply_classification(class_boundary)

    save_plot(path, iteration, percept.get_weights(), class_boundary, points)

    # As long as the perceptron is not perfectly classifying points, keep
    # training with training data.
    while not perceptron.is_classified(percept, points):
        iteration += 1

        for pt in points:
            percept.train(int(pt.classification), pt.x, pt.y)

        save_plot(path, iteration, percept.get_weights(), class_boundary, points)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        os.makedirs(path)

    main(path)
