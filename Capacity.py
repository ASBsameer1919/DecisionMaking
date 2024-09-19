'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z. A single lab needs to be allocated to a class of 'n' students. How many of the 3 labs can accommodate 'n' students?
Input format:
Input consists of 4 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the number of students(x)
Output format:
Print the number of labs which can accommodate the 'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
2 
Ans:
'''
def count_accommodating_labs(a, b, c, n):
    # Initialize a counter for labs that can accommodate 'n' students
    count = 0
    
    # Check each lab's capacity against the number of students
    if a >= n:
        count += 1
    if b >= n:
        count += 1
    if c >= n:
        count += 1
        
    return count

# Input
a = int(input())
b = int(input())
c = int(input())
n = int(input())

# Find and print the number of labs that can accommodate 'n' students
accommodating_labs_count = count_accommodating_labs(a, b, c, n)
print(accommodating_labs_count)
