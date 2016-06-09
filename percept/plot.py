import matplotlib.lines as lines
import matplotlib.pyplot as plt

COLOR_CLASSIFICATIONS = [
    'black',    # Unclassified
    'blue',     # Classified True (1)
    'red'       # Classified False (0)
]


def generate_line(ax, p0, p1, color='black', style='-'):
    '''
    Generates a line between points p0 and p1 which extends to be the width of
    the plot.
    '''
    x0, y0 = p0
    x1, y1 = p1
    gradient = (y0 - y1) / (x0 - x1)
    intercept = y1 - gradient * x1
    x = ax.get_xlim()
    data_y = [x[0] * gradient + intercept, x[1] * gradient + intercept]
    return lines.Line2D(x, data_y, color=color, linestyle=style)


def get_boundary_plot_fn(weights):
    '''
    Gets the function used to represent and plot the line representative by the
    perceptron's weights. The equation is: f(x) = -(w1/w2)x - w0/w2.
    '''
    def fn(x):
        return -weights[1] / weights[2] * x - weights[0] / weights[2]
    return fn


def get_point_color(point, colors):
    '''
    Get's the color of the point to be displayed.
    '''
    if point.classification is None:
        return colors[0]
    return colors[1] if point.classification else colors[2]


def generate(title, class_boundary, weights, points, bounds):
    '''
    Generates a scatter plot of points with the actualy classification boundary
    and the perceptron's classification boundary drawn in.
    '''
    boundary_fn = get_boundary_plot_fn(weights)

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.set_xlim(bounds[0])
    ax.set_ylim(bounds[1])
    ax.set_title(title)
    ax.add_line(generate_line(
        ax, class_boundary[0], class_boundary[1], 'cyan', '--'
    ))
    ax.add_line(generate_line(ax, (0, boundary_fn(0)), (1, boundary_fn(1))))
    ax.scatter(
        [pt.x for pt in points], [pt.y for pt in points],
        c=[get_point_color(pt, COLOR_CLASSIFICATIONS) for pt in points], s=30
    )
    return fig
