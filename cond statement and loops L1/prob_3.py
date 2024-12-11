Masai Divisors:

Description

you are provided 3 integers: left, right and k. 
your task is to write a program that,
finds out the count of all such numbers between lefts and right (both inclusive) which are divided by k.
  
Input Description

Input Format
First line contains 3 space separated integers which are left, right and k respectively.
  
Constraints
0<=left, right, k <= 10000
  
Output Description
output the count as mentioned in problem description.

Sample Input 
1 10 3
Sample Output 
3

solution:

def count_numbers_divisible_by_k(left, right, k):
    count=0
    for i in range (left,right+1):
        if i%k==0:
          count +=1
    print(count)
    
