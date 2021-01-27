#8.1
#row-major 橫資料 
#column-major 直資料
#輸入矩陣為n*m，放入數字，最後輸入要*幾倍
#input
# 3 4
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34
# 2
# output
# 22 24 26 28
# 42 44 46 48
# 62 64 66 68
row, col = [ int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(row)]
mul = int(input())
for i in range(row):
    for j in range(col):
        a[i][j] *= mul
for row in a:
    print(*row)


#8.3
#生成n*n，對角線為0的矩陣
# 0 1 2 3 4
# 1 0 1 2 3
# 2 1 0 1 2
# 3 2 1 0 1
# 4 3 2 1 0
n=int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]= abs(i-j)
for row in a:
    print(*row)

#8.4
#產出n*m的矩陣，對角為1，上半部為0，下半部為2
# input 4
# 0 0 0 1
# 0 0 1 2
# 0 1 2 2
# 1 2 2 2

#8.7
#產出n*m的矩陣，最左上角為'.'，且'.'與'*'不相鄰
#input 6 8
#output
# . * . * . * . *
# * . * . * . * .
# . * . * . * . *
# * . * . * . * .
# . * . * . * . *
# * . * . * . * .
n,m=[ int(i) for i in input().split()]
a = [['.'] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i+j)%2!=0:
            a[i][j]='*'
for row in a:
    print(*row)