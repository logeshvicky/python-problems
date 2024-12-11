Minimum of three:

Description

Given three integers a, b, c, find the minimum of the three integers and output the value.

Note: Do not use any inbuilt library to find the maximum and minimum value.
  
Input Description
Input:
The first line of input contains 3 space separated integers
  
Constraints:
1<=a<=1000
1<=b<=1000
1<=c<=1000
  
Output Description
Output the minimum value among the three given integers
  
Sample Input 1
11317
Sample Output 1 
3

solution:
  
method_1:
  
def minimumOfThree(a,b,c):
   mylst=[a,b,c] #store input in a list
   mylst.sort() # sort will ascending the element
   print(mylst[0])
  
method_2:  

def minimumOfThree(a,b,c):
  if(a<b and a<c):
    print(a)
  elif(b<c and b<a):
    print(b)
  else:
    print(c)
  
