'''
ELVIS LUTTA
P15/35805/2013
'''


from random import uniform
from utility import calc_avg, euclidean_distance, load_pima_diabetes


#########  TODO: ADD DESIRED OUTPUT TO EACH DATA ELEMENT
######### ALSO MAKE SURE THE LENGTH OF WEIGHT VECTOR AND INPUT ITEM LIST ARE SAME

class Data(object):
    """data structure for representing Each input element and its attributes"""
    group = 0
    weight = 0

    def __init__(self, input_elements, desired_output):
        self.input_elements = input_elements
        self.desired_output = desired_output

    def __getitem__(self,index):
        return self.input_elements[index]

    def __setitem__(self,index,value):
        self.input_elements[index] = value

    def __str__(self):
        return self.input_elements

    def __repr__(self):
        return str(self.input_elements)

    def assign_group(self, grp):
        self.group = grp


# These can be changed later if user wants to
threshold = 1
learning_rate = 0.05


# calculate the dot product of the weights and input vectors
def dot_product(input_vector, weight):
    return sum(v * w for v, w in zip(input_vector, weight))


# if there are no specific weights for the input we can generate a list of weights for each size of the vector.
def get_weights(vector_size):
    weights = list()
    for weight in range(vector_size):
        weights.append(uniform(0,1))
    return weights


def calc_output(dot_prod, bias=0):
    if (dot_prod + bias) > threshold:
        return 2
    else:
        return 1


def modify_weight(learn_rate, error, cur_input, old_weight=0):
    return old_weight + (learn_rate * error * cur_input)


# Takes in a list of Data objects(input_vector) which have within them lists containing the input
def perceptron(input_vector):
    error_rate = 1
    weight_vector = get_weights(len(input_vector[0].input_elements))  # add check for data that includes weights

    # If there is no error we do not continue with the loop
    while error_rate is not 0:
        for data in input_vector:
            output = calc_output(dot_product(data.input_elements, weight_vector))
            error_rate = data.desired_output - output
            # print 'Data ', data.input_elements, 'Weight ', weight_vector, ' output ', output, ' desired output ', data.desired_output
            # print 'Output - ', output, '\n'
            # print 'error rate - ', error_rate, '\n'
            # When we find an error ie its 0 we adjust weights
            if error_rate is not 0:
                for i in range(len(weight_vector)):
                    weight_vector[i] = modify_weight(learning_rate, error_rate, data.input_elements[i], weight_vector[i])
                    # print "Weight modified\n"
                    # print 'Data ', data.input_elements, 'Weight ', weight_vector[i], ' output ', output, ' desired output ', data.desired_output

            # if error_rate is 0:
                # print 'error rate is ', error_rate
    global weights
    weights = weight_vector

    # print 'inputs', input_vector, ' weights ', weight_vector


def test(input_vector):
    f = open('perceptron_results.txt', 'w')
    for data in input_vector:
        output = calc_output(dot_product(data.input_elements, weights))
        f.write('desired - ')
        f.write(str(data.desired_output))
        f.write('  actual - ')
        f.write(str(output))
        f.write('\r\n')

    f.close()
# weights = [0, 0, 0]
# a1 = Data([1, 0, 0], 1)
# a2 = Data([1, 0, 1], 1)
# a3 = Data([1, 1, 0], 1)
# a4 = Data([1, 1, 1], 0)

# training_set = [a1, a2, a3, a4]
# perceptron(training_set)


# print '\n\n\n'

diabetes_data = load_pima_diabetes()
input_data = list()

for data in diabetes_data:
    output = data[-1]
    data.pop(len(data) - 1)
    input_data.append((data, int(output)))
# print input_data
input_elem = list()

for index, data in enumerate(input_data):
    temp = Data(data[0], data[1])
    input_elem.append(temp)

num_elements = len(input_elem)
# print len(input_elem[0].input_elements)
perceptron(input_elem[0:((num_elements / 50) * 49)])
test(input_elem[((num_elements / 50) * 49):])


# training_set = [((1, 0, 0), 1), ((1, 0, 1), 1), ((1, 1, 0), 1), ((1, 1, 1), 0)]
# while True:
#     print('-' * 60)
#     error_count = 0
#     for input_vector, desired_output in training_set:
#         print(weights)
#         result = dot_product(input_vector, weights) > threshold
#         error = desired_output - result
#         if error != 0:
#             error_count += 1
#             for index, value in enumerate(input_vector):
#                 weights[index] += learning_rate * error * value
#         if error_count == 0:
#             break
