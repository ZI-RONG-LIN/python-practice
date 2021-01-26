#5.1
# Read a string:
s = input()
# Print a string:
# print(s)
print(s[2])
#倒數第二個字
print(s[-2])
#印前五個字
print(s[:5])
print(s[:-2])
#每隔兩個位置取字
print(s[0::2])
#取奇數位置的字
print(s[1::2])
#從最後面開始數
print(s[::-1])
#從後面取偶數位置字
print(s[::-2])
print(len(s))

#5.2
#算總共有幾個字
#HELLO WORLD ->2
# Read a string:
s = input()
# Print a string:
# print(s)
print(s.count(' ')+1)

#5.3
#字串剖半後前後交換，奇數的話以中位數的字作為開頭
# Qwerty
# rtyQwe
# Read a string:
s = input()
# Print a string:
# print(s)
from math import ceil
print(s[ceil(len(s)/2):]+s[:ceil(len(s)/2)])

#5.4
#以空白把兩個字分開後，前後對調
# Hello, world!
# world! Hello,
# Read a string:
s = input()
# Print a string:
# print(s)
k=s.find(' ')
print(s[k+1:],s[:k])
#解二
#split()空白切割
word1, word2 = input().split()
print(word2, word1)

#5.5
#如果沒有f，則顯示-1；
#有兩個f，則顯示第一個和最後一個的位置
#只有一個f，則顯示左到右數來的位置
# Read a string:
s = input()
# Print a string:
# print(s)
if s.count('f') > 1:
  print(s.find('f'),s.rfind('f'))
elif s.count('f') == 0 :
  print("-1")
else:
  print(s.find('f'))
#解二
s = input()
if s.find('f') == s.rfind('f'):
  print(s.find('f'))
else:
  print(s.find('f'), s.rfind('f'))

#5.6
#找第二個p出現的位置
#如果都沒有，則顯示-2
#如果只有一個，則顯示-1
# Read a string:
s = input()
# Print a string:
# print(s)
a=s.find('p')
if s.find('p')==-1:
  print(-2)
else:
  print(s.find('p',a+1))

#5.7
# 找第一個和最後一個h，中間的字都去掉
# In the hole in the ground there lived a hobbit
# In tobbit
# Read a string:
s = input()
# Print a string:
# print(s)
print(s[:s.find('h')]+s[s.rfind('h')+1:])

#5.8
# 找第一個和最後一個h，中間的字反轉
#先用find()找第一個，rfind()找最後一個
#中間則是從後面rfind()到前面find()，以-1的方式讀字出來
# In the hole in the ground there lived a hobbit
# In th a devil ereht dnuorg eht ni eloh ehobbit
# Read a string:
s = input()
# Print a string:
# print(s)
print(s[:s.find('h')]+s[s.rfind('h'):s.find('h'):-1]+s[s.rfind('h'):])

#5.C
# 把可以被3整除的位置的字拿掉
# 把可以被3整除的字拿出來依序補進空的字串裡面，最後印出來
# Read a string:
s = input()
d=''
# Print a string:
# print(s)
for i in range(len(s)):
  if i%3!=0:
    d += s[i]
print(d)
