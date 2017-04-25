from math import sqrt

def euclidean_distance(list1, list2):
# Find the euclidean distance between 2 points
    sum = 0
    for i in range(len(list1)):
        sum += (list1[i] - list2[i]) ** 2

    return sqrt(sum)
