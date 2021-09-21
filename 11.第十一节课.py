# 创建一个列表
a = []
b = ['1','abc','2.3']
print(a)
print(b)
# 输出列表中指定位置的内容
print(b[1])
#往列表中添加元素
c = []
name = input('请输入你的名字:')
c.append(name)
print(c)

# 往列表连续添加元素
names=[]
for i in range(1,7):
           name = input('请输入第'+str(i)+'个名字:')
           names.append(name)

for j in range(0,6):
           print(names[j])

d = []
while True:

       shuzi= input('请输入数字(按回车键结束):')
                    
       if shuzi =='':
           break
       d.append(float(shuzi))


print('你一共输入了%d个数字'%(len(d)))
print('最大值是%f'%max(d),'最小值是%f'%min(d))




       




    
