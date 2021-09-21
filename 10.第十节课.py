#输出0-20以内的偶数
i=0
while i<21:
 if i%2==0:
  print('%d是偶数'%i)
 i=i+1
#给你500个美女，你从里面选十个人当老婆

import random

renshu=500

while renshu>490:
 sj=random.randint(1,renshu)
 dafu=input(str(sj)+'号人，你满意吗？请选择(y/n)')
 if dafu=='y':
    renshu-=1
 print('还有%d位人'%renshu)
 
#打印出1000以内的斐波那契数列
#后面的数字是前面两个数字的和
#1,2,3,5,8,13,21,34
 
a = 1
b = 1
c = 1
while a+b<1000:
 c=b
 b=a+b
 a=c
 print(b)
