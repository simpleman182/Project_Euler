lstnum = [2]
limit = 2000000
for num in range(3,limit +1):
	for i in range(2,num):
		if num % i == 0:
			break
	else:
		print (num)
		lstnum.append(num)

print (sum(lstnum))
#1709600813 => 200000