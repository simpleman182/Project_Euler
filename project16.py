import time
start = time.time()
string = str(2**1000)
result = 0
for i in string:
	i = int(i)
	result += i

eslaped = time.time() - start
print (result,eslaped)
