import math

point1 = {
    "x": 2,
    "y": 3
}

point2 = {
    "x": 10,
    "y": 8
}

def euclidean_distance(point1, point2):
    return math.sqrt((point1['x'] - point2['x'])**2 + (point1['y'] - point2['y'])**2)

print('Euclidean distance between', point1, 'and', point2, 'is:')
print(round(euclidean_distance(point1, point2),2))