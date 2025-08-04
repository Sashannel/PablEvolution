import numpy as numpy
import math

class NN:

    def __init__(self):

        self.layers = []
        self.networkShape = [9, 30, 15, 15, 1]

        for i in range(1, len(self.networkShape)):

            self.layers.append(Layer(self.networkShape[i - 1], self.networkShape[i]))


    def brain(self, inputs):

        for i, layer in enumerate(self.layers):

            if i == 0:

                layer.forward(inputs)

            else:

                layer.forward(self.layers[i - 1].nodes)

            if i != len(self.layers) - 1:

                layer.activation()


        return self.layers[-1].nodes


class Layer:


    def __init__(self, numberOfInputs, numberOfNodes):

        self.numberOfInputs = numberOfInputs
        self.numberOfNodes = numberOfNodes
        self.weights = numpy.random.randn(numberOfNodes, numberOfInputs)
        self.biases = numpy.random.randn(numberOfNodes)
        self.nodes = numpy.zeros(numberOfNodes)


    def forward(self, inputs):

        self.nodes = numpy.dot(self.weights, inputs) + self.biases


    def activation(self):

        self.nodes = 4 / (1 + numpy.exp(self.nodes))
