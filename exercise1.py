# Find the all factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1

x = 52633
list1 = []

# your code here
for i in range(x+1):
    if i == 0:
        continue

    if x % i == 0:
        list1.insert(i-1, i)

print('All factors of x are: ', list1)