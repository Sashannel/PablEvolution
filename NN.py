import numpy as numpy
import math
import random
import json

class NN:

    def __init__(self):

        self.layers = []
        self.networkShape = [10, 8, 16, 16, 8, 1]

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
    

    @staticmethod
    def create(mode="random", filepath=None):

        if mode == "random":

            return NN()
        
        elif mode == "saved":

            if filepath == None:

                print("No save file found")

            return NN.load(filepath)
        
        else:

            print("Only random and saved values are accepted")


    @classmethod
    def load(cls, filepath):

        with open(filepath, 'r') as f:

            data = json.load(f)


        nn = cls.__new__(cls)  # Bypass __init__
        nn.networkShape = data['networkShape']
        nn.layers = []

        for i, layer_data in enumerate(data['layers']):

            num_inputs = nn.networkShape[i]
            num_nodes = nn.networkShape[i + 1]
            layer = Layer(num_inputs, num_nodes)
            layer.weights = numpy.array(layer_data['weights'])
            layer.biases = numpy.array(layer_data['biases'])
            nn.layers.append(layer)

        return nn
    
    
    def save(self, filepath):
        
        data = {
            'networkShape': self.networkShape,
            'layers': [
                {
                    'weights': layer.weights.tolist(),
                    'biases': layer.biases.tolist()
                } for layer in self.layers
            ]
        }

        with open(filepath, 'w') as f:

            json.dump(data, f)


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
