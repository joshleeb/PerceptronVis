# PerceptronVis

2D Perceptron Visualiser.

Generates nodes places at random locations in a [-1, 1], [-1, 1] region and then splits nodes by a random boundary to simulate two types which are to be classified. The perceptron is then initialised and trained to find this classification.

The dotted cyan line is the actual classification boundary and the black line is the perceptron's boundary at a given iteration.

<img src="/plots/iteration0.png" width="300" height="300" />
<img src="/plots/iteration1.png" width="300" height="300" />
<img src="/plots/iteration2.png" width="300" height="300" />

and so on until the perceptron correctly classifies the nodes.

<img src="/plots/iteration7.png" width="300" height="300" />

## Usage
    python3 percept <directory>

The `directory` is where the PNG images of each training iteration will be stored as `iteration<N>.png`.


## Requirements
The versions are those that were used in development. Other versions may work as well.

+ Python 3.5.1
+ Matplotlib 1.5.1
