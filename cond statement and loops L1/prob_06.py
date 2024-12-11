Even Sum Below N:

Description
You are given a number, stored in a variable with the name num
Find the sum of all even numbers greater than zero, and less than or equal to the valuestored in num
For example, if the value stored in num = 5, then all the even numbers smaller than or equal to 5, and greater than zero are

2
4

Therefore, the sum becomes,
sum = 2 + 4 = 6,which is the required output

Input Description
The first and the only line of input contains the number stored in the variable num

Output Description
Print the sum of all even numbers greater than zero, and less than or equal to the value stored in num

Sample Input 1 
6
Sample Output 1
12

solution:

def sum_of_even_numbers(num):
  sum=0
  for i in range (1,num+1):
    if i%2==0:
      sum+=i
  print(sum)
