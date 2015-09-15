import math, random
from functools import partial
import matplotlib.pyplot as plt

class Kmeans:
    def __init__(self,k):
        self.means = None
        self.k = k
        self.assignment = None
    
    def distance(self, node1,node2):
        return sum((node1_i-node2_i) ** 2 for node1_i,node2_i in
            zip(node1,node2)) 

    def classify(self,node):
        distance_node = partial(self.distance, node) 
        return min(range(self.k), key = lambda i: distance_node(self.means[i]))
        # return min(self.means, key = distance_node)
   
    def vector_average(self, input_i):
        length = len(input_i)
        w = len(input_i[0]) 
        v = input_i[0] 
        for i in range(1,length):
            for j in range(w):
                v[j] += input_i[i][j]
        v = [v_i/(1.0*length) for v_i in v]
        return v
    
    def train(self, inputs):
        self.means =random.sample(inputs, self.k)
        assignment = None
        while True:
            new_assignment  =  map(self.classify, inputs)
            if new_assignment == assignment:
                self.assignment = new_assignment
                return
            else :
                assignment = new_assignment
            for i in range(self.k):
                input_i = [input_i for index,input_i in enumerate(inputs) if
                        new_assignment[index] == self.means[i]]
                if input_i:
                    self.means[i] = self.vector_average(input_i)

if __name__ == "__main__":
    inputs = [[-14,-5],[13,13],[20,23],[-19,-11],[-9,-16],[21,27],[-49,15],[26,13],[-46,5],[-34,-1],[11,15],[-49,0],[-22,-16],[19,28],[-12,-8],[-13,-19],[-41,8],[-11,-6],[-25,-9],[-18,-3]]
    random.seed(0)
    k_means = Kmeans(3)
    k_means.train(inputs)
    print k_means.means

