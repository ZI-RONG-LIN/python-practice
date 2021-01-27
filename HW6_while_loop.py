#6.1
# Read an integer:
a = int(input())
# Print a value:
# print(a)
i=1
while i<=a**0.5:
  print(i**2)
  #如果沒有i+=1的話，i就會一直停留在1
  i +=1

#老師解
a = int(input())
i=1
while i**2<=a:
  print(i**2,end=" ")
  i +=1

#6.2
# Read an integer:
a = int(input())
# Print a value:
# print(a)
i=2
#除i的餘數不等於0的時候，繼續試，有0的時候則跳出while迴圈，print出來
while a%i!=0:
  i +=1
print(i)

#6.3
#老師解
# Read an integer:
a = int(input())
#用i+1是因為先跑到i+=1之後才print，所以如果沒有用i的話
#就會print出6
i=0
while 2**(i+1)<=a:
  i +=1
print(i,2**i)
#解二
x = int(input())
n = 1
while 2 ** n <= x:
  n += 1
print(n - 1, 2 ** (n - 1))

#6.4
#老師解
#每天多跑10%的距離的話，要幾天會超過指定距離
# Read an integer:
x = int(input())
y = int(input())
# Print a value:
# print(a)
i=1
while x<y:
  x*=1.1
  i+=1
print(i)

#6.5
# Read an integer:
a = int(input())
i=0
#a不等於0的時候，i就+1；等於0的話就跳出迴圈print出來
while a!=0:
  i +=1
  #後面輸入的值繼續放進去判斷，就不用一開始就打一堆變數進去
  a = int(input())
print(i)

#6.6
#把0前面的數字加總
a = int(input())
i=0
sum=0
#a不等於0的時候，i就+1；等於0的話就跳出迴圈print出來
while a!=0:
  i +=1
  sum+=a
  #後面輸入的值繼續放進去判斷，就不用一開始就打一堆變數進去
  a = int(input())
print(sum)

#6.7
#取平均
a = int(input())
i=0
sum=0
#a不等於0的時候，i就+1；等於0的話就跳出迴圈print出來
while a!=0:
  i +=1
  sum+=a
  #後面輸入的值繼續放進去判斷，就不用一開始就打一堆變數進去
  a = int(input())
#"%.2f"%(sum/i)指的是取平均之後，留到小數點後2位
#看要取幾位，就改f前面的數字
#如果有兩個值分別留不同位數
#ex:"%.2f %.1f"%(5/3,2/6)  
#則是5/3取到小數點後2位，2/6取小數點後1位
print("%.2f"%(sum/i))

#6.8



#6.F
#費式數列:1,1,2,3,5,8,13,21,34...
#求第幾個值的數字是多少
#ex:input:6 output:8  第6個位置的數字為8
n=int(input())
a=1
b=1
i=3
while i<=n:
  c=a+b
  print(c,end=" ")
  a,b=b,c
  i+=1
#上面的話就是費式數列
n=int(input())
a=1
b=1
i=3
while i<=n:
  a,b=b,a+b
  i+=1
print(b,end=" ")