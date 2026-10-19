# Fulfilling-Numbers

Explores the novel concept of a "fulfilling" number, associated with the aliquot sum function from number theory (s(n)). A "fulfilling" number is any positive integer n that is equal to its own output from the "fulfillment" function f(n). f(n) = s(n) plus the summation of f(n) recursively applied to each proper divisor of n (with a base case of f(0) = 0). These numbers are called "fulfilling" because they are not perfect but still fulfill their own value when the aliquot sum function is recursively applied to their proper divisors.

In the range \[1, 100000\], the program identifies 4, 10, and 195 as fulfilling numbers. There does not appear to be an obvious pattern in these three fulfilling numbers, contrasting with the pattern among even perfect numbers where each even perfect number is the product of a power of 2 and a Mersenne prime. Interestingly, 195 may be the only odd fulfilling number. If there are no odd perfect numbers in existence, then 195 may represent a unique and unmatched example of an odd number with a meaningful self-referential result from a function related to aliquot sums.

The code contains two variables that the user can adjust, max_num_to_print and max_num_to_test_for_fulfillment. The program will print the fulfillment function result of all integers in the range \[1, max_num_to_print\]. In addition, The program will print all fulfilling numbers in the range \[1, max_num_to_test_for_fulfillment\]. Reduce max_num_to_test_for_fulfillment from 100000 if a shorter runtime is desired. 

Online sources and Gemini were used to provide common-knowledge advice relating to technical aspects of Python and a few minor technical suggestions during the creation of the code.
