import math
import random
from collections import Counter
import matplotlib.pyplot as plt

def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

def normal_cdf(x, mu=0,sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z, low_p = -10.0, 0
    # normal_cdf(-10) is (very close to) 0
    hi_z, hi_p = 10.0, 1
    # normal_cdf(10) is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        # consider the midpoint
        mid_p = normal_cdf(mid_z)
        # and the cdf's value there
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break
        return mid_z

def bernoulli_trial(p):
    return 1 if random.random()<p else 0

def bernoulli(n,p):
    return sum(bernoulli_trial(p) for _ in range(n))

def bernoulli_trial(p):
    return 1 if random.random() < p else 0
def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]
    # use a bar chart to show the actual binomial samples
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,color='r')
    plt.show()
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))
    # use a line chart to show the normal approximation
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
            for i in xs]
    plt.plot(xs,ys)
    plt.title("Bin")
    plt.show()

# def mak_hist1(p,n,num_points):
    # data = [bernoulli(n,p) for _ in range(num_points)]
    # histgram = Counter(data)
    # plt.bar([x-0.4 for x in histgram.keys()],[v/num_points for v in
            # histgram.values()],0.8)

    # mu = p*n
    # sigma = math.sqrt(n*p*(1-p))

    # xs = (min(data),max(data)+1)
    # ys=[normal_cdf(i+0.5,mu,sigma) - normal_cdf(i-0.5,mu,sigma) for i in xs]

    # plt.plot(xs,ys)
    # plt.show()
    
make_hist(0.75,100,10000)
