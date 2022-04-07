'''
Given five positive integers, find the minimum and maximum values that can be 
calculated by summing exactly four of the five integers. Then print the 
respective minimum and maximum values as a single line of two space-separated 
long integers.

Example

Input Format

A single line of five space-separated integers.

Constraints

Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
'''

def miniMaxSum(arr):
    arr.sort()
    
    aa = arr[:-1]
    bb = arr[1:]
    
    print(sum(aa), sum(bb))
    
arr =[1, 7,9,3,34]
    
miniMaxSum(arr)


