import matplotlib.pyplot as plt
from functools import partial
import random
import math

def sum_of_square(v):
    return sum(v_i ** 2 for v_i in v) 

def sum_of_squares_gradient(x):
    return 2*x

def step(theta,gradient,step_size):
    return [theta_i+gradient_i*step_size for theta_i,gradient_i in
            zip(theta,gradient)]
    
def safe(f):
    def g(*args,**kargv):
        try:
            return f(*args, **kargv)
        except:
            return float('inf')
    return g

def minimize_batch(target_fn,gradient_fn,theta_0,tolerance):
    step_size = [1000,100,10,1,0.1,0.01,0.001,0.0001,0.00001]
    theta=theta_0
    value = target_fn(theta_0)
    while True:
        gradient = map(gradient_fn,theta) 
        next_theta_list=[step(theta,gradient,-step_size_i) for step_size_i in
                step_size]
        next_theta = min(next_theta_list, key=target_fn)
        next_value = target_fn(next_theta)
        if  value - next_value < tolerance:
            break
        theta=next_theta
        value = next_value
    return theta

def negate(f):
    return lambda *args,**kargv: -f(*gras,**kargv)

def negate(f):
    return lambda *args,**kargv: [-y for y in f(*gras,**kargv)]

if __name__ == "__main__":
    theta_random = [random.randint(-10,10) for _ in range(3)]
    theta = minimize_batch(sum_of_square, sum_of_squares_gradient,
            theta_random, 0.0000001)
    print theta







# all the content bellow is the test code I write while reading the chapter


# def gradient_estimate(f,x,h):
    # return (f(x+h)-f(x))/h

# def gradient(x):
    # return 2*x

# def square(x):
    # return x ** 2

# partial_gradient_estimate = partial(gradient_estimate,square,h=0.001)

# xs = [x for x in range(-10,10)]
# plt.plot(xs,[gradient(x) for x in xs],'rx',label='Actual')
# plt.plot(xs,[partial_gradient_estimate(x) for x in xs],'+',label='Estimate')
# plt.title('Actual Derivatives vs. Estimates')
# plt.legend(loc=9)
# plt.show()


# def step(v,direction,step_size):
    # return [v_i+d_i*step_size for v_i,d_i in zip(v,direction)]

# def sum_of_squares_gradient(v):
    # return [2*v_i for v_i in v]

# def distance(v1,v2):
    # return math.sqrt(sum([(v1_i-v2_i) ** 2 for v1_i,v2_i in zip(v1,v2)]))

# v= [random.randint(-10,10) for i in range(3)]
# tolerance = 0.00000001

# while True:
    # direction = sum_of_squares_gradient(v)
    # new_v=step(v,direction,-0.01)
    # if distance(new_v,v) < tolerance:
        # break
    # v=new_v

# print v
