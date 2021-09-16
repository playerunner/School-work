#main program file for module_test_1
print ()
print ("welcome to the module import program!")

import GitHub_data_module

num_1 = GitHub_data_module.a
num_2 = GitHub_data_module.b
num_3 = GitHub_data_module.c
num_4 = GitHub_data_module.d
num_5 = GitHub_data_module.e

print ("we will now access the data from the module!")
print (num_1, "+", num_2, "=", num_1 + num_2)
print (num_3, "*", num_4, "*", num_5, "=", num_3 * num_4 * num_5)
print ("Magic!")
