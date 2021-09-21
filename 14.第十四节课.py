import random
z = input('需要多少数字:')
a = [random.randint(0,100)for i in range(int(z))]
print(a)
for i in range(1,len(a)-1):
    for j in range (0,len(a)-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
        print(a)
print(a)
a.sort()
print(a)
a.sort(reverse=1)
print(a)
a.sort(reverse=0)
print(a)
