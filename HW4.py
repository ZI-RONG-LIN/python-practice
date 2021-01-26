#4.1
a = int(input())
b = int(input())
for i in range(a,b+1):
  print(i,end=' ')

#4.2
# Read an integer:
a = int(input())
b = int(input())
# Print a value:
# 
if a>=b:
  for i in range(a, b-1,-1):
    print(i,end=' ')
else:
  for i in range(a, b+1):
    print(i,end=' ')

#4.3
#老師解
sum=0
for i in range(10):
    sum=sum+int(input())
print(sum)

#4.4
sum=0
N=int(input())
for i in range(N):
    sum=sum+int(input())
print(sum)

#4.5
sum=0
N=int(input())
for i in range(1,N+1):
    sum=sum+(i**3)
print(sum)

#4.6
#階層的話起始ersult不能等於0，要設成1
result=1
n=int(input())
for i in range(1,n+1):
  result=result*i
print(result)

#4.7
#判斷輸入的數字中有幾個數字是0
count=0
n=int(input())
for i in range(n):
  if int(input())==0:
    count=count+1
print(count)

#4.8 難
#先計算階層之後，再把階層結果相加
#n=4 -> 1!+2!+3!+4!=33
result=1
sum=0
n=int(input())
for i in range(1,n+1):
  result=result*i
  sum=sum+result
print(sum)

#4.9
#找不見的牌，假設有5張牌，只拿到4張，猜是哪個數字沒拿到
#先算N!，再算拿到的數字加總，相減就可以知道缺哪個數字
result=0
sum=0
N=int(input())
for i in range(1,N+1):
  result += i
for i in range(1,N):
  sum += int(input())
# print(result)
# print(sum)
print(result-sum)

#4.A
#巢狀迴圈
#ex:input(3)
#output:
#1
#12
#123
a = int(input())
for i in range(1,a+1):
  for j in range(1,i+1):
    print(j,end="")
  print()
