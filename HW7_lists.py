#7.1
#input 5 6 7 8 9 
#output 5 7 9
#每個字串切割，每個元素都轉成數字
a = [int(s) for s in input().split()]
#印出奇數位置的元素，並轉呈數值
print(*a[::2])

#7.2
#印出偶數
#input 1 2 2 3 3 3 4
#output 2 2 4
a = [int(s) for s in input().split()]
for i in a:
  if i%2==0:
    print(i,end=" ")

#7.3
#找出比左邊數字大的值
#input 1 5 2 4 3
#output 5 4 
a = [int(s) for s in input().split()]
#用range跑a的全部索引值，一一比對之後print出來符合if條件的資料
for i in range(1,len(a)):
  if a[i-1]<a[i]:
    print(a[i],end=" ")

#7.5
#找出筆左右兩個數字還大的數字個數
#input 1 5 1 5 1
#output 2
a = [int(s) for s in input().split()]
count=0
#range只選左右兩邊有數字的去做，所以頭尾要去掉
#有符合的話就count+1
for i in range(1,len(a)-1):
  if a[i-1]<a[i] and a[i+1]<a[i]:
    count+=1
print(count)

#7.6
#找出不一樣的數字有幾個
#把input的值丟進set裡面(因set中數值必須不重複)，再print出長度
a = [int(s) for s in input().split()]
print(len(set(a)))
#老師解
a = [int(s) for s in input().split()]
b=[]
count=0
for i in a:
    if i not in b:
        b.append(i)
        count+=1
print(count)
#解二
num_distinct = 1
a = [int(s) for s in input().split()]
for i in range(1, len(a)):
  if a[i - 1] != a[i]:
    num_distinct += 1
print(num_distinct)

#7.A
#計算數值相同的組合數
#ex 1 2 3 2 3  -> 2
#ex 1 1 1 1 1  -> 10
#一種方式是用i和j的迴圈，i去跟j去比
#另一種是先把一樣的數字放一起，分別計算Cn取2的組合數再相加
a = [int(s) for s in input().split()]
count=0
for i in range(len(a)):
  for j in range(i+1,len(a)):
    if a[i]==a[j]:
      count+=1
print(count)

#7.B
#找出只顯示一次的數字
#輸入8個點，米字路徑上不會有其他點
#可以找八皇后，遞迴經典題
