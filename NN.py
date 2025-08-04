import numpy as numpy
import math
import random

class NN:

    def __init__(self):

        self.layers = []
        self.networkShape = [10, 15, 15, 1]

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
    
    def copyLayers(self):

        copied_layers = []

        for layer in self.layers:

            copied_layer = Layer(layer.numberOfInputs, layer.numberOfNodes)
            copied_layer.weights = layer.weights.copy()
            copied_layer.biases = layer.biases.copy()
            copied_layers.append(copied_layer)
            
        return copied_layers
    
    def copy(self):
        new_nn = NN()
        new_nn.layers = self.copyLayers()
        return new_nn


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

        self.nodes = 4 * numpy.tanh(self.nodes)

    def mutateLayer(self, mutation_chance, mutation_amount):

        for i in range(self.numberOfNodes):

            for j in range(self.numberOfInputs):

                if random.randrange(0, 1) * 0.0001 < mutation_chance:
                    
                    print("Mutation on weights")
                    self.weights[i, j] += random.randrange(-1, 1) * 0.0001 * mutation_amount

            if random.randrange(0, 1) * 0.0001 < mutation_chance:

                print("Mutation on biases")
                self.biases[i] += random.randrange(-1, 1) * mutation_amount

    
    def mutate(self, mutation_chance, mutation_amount, nn):

        for i in range(len(nn.layers)):

            nn.layers[i].mutateLayer(mutation_chance, mutation_amount)
