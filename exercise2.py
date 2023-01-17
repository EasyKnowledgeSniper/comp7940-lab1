# Write a function that prints all factors of the given parameter x

def print_factor(x):
# your code here
    list2 = []
    for i in range(x+1):
        if i == 0:
            continue

        if x % i == 0:
            list2.append(i)
    
    return print('All factors are: ', list2)
    

# print_factor(52633)