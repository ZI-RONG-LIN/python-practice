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

