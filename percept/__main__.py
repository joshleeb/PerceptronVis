import perceptron
import plot
import point
import random
import time

NUM_POINTS = 50
BOUNDS = ((-1, 1), (-1, 1))


# TODO: Generate random classification split
def generate_class_boundary_line(bounds):
    '''
    Generates a classification boundary to be used on the randomly places
    points before the perceptron is trained.
    '''
    return (-1, -1), (1, 1)


def classification_rule(point):
    '''
    Classification rule to be used to classify the random points before the
    perceptron is trained.
    '''
    return point.y >= point.x


def main():
    points = point.generate_points(NUM_POINTS, BOUNDS)
    class_boundary = generate_class_boundary_line(BOUNDS)
    percept = perceptron.Perceptron()
    iteration = 0

    # Apply classification to randomply places points.
    for pt in points:
        pt.apply_classification(classification_rule)

    # As long as the perceptron is not perfectly classifying points, keep
    # training with training data.
    while not perceptron.is_classified(percept, points):
        iteration += 1

        for pt in points:
            percept.train(int(pt.classification), pt.x, pt.y)

        weights = percept.get_weights()

        plt = plot.generate(
            'N={}, Iteration {}, W={}'.format(NUM_POINTS, iteration, weights),
            class_boundary, weights, points, BOUNDS
        )
        plt.savefig('iteration{}.png'.format(iteration))


if __name__ == '__main__':
    random.seed(int(time.time() * 10**6))
    main()
