Right Triangle:

Description
Given three integers a, b, and & find whether they form the sides of the (Right Angled Triangle)or not, and print “Yes" 
if they form the sides of the triangle else print "No"

For a triangle to be a right-angled triangle it must hold the Pythagoras Theorem i.e. (a^2 + b^2 = c^2, if c is thehypotenuse of the triangle )
Note: If the input holds the necessary condition to be a triangle and right-angled triangle then output "Yes" else output "No"

Input Description
Input:
The first line of input contains 3 space separated integers

Constraints:
1<= a<=1000
1<=b<=1000
1<=c<=1000

Output Description
Output "Yes" or "No",depending upon the answer.
  
Sample Input 1
3 4 5
Sample output 1
Yes

Sample input 2
3 4 6
Sample output 2
No

solution:

def Solve(a,b,c):
    if a*a + b*b == c*c:
        print("Yes")
    else:
        print("No")
  
