From A to B:

Description
You are given two numbers, stored in variables with the following names

max,Min

You have to print all the numbers from min to max, excluding max. Print each number on a new line 
For example, if the value stored in max=19 , and the value stored in min=14, then the output will be
14
15
16
17
18

Note: The value stored in max will always be greater than or equal to min

Input Description
The first and the only line of input contains the value stored in max, min respectively 

Output Description
Print all  the values from min to max exduding max Print each number on anew Line

Sample Input 1 
19 13
Sample Output 1
13
14
15
16
17
18

solution:

def print_range(min_val, max_val):
    for i in range(min_val,max_val):
        print(i)
