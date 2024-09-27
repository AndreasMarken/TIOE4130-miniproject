from math import sqrt

def manhattan(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
def euclidean(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)