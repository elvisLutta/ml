'''
ELVIS LUTTA
P15/35805/2013
'''


from math import sqrt
from csv import reader


def euclidean_distance(list1, list2):
# Find the euclidean distance between 2 points
    total = 0
    for i in range(len(list1)):
        total += (list1[i] - list2[i]) ** 2

    return sqrt(float(total))


def calc_avg(lists):
    total = 0
    final = list()
    # print len(lists)

    # We return the centroid if there is only one in the array
    if (len(lists) == 1):
        return lists[0]

    # print "length of lists", len(lists)

    # for i in range(len(lists)):
    #     print lists[i].list
    #     print "lists ", lists

    # Otherwise we calculate the average of the centroids
    for index in range(len(lists[0].features)):  # all lists same size so we can use size of the first to determine the rest
        for data in lists:
            total += float(data.features[index])
        final.append(total/len(lists))
        total = 0
    # print 'final', len(final)

    return final


# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


def load_pima_diabetes():
    diabetes_data = load_csv('pimadiabetes.data.txt')
    input_elem = list()
    for diabetes in diabetes_data:
        for data in diabetes:
            data = data.split()
            input_elem.append(data)
    diabetes_data = list()
    temp = list()

    for current in input_elem:
        for data in current:
            data = float(data)
            temp.append(data)
        diabetes_data.append(temp)
        temp = list()
    return diabetes_data
