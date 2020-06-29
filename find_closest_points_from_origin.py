# date: 29/06/2020

# Description:
# Given a list of points and a number k, 
# find the k closest points to the origin

import math

ORIGIN = [0,0]
# get distance between two points
def get_distance(p):
    # square root needs more computational power
    # d = math.sqrt(pow(ORIGIN[0]-p[0],2) + pow(ORIGIN[1]-p[1],2))
    d = pow(ORIGIN[0]-p[0],2) + pow(ORIGIN[1]-p[1],2)
    return d

def findClosestPointsOrigin(points, k):
    dists = []
    for i in points:
        d = get_distance(i)
        dists.append([d,i])
    
    dists.sort()
    
    return dists[:k]
print (findClosestPointsOrigin([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))
