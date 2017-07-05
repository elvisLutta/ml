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
learning_rate = 0.0000000001
accepted_error_rate = 0.00005
sq_total_error = 0.0
error_list = list()
# calculated_weights = list()


# calculate the dot product of the weights and input vectors
def dot_product(input_vector, weight):
    return sum(float(v) * float(w) for v, w in zip(input_vector, weight))


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
    return old_weight + (2 * learn_rate * error * cur_input)

def compute_total_error(error_list):
    total = 0.0
    for error in error_list:
        total += error ** 2
    return total / 2.0


def adaline(input_vector):
    error_rate = 0
    weight_vector = get_weights(len(input_vector[0].input_elements))

    # while error_rate > accepted_error_rate:
    while error_rate: # > accepted_error_rate:
        for data in input_vector:
            output = calc_output(dot_product(data.input_elements, weight_vector))
            error_rate = data.desired_output - output
            # print output

            # if error_rate > accepted_error_rate:
            if error_rate:# > accepted_error_rate:
                for i in range(len(weight_vector)):
                    weight_vector[i] = modify_weight(learning_rate, error_rate, data.input_elements[i], weight_vector[i])
                    print "Weight modified\n"

    global calculated_weights

    calculated_weights = weight_vector

    print 'FINISHED TRAINING'


def predict(input_vector):
    # modify_weight(learning_rate, error, cur_input, old_weight)
    f = open('lms_results.txt', 'w')

    for data in input_vector:
        f.write(str(data.input_elements))
        f.write('\r\n')
        output = dot_product(data.input_elements, calculated_weights)
        error_rate = data.desired_output - output
        f.write(str(error_rate))
        f.write('\r\n')
        error_list.append(error_rate)  # add error to the to the list
        output = calc_output(output)

        # print 'desired - ', data.desired_output, '  ->   actual - ', output

    sq_total_error = compute_total_error(error_list)
    f.write('\r\nTotal square error\r\n')
    f.write(str(sq_total_error))
    f.close()



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

print '\n\n\n'
print 'TRAINING'

# training_input = list()

# for i in range(len(input_elem)):
#     if (i <= ((num_elements / 4) * 3)):
#         print i
#         training_input[i] = input_elem[i]
#     else:
#         break


# test_data = list()

# for i in range(len(input_elem)):
#     if (i > ((num_elements / 4) * 3)):
#         test_data[i] = input_elem[i]
#     else:
#         break


adaline(input_elem[0:((num_elements / 50) * 49)])

predict(input_elem[((num_elements / 50) * 49):])
# print error_list
