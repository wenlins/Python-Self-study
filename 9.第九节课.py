#打印九九乘法表
for i in range(1,10):
    for a in range(1,i+1):
        print(str(a)+'×'+str(i)+'='+str(a*i)+' ',end=' ')
    print(' ')
# while 循环引用

while True :
    print('我不想写作业!!!')
n=0
while n<5:
          n=n+1
          print('我不想写作业!!!第%d次'%n)
