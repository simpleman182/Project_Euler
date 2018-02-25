lstnum = [2]
limit = 2000000
for num in range(3,limit +1):
	for i in range(2,int(num**0.5)+1):
		if num % i == 0:
			break
	else:
		print (num)
		lstnum.append(num)

print (sum(lstnum))

# 142913828922
# Runtime =  21.923160791397095
