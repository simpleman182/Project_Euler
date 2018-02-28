import time
start = time.time()
x = 1
def factor(n):
	number = 0
	for i in range(1,int(n**0.5)+1):
		if n % i == 0:
			number += 2
		else:
			continue
	return number 
for i in range(2,100000):
	x += i
	if factor(x) >= 500:
		print (x)
		break
elapsed = time.time() - start
print (elapsed)
