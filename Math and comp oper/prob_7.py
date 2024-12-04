'''---> find X

Description

In a land of puzzles, there lies a mysterious number (X). This number holds a secret, but it is hidden behind a series of magical operations.
To unlock the mystery, follow these clues carefully" 
Clue 1: A sorcerer multiplies this secret number 00) by (3), tripling its power.
Clue 2 To make things even more baffling, the sorcerer then adds 10 to the result.

Your task is to determine X's value from the clues above. Can you unravel this numerical enigma and reveal the hidden number?

Input Description
Input:
Input will contain one number X

Constraints:
0 <X < 1000

Output Description
Output:
Output should be the number X after performing above operations

Sample Input 1 
3
Sample Output 1
19'''

solution:

def solve(N):
    x=N
    y=x*3
    m=y+10
    print(m)

