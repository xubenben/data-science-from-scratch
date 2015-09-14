import matplotlib.pyplot as plt
import math
import numpy
from collections import Counter, defauldict
from functools import partial

def entropy_function(p):
    if p ==0:
        return 0
    else: return -p*math.log(p)

def entropy(class_probabilities):
    #the trick: if p
    return sum([-p*math.log(p) for p in class_probabilities if p])

def partition_entropy(inputs):
    labels = [label for _,label in inputs]
    total_len = len(inputs)
    class_probabilities = [count/(1.0*total_len) for count in
            Counter(labels).values()]
    return entropy(class_probabilities)

def group_by(inputs,attribute):
    groups = defauldict(list)
    for input_i in inputs:
        groups[input_i[attribute]].append(input_i)
    return groups

def partition_entropy_by(inputs, attribute):
    groups = group_by(inputs,attribute)
    total_len = sum([len(group) for group in groups.values()])
    return sum([len(group)/(1.0*total_len) * partition_entropy(group) for
        group in groups.values()])

def classify(tree,item):
    if tree in [True,False]:
        return tree
    attribute,subtrees = tree
    subtree_key = item.get(attribute)
    if subtree_key not in subtrees:
        subtree_key = None
    subtree = subtrees[subtree_key]
    return classify(subtree,item)

# sample = numpy.arange(0,1.0,0.01)
# plt.plot(sample,[entropy_function(p_i) for p_i in sample])
# plt.show()
def build_decision_tree_d3(inputs,attribute_candidates=None):
    num = len(inputs)
    num_true = len([input_i for _,input_i in inputs if input_i])
    num_false = num - num_true

    if num_true == 0 :
        return False
    if num_false == 0:
        return True

    if len(attribute_candidates) == 0 :
        return num_true>=num_false

    partition_entropy_by_candidate = partial(partition_entropy_by,inputs)

    best_partition = min(attribute_candidates,key =
            partition_entropy_by_candidate) 
    groups = group_by(inputs, best_partition)
    
    subtrees = {attribute_value: build_decision_tree_d3(partition) for
        attribute_value,partition in groups.iteritems()} 

    subtrees[None] = num_true>=num_false
    return (best_partition,subtrees)

    

if __name__ == "__main__":
    inputs = [
        ({'level':'Senior','lang':'Java','tweets':'no','phd':'no'},   False),
        ({'level':'Senior','lang':'Java','tweets':'no','phd':'yes'},  False),
        ({'level':'Mid','lang':'Python','tweets':'no','phd':'no'},     True),
        ({'level':'Junior','lang':'Python','tweets':'no','phd':'no'},  True),
        ({'level':'Junior','lang':'R','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'R','tweets':'yes','phd':'yes'},    False),
        ({'level':'Mid','lang':'R','tweets':'yes','phd':'yes'},        True),
        ({'level':'Senior','lang':'Python','tweets':'no','phd':'no'}, False),
        ({'level':'Senior','lang':'R','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'Python','tweets':'yes','phd':'no'}, True),
        ({'level':'Senior','lang':'Python','tweets':'yes','phd':'yes'},True),
        ({'level':'Mid','lang':'Python','tweets':'no','phd':'yes'},    True),
        ({'level':'Mid','lang':'Java','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'Python','tweets':'no','phd':'yes'},False)
    ]
    print build_decision_tree_d3(inputs)
