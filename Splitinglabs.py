'''
There are 3 labs in the CSE department(L1, L2, and L3) with a seating capacity of x, y, and z respectively. Find the lab which has minimal seating capacity.  
Input format:
Input consists of 3 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
Output format:
Print the minimal seating lab capacity
Refer the Sample output for formatting
Sample Input:
30
40
20
Sample Output:
L3
Ans:
'''
def find_minimal_lab(a, b, c):
    # Create a dictionary to map lab names to their capacities
    labs = {'L1': a, 'L2': b, 'L3': c}
    # Find the lab with the minimum capacity
    min_lab = min(labs, key=labs.get)
    return min_lab

# Input
a = int(input())
b = int(input())
c = int(input())

# Find and print the lab with minimal seating capacity
minimal_lab = find_minimal_lab(a, b, c)
print(minimal_lab)
