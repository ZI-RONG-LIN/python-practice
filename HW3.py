#3.1
# Read an integer:
a = int(input())
# Print a value:
# print(a)
if a%2 == 0:
    print("even")
else:
    print("odd")

#3.2
# Read an integer:
a = int(input())
b = int(input())
# Print a value:
# print(a)
if a<b:
  print(a)
else:
  print(b)

#3.3
# Read an integer:
a = int(input())
# Print a value:
# print(a)
if a<0:
  print("-1")
elif a>0:
  print("1")
else:
  print("0")

#3.4
# Read an integer:
a = int(input())
# Print a value:
# print(a)

if 99<a<1000:
  print("YES")
else:
  print("NO")

#3.5
# Read an integer:
a = int(input())
b= int(input())
# Print a value:
# print(a)
if a*b<0:
  print("YES")
else:
  print("NO")

#3.6
# Read an integer:
a = int(input())
# Print a value:
if a%1000//100 < a%100//10 < a%10:
  print("YES")
else:
  print("NO")
# print(a%10)

#3.7
# Read an integer:
# a = int(input())
# Print a value:
# print(a)
a = int(input())
# print(a//100)
# print(a%100)
# print(a%100//10)
# print(a%10)
# print(str(a//100))
# print(str(a%10) + str(a%100//10))

if str(a//100) == str(a%10) + str(a%100//10):
  print("YES")
else:
  print("NO")

#3.8
# Read an integer:
# a = int(input())
# Print a value:
# print(a)
a = int(input())
b = int(input())
c = int(input())

print(min(a,b,c))

#3.9
# Read an integer:
a = int(input())
# Print a value:
# print(a)
if a in (1,3,5,7,8,10,12):
  print("31")
elif a == 2:
  print("28")
else:
  print("30")

#3.A
# Read an integer:
a = int(input())
b = int(input())
c = int(input())
# Print a value:
# print(a)
if a==b and a==c and b==c:
  print("3")
elif a!=b and a!=c and b!=c:
  print("0")
else:
  print("2")

#3.B
# Read an integer:
a = int(input())
b = int(input())
c = int(input())
# Print a value:
# print(a)
if a==b:
  print("3")
elif a==c:
  print("2")
else:
  print("1")

#3.C
# Read an integer:
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
# Print a value:
# print(a)
if a1==b1 or a2==b2:
  print("YES")
else:
  print("NO")

#3.D
# Read an integer:
x = int(input())
y = int(input())
# Print a value:
if (x+y)%2 ==0:
  print("YES")
else:
  print("No")

#3.E
# Read an integer:
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
# Print a value:
# print(a)
if (a1+a2+b1+b2)%2 ==0:
  print("YES")
else:
  print("NO")

#3.F
# Read an integer:
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
# # Print a value:
if 0<=((b1-a1)**2)<=1 and 0<=((b2-a2)**2)<=1:
  print("YES")
else:
  print("NO")
#解二
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
  print('YES')
else:
  print('NO')

#3.G
# Read an integer:
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
# Print a value:
# print(a)

if abs(b1-a1)-abs(b2-a2)==0:
  print("YES")
else:
  print("NO")

#3.H
# Read an integer:
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
# Print a value:
# print(a)
if abs(b1-a1) == abs(b2-a2):
  print("YES")
elif abs(b1-a1)==0 or abs(b2-a2)==0:
  print("YES")
else:
  print("NO")

#3.I
# Read an integer:
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
# Print a value:
# print(a)
if abs(b1-a1)*abs(b2-a2)==2:
  print("YES")
else:
  print("NO")

#3.J
if a%4 ==0 and a%100 !=0:
  print("LEAP")
elif a%400==0:
  print("LEAP")
else:
  print("COMMON")

#3.K
# Read an integer:
MON = int(input())
D = int(input()) 
# Print a value:
# print(a)
if MON in [1,3,5,7,8,10] and D==31:
  print(MON+1)
  print(1)
elif MON ==2 and D==28:
  print(MON+1)
  print(1)
elif MON in (2,4,6,9,11) and D==30:
  print(MON+1)
  print(1)
elif MON==12 and D==31:
  print(1)
  print(1)
else :
  print(MON)
  print(D+1)

#3.L
# Read an integer:
a = int(input())
b = int(input())
# Print a value:
# print(a)
if a==0 and b!=0:
  print("no solution")
elif a==0 and b==0:
  print("many solutions")
elif b%a !=0 :
  print("no solution")
elif b%a ==0:
  print(int(b/a))
else:
  print("many solutions")

#3.M
# Read an integer:
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
# Print a value:
print(min(a,b,c,d,e))

#3.N
# Read an integer:
a1 = int(input())
a2= int(input())
b1 = int(input())
b2 = int(input())
c1 = int(input())
c2 = int(input())
d1=b1-a1+c1
d2=b2-a2+c2
if a1==b1:
  print(c1)
  if a2==b2:
    print(c2)
  elif a2==c2:
    print(b2)
  elif b2==c2:
    print(a2)
elif a1==c1:
  print(b1)
  if a2==b2:
    print(c2)
  elif a2==c2:
    print(b2)
  elif b2==c2:
    print(a2)
elif b1==c1:
  print(a1)
  if a2==b2:
    print(c2)
  elif a2==c2:
    print(b2)
  elif b2==c2:
    print(a2)
#解二
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

if x1 == x2:
  x4 = x3
elif x1 == x3:
  x4 = x2
else:
  x4 = x1
  
if y1 == y2:
  y4 = y3
elif y1 == y3:
  y4 = y2
else:
  y4 = y1
  
print(x4)
print(y4)

#3.O
# Read an integer:
a = int(input())
b = int(input())
c = int(input())
# Print a value:
# print(a)
print(min(a,b,c))
print(a+b+c-min(a,b,c)-max(a,b,c))
print(max(a,b,c))