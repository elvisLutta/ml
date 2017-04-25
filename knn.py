from mymath import euclidean_distance


class Data(object):
    """Define the data and its attributes"""
    pos = 0
    dist = 0
    def __init__(self, list, classification):
        self.list = list
        self.classification = classification

    def set_pos(self, pos):
        self.pos = pos

    def set_dist(self, dist):
        self.dist = dist


# Receive a list of Data objects
def KNN(k, qi, data):
    for item in data:
        dist = euclidean_distance(qi, item.list)
        item.set_dist(dist)

    # once all the distances are set sort them and pick the k nearest neighbour
    data = sorted(data, key=lambda data_item: data_item.dist)

    for index, i in enumerate(data):
        i.set_pos(index + 1)

    # list containing K Nearest Neighbours
    k_list = []
    for item in range(k):
        k_list.append(data[item].classification)


    if k < 3:
        if k == 1:
            return k_list
        total = 0
        for x in range(2):
            total += k_list[x]
        return total / 2.0


    print k_list
    return max(set(k_list), key=k_list.count)


# def main():
#     if __name__ == '__main__':
data1 = Data([1], 23)
data2 = Data([1.2], 17)
data3 = Data([3.2], 12)
data4 = Data([4], 27)
data5 = Data([5.1], 8)
# data6 = Data([], 'F')
# data7 = Data([], 'F')
# data8 = Data([], 'G')

data_items = [data1, data2, data3, data4, data5]

print KNN(2, [6.5], data_items)
