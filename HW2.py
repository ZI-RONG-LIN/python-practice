#2.1 向下取整//  取餘數%
# Read an integer:
a = int(input())
# Print a value:
print(str(a//10)+" "+str(a%10) )
#輸入陣列
a,b=input()
print(a,b)

#2.2
# Read an integer:
a = int(input())
# Print a value:
print(str(a%10)+str(a//10))

a,b=input()
print(b+a)

#2.3
# Read an integer:
a = int(input())
# Print a value:
print(a%100)

#2.4
# Read an integer:
#a = int(input())
# Print a value:
# print(a)
a= int(input())
print(a%100//10)

#2.5
# Read an integer:
a = int(input())
# Print a value:
print(a//100+a%100//10+a%10)

#2.6
# Read a float:
a = float(input())
# Print a value:
print(int(a*10%10))

#2.7 向上取整ceil()
# Read an integer:
N = int(input())
M = int(input())
# Print a value:
from math import ceil
print(ceil(M/N))

#2.8
# Read an integer:
a = int(input())
# Print a value:
from math import ceil
print(ceil(a/100))

#2.9
A = int(input())
B = int(input())
N = int(input())
# print(str(A*N + (B*N/100))+ " " +str(B*N%100))
D=A*N+(B*N//100)
C=(B*N)%100
print(str(D)+" "+str(C)) 

#2.A
# Read an integer:
a = int(input())+3
# Print a value:
print(a%7)

#2.B
M = int(input())
# Print a value:
print(str(M//60)+ " " +str(M-(M//60*60)))

#2.C
# Read an integer:
a = int(input())
b=a%60*12%360
# Print a value:
print(b)

#2.D
# Read an integer:
a = int(input())
b= int(input())
c= int(input())
# Print a value:
from math import ceil
print (ceil(a/2)+ceil(b/2)+ceil(c/2))
