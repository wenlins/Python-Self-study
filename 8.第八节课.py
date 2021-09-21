# 打印金字塔
for i in range(1,11):
 print('  '*(10-i),'*'*(2*i-1))
# break 应用
for i in range(1,15):
    print('执行任务第%d天'%i)
    xinhao= input('你遇到危险了吗？(y/n)')
    if xinhao=='y':
     break 
print('卧底有危险！营救！') 
#continue 应用
for i in range(1,21):
 print('行军第%d天'%i)
 xinhao=input('战马还能不能行走了？(y/n)')
 if(xinhao=='y'):
  continue
 else:print('休息一个小时！')
