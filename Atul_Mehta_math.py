#Create a math function to determine max and min values
def Max(list_of_numbers): #Define a function for finding max number in a list
    max1 = -100000
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] > max1: # This code define max number in a list
            max1 = list_of_numbers[i]
    return max1

# Create a new function for min value in a list
def Min(list_of_numbers): #Define a function for finding Min number in a list
    min1 = 100000
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] < min1: # This code define min number in a list
            min1 = list_of_numbers[i]
    return min1
# Now i define a histogram function
def histogram(list1,b = 3): # here b a default argument for bin
    bin = (Max(list1)- Min(list1))/b
    #now i define a dict
    dict1 = {}
    count1 = 0
    start = Min(list1)
    end = start + bin
    for i in range(b):
        for k in list1:
            if k >= start and k<end:
                count1 += 1
        dict1['<' + str(round(end,2))] = count1
        start = end
        end = end + bin
        count1 = 0
    return dict1
list1 = [2, 4, 6, 8, 1, 4, 6, 7, 2, 4, 6, 8, 1, 2, 5]
print(histogram(list1))
