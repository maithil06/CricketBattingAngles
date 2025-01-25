import numpy as np
from scipy.spatial.distance import euclidean

from fastdtw import fastdtw

def score(a,b):
    a = np.array(a)
    b = np.array(b)
    distance = fastdtw(a, b, dist=euclidean)
    return distance