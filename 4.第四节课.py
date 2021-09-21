#数据类型 int() float() str()
# 整型 int()
a=1
print(type(a))
# 浮点型 float()
b=1.0
print(type(b))
# 字符串型 str()
c='1'
print(type(c))
# 布尔型
d=True
print(type(d))
print('----数据类型转换----')
e=1
print('本来的数据类型:',type(e))
e=float(e)
print(e)
print('转成浮点数串型:',type(e))
e=str(e)
print(e)
print('转成字符串型:',type(e))
print('----输入函数----')
# 输入函数 input
name=input('请输入你的名字:')
print('你好！原来你叫',name)
#输入算式
jieguo=input('输入一个算式:')
print(jieguo)
# eval 函数
print(eval(jieguo))
print(jieguo,'=',eval(jieguo))
