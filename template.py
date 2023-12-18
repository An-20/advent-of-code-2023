import sys
import itertools
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque


# sys.setrecursionlimit(1000000)

def transpose(l):
    return list(map(list, zip(*l)))

def transpose_filled(l):
    return list(map(list, itertools.zip_longest(*l, fillvalue=None)))
