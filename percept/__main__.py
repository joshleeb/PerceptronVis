import perceptron
import plot
import point
import random
import time

NUM_POINTS = 100
BOUNDS = ((-1, 1), (-1, 1))


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


def main():
    points = point.generate_points(NUM_POINTS, BOUNDS)
    class_boundary = generate_class_boundary_line(BOUNDS)
    percept = perceptron.Perceptron()
    iteration = 0

    # Apply classification to randomply places points.
    for pt in points:
        pt.apply_classification(class_boundary)

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
