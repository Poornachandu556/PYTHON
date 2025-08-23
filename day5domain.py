'''
from datetime import datetime
a = input("enter birthday date in(YYYY-MM-DD)")
b = input("enter todays date in (YYYY-MM-DD)")
a1 = datetime.strptime(a,"%Y-%m-%d")
b1 = datetime.strptime(b,"%Y-%m-%d")
print("No of days lived",b1-a1)
'''
'''
# MATCHES SHEDULE
import random
n = int(input("Enter no of teams: "))
teams = []
for i in range(n):
    t = input("Enter team name: ")
    teams.append(t)
m = int(input("Enter no of meetups: "))
matches = []
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(m):
            matches.append([teams[i],teams[j]])
random.shuffle(matches)
for i in range(len(matches)):
    print("Match {} : {} vs {}".format(i+1,matches[i][0],matches[i][1]))
'''
'''
n = int(input("enter any num:"))
num = []
while(n!=1 and n not in num):
    num.append(n)
    n = sum([int(i)*int(i) for i in str(n)])
    
print(num)
if(n==1):
    print("round number")
else:
    print("not a round number")
'''
'''
1
3  * 2
4  * 5 * 6
10 * 9 * 8 * 7
'''
g = [[" " for i in range(10)]for j in range(10)]
for i in range(10):
    for j in range(10):
        if(j==0):
            g[i][j]=int((i*(i+1))/2)
        else:
            g[i][j]=g[i][j-1]-1
        
for i in range(5):
    for j in range(i):
        print(g[i][j],end=" ")
    print()


