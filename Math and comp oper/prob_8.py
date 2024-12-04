'''---> Seven Numbers

Description

You are given 7 numbers A, B, C, D, E, F, G. Find out the product of (A + B + C) and (D + E + F + G).

Input Description
The first and the only line of the input contains A, B, C, D, E, F, and G.

Constraints
I == A, B, C, D, E, F, G == 30

Output Description
Print the value of the expression (A + B + C) * (D + E + F + G)

Sample input 1
1234567
Sample Output 1 
132'''

solution:

def calculate_expression(A, B, C, D, E, F, G):
     print((A+B+C)*(D+E+F+G))
    
