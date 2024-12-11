Multiplication Table of N:

Description
Given a number, stored in the variable with the name num Print the multiplication table of the value stored in num 
For example, if the value stored in num is 2, then the output should be
2
4
6
8
10
12
14
16
18
20
Print each number, on a newline

Input Description
The first and the only line of the input contains the value stored in num 

Output Description
Print the multiplication table of the value stored in num

Sample Input 1
3
Sample output 1
3
6
9
12
15
18
21
24
27
30

solution:

def print_multiplication_table(num):
    for i in range (1,11):
        print(i * num)

