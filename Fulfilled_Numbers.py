import math

# initializes a variable max_num_to_print
# the program will print the fulfillment function result of all integers 
# in the range [1, max_num_to_print]
max_num_to_print = 20

# initializes a variable max_num_to_test_for_fulfillment
# the program will print all fulfilled numbers in the range 
# [1, max_num_to_test_for_fulfillment]
max_num_to_test_for_fulfillment = 100000

# get_proper_divisors
# function to return the proper divisors of an integer
# expects a positive integer n as input
# returns the proper divisors of n as a list
def get_proper_divisors(n):

    # initializes list to store proper divisors
    proper_divisors = []

    # appends all divisors in the range [1, sqrt(n)) to the list
    for i in range(1, math.ceil(math.sqrt(n))):
        if (n % i == 0):
            proper_divisors.append(i)

    # appends sqrt(n) to the list if appropriate 
    if math.ceil(math.sqrt(n)) == math.sqrt(n) and n > 1:
        proper_divisors.append(round(math.sqrt(n)))

    # considering the existing elements of the list, 
    # appends the remaining proper divisors in the range (sqrt(n), n)
    for f in proper_divisors[::-1]:
        if (n // f) not in proper_divisors and f != 1:
            proper_divisors.append(n // f)

    # returns the list of proper divisors
    return(proper_divisors)


# fulfillment_function
# function to return the result of applying the fulfillment function to an integer
# expects a positive integer n as input 
# returns an integer result of applying the fulfillment function to the input n
def fulfillment_function(n):

    # start by identifying the proper divisors of n
    proper_divisors_of_n = get_proper_divisors(n)

    # initialize a variable "fulfillment_result" to store the output of fulfillment_function
    # calculate the aliquot function of n as a first step in the fulfillment function
    fulfillment_result = sum(proper_divisors_of_n)
    
    # recursively apply the function to each proper divisor and add the values to fulfillment_result
    for i in proper_divisors_of_n:
        fulfillment_result += fulfillment_function(i)

    # return the fulfillment_result
    return fulfillment_result


# print the fulfillment result of integers in the range [1, max_num_to_print]
for i in range(1, max_num_to_print + 1):
    print(str(i) + ": " + str(fulfillment_function(i)))

# print all fulfilled numbers in the range [1, max_num_to_test_for_fulfillment]
for i in range(1, max_num_to_test_for_fulfillment + 1):
    if i == fulfillment_function(i):
        print(str(i) + " is a fulfilled number.")


