Play ot 4 and 6:

Description
You are given a number stored in a variable with the name N Print the output according to the following conditions
1. If N is divisible by both 4 and 6, print "Awesome!", without quotes
2. Else If N Is divisible by 4, print "Four!", without quotes
3. Else if N is divisible by 6, print "six!", without quotes
4. Else print "Dark!", without quotes

Input Description
The first and the only line of the input contains the value stored in N

Output Description
Print the output as per the conditions mentioned in the problem 

Sample Input 1 
12
Sample Output 1 
Awesome!

solution:

def Solve(N):
  if (N%4==0 and N%6==0):
      print("Awesome!")
  elif(N%4==0):
      print("Four!")
  elif(N%6==0):
      print("Six!")
  else:
      print("Dark!")
   
