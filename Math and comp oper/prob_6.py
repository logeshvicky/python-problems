'''---> Operation on Numbers

Description

You are given a number, stored in a variable with the name numberPerform the following operations on the value
stored in the number

1. Multiply the value by 3
2. Add 7 after it
3. Subtract 10 from it

After performing all the above operations, print the updated value

Input Description
The first and the only line of the input contains the number, stored in the variable number

Constraints
1K=N<=30

Output Description
Print a single integer, denoting the updated value of the number stored, after performing all the operations, given in the problem statement

Sample Input 1
4
Sample Output 1
9'''

solution:

def update_number(num):
  a=num
  b=a*3
  c=b+7
  d=c-10
  print(d)
  
    
