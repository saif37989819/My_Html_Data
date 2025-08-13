import time
n_M= input('Enter your Name \n')
 
recentTime= time.strftime('%H:%M:%S')
print(recentTime)
globalTime= int(time.strftime('%H'))
globalMin= int(time.strftime('%M'))
if  globalTime >= 14 and  globalTime <= 16:
     print(n_M, 'Bro, Good Morning')
elif globalMin > 15 and globalTime >7 and globalTime < 9:
    print(n_M,  'Bro, Good Night')
else:
     print(n_M,  'Bro, Good Night')
 