
from .Vector import Vector

def subtract(v: Vector, w: Vector):
    return [vi - wi for vi,wi in zip(v,w)]

def dot(v: Vector, w: Vector):
    return sum(a * b for a,b in zip(v,w))

def sumOfSquares(v: Vector):
    return dot(v,v)

def magnitude(v: Vector):
    return sumOfSquares(v) ** 0.5

def squaredDistance(v: Vector, w: Vector):
    return sumOfSquares(subtract(v,w))

def distance(v: Vector, w: Vector):
    return magnitude(subtract(v,w))

