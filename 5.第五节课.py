import random
jiqi = random.randint(1,3)
jilu = int(input('1-石头，2-剪刀，3-布:'))
if jiqi == 1:
    print('石头')
elif jiqi == 2:
    print('剪刀')
elif jiqi == 3:
    print('布')
if jilu == 1 and jiqi == 2 or jilu == 2 and jiqi == 3 or jilu == 3 and jiqi == 1:
    print('人赢')
elif jiqi == jilu:
    print('平局')
else:
    print('机器人赢')
