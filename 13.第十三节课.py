
a = ['3','1','4','6','2','5','7','8']

#a[0] = '123'
print(a)
b = input('你需要那个数字:')
if b in a:
    print(a.index(b))
else:
    print('emm')
a.sort()
print(a)


import random
z = input('需要多少数字:')
a = [random.randint(0,10000)for i in range(int(z))]
print(a)
for i in range(0,len(a)-1):
    for q in range (i+1,len(a)-1):
        if a[i] > a[q]:
            a[i],a[q] = a[q],a[i]
print(a)
