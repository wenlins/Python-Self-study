# 变量的定义
a=45
b=56
print('a=',a)
print('b=',b)


#两个变量互换数值
c=b
b=a
a=c
print('a=',a)
print('b=',b)

# == 判断
d=3
print(d==3)
print(int(d==3))
print(d==4)
print(int(d==4))
#判断表达式:>=,<=,>,<,==,!=,in

print('7>=9:',7>=9)
print('7>=5:',7>=5)
print('7>9:',7>9)
print('7<9:',7<9)
print('7==9:',7==9)
print('7!=9:',7!=9)

a='abcd'
print('a'in a)

# 与或否
# and 两者都为 true 结果为 true 有一个为 false 结果为false
# or 有一个为true结果为true
# not和结果相反
#and 应用
print('2>1 and 3>2:',2>1 and 3>2)
print('2<1 and 3>2:',2<1 and 3>2)
# or 应用
print('2>1 or 3>2:',2>1 or 3>2)
print('2<1 or 3>2:',2<1 or 3>2)

# not 应用
print('not(2>1 or 3>2):',not(2>1 or 3>2))
print('not(2<1 or 3>2):',not(2<1 or 3>2))
