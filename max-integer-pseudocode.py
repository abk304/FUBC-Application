#Consider a sample array with five sample integers.
sample_array = [sample_number1, sample_number2, sample_number3, sample_number4, sample_number5]
#Assume for instance that we know that sample_number4 is the largest integer in the array.

#Initializing the temporary_max_integer variable to the first element in the array.
temporary_max_integer = sample_array[0]

#Creating a "for-loop" that progressively compares array elements. 
for sample_number in sample_array:
    
    #Compare iteration element to current maximum and replace current maximum if iteration element is larger. Do nothing if it is smaller.
    if sample_number >= temporary_max_integer:
        temporary_max_integer = sample_number
    else:
        pass
        
    #Each iteration the larger number is kept and compared to the next array element until the entire array is scanned.
    #When sample_number4 is compared to sample_number3, it will be stored as the temporary_max_integer, and will then be
    #compared to sample_number5, where temporary_max_integer will remain the same.

print("Maximum integer is: " + str(temporary_max_integer))
#Simply presents the maximum integer back.
