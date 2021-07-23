import csv
from collections import Counter 
with open('height.csv') as f:
    data = csv.reader(f)
    filedata = list(data)
filedata.pop(0)
newdata = []
for i in range(len(filedata)):
    num = filedata[i][2]
    newdata.append(float(num))
print(newdata)  
n = len(newdata)
total = 0
for x in newdata:
    total += x
mean = total/n
print('mean is '+ str(mean))    
newdata.sort()
if n%2 == 0:
    m1 = float(newdata[n//2])
    m2 = float(newdata[n//2 - 1])
    m = (m1 + m2)/2
else:
    m = newdata[n//2]
print('median is '+str(m))
